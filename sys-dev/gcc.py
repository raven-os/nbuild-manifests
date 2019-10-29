#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
import stdlib.split.system
import stdlib.deplinker.elf
import stdlib.build
import stdlib.extract
from typing import Dict
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


def check_gcc():
    # Remove a test known to cause problem
    os.remove('../gcc/testsuite/g++.dg/pr83239.C')

    # Run the GCC tests as a non-privileged user
    stdlib.cmd('chown -Rv nobody . ')
    stdlib.cmd('ulimit -s 32768 ; su nobody -s /bin/bash -c "PATH=$PATH make -k check"', fail_ok=True)

    # Print a test summary
    stdlib.cmd('../contrib/test_summary')


def install_gcc():
    build = stdlib.build.current_build()
    target = os.environ['TARGET']

    # Install the main components of gcc and g++
    make('install', f'DESTDIR={build.install_cache}')

    # Compatibility symlink to enable building programs with Link Time Optimization
    #stdlib.cmd(f'install -v -dm755 {build.install_cache}/usr/lib64/bfd-plugins')
    with stdlib.pushd(build.install_cache):
        os.makedirs('usr/lib64/bfd-plugins/', exist_ok=True)
        os.symlink(f'../gcc/{target}/8.2.0/liblto_plugin.so', 'usr/lib64/bfd-plugins/liblto_plugin.so')


def split_gcc() -> Dict[str, stdlib.package.Package]:
    build = stdlib.build.current_build()
    target = os.environ['TARGET']

    gcc = stdlib.package.Package(
        stdlib.package.PackageID('gcc'),
    )

    gpp = stdlib.package.Package(
        stdlib.package.PackageID('g++'),
    )

    cpp = stdlib.package.Package(
        stdlib.package.PackageID('cpp'),
    )

    libs = stdlib.package.Package(
        stdlib.package.PackageID(
            category='sys-libs',
            name='gcc-libs',
        ),
    )

    libs_dev = stdlib.package.Package(
        stdlib.package.PackageID(
            category='sys-libs',
            name='gcc-libs-dev',
        ),
    )

    gcc.drain(
        'usr/bin/*gcc*',
        'usr/bin/*gcov*',
        'usr/lib{,64}/bfd-plugins/*.so',
        'usr/lib{,64}/*-gdb.py',
        f'usr/lib{{,64}}/gcc/{target}/*/collect2',
        f'usr/lib{{,64}}/libcc1*',
        f'usr/lib{{,64}}/gcc/{target}/*/libcc1*',
        f'usr/lib{{,64}}/gcc/{target}/*/libcp1*',
        f'usr/lib{{,64}}/gcc/{target}/*/liblto_plugin*',
        f'usr/lib{{,64}}/gcc/{target}/*/lto*',
        'usr/share/man/*/*{gcc,gcov}*',
        f'usr/lib64/gcc/{target}/*/plugin/',
    )

    gpp.drain(
        'usr/bin/*{g,c}++*',
        'usr/share/man/*/*g++*',
        'usr/share/man/*/*gcc*',
        f'usr/lib64/gcc/{target}/*/cc1plus',
    )

    cpp.drain(
        'usr/bin/*cpp*',
        'usr/share/man/*/*cpp*',
        f'usr/lib64/gcc/{target}/*/cc1', # Unfortunately, cpp cannot work without cc1
    )

    libs.drain(
        'usr/lib{,64}/*.so.*',
        'usr/lib{,64}/*.o',
        'usr/lib{,64}/*.spec',
        f'usr/lib64/gcc/{target}/*/*.so.*',
        f'usr/lib64/gcc/{target}/*/install-tools/',
        'usr/share/gcc-*/python/',
        'usr/share/locale/',
        'usr/share/man/man7/',
    )

    libs_dev.drain(
        'usr/lib{,64}/*.so',
        'usr/lib{,64}/*.a',
        f'usr/lib64/gcc/{target}/*/*.{{o,a,so}}',
        f'usr/lib64/gcc/{target}/*/include*/',
        'usr/include/c++/',
    )

    # Remove .la files that have been drained by accident
    gcc.remove(
        'usr/lib{,64}/*.la',
        'usr/lib{,64}/gcc/x86_64-raven-linux-gnu/8.2.0/*.la',
        'usr/lib{,64}/gcc/x86_64-raven-linux-gnu/8.2.0/plugin/*.la',
    )

    libs_dev.depends_on(libs)
    libs_dev.rdepends_on('sys-libs/glibc-dev', '^2.28')

    cpp.depends_on(libs, f'^{build.semver}')

    gcc.depends_on(cpp)
    gcc.depends_on(libs, f'^{build.semver}')
    gcc.depends_on(libs_dev)
    gcc.rdepends_on('sys-dev/binutils', '*')

    gpp.depends_on(cpp)
    gpp.depends_on(libs, f'^{build.semver}')
    gpp.depends_on(libs_dev)
    gpp.depends_on(gcc)
    gpp.rdepends_on('sys-dev/binutils', '*')

    return {
        gcc.id.short_name(): gcc,
        gpp.id.short_name(): gpp,
        cpp.id.short_name(): cpp,
        libs.id.short_name(): libs,
        libs_dev.id.short_name(): libs_dev,
    }


@manifest(
    name='gcc',
    category='sys-dev',
    description='''
    The GNU Compiler Collection
    ''',
    tags=['gnu', 'compiler', 'c', 'cpp', 'go', 'fortran', 'ada', 'd'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://gcc.gnu.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.2.0',
            'fetch': [{
                    'url': 'http://ftp.lip6.fr/pub/gcc/releases/gcc-8.2.0/gcc-8.2.0.tar.xz',
                    'sha256': '196c3c04ba2613f893283977e6011b2345d1cd1af9abeac58e916b1aab3e0080',
                },
            ],
        },
    ],
)
def build(build):
    os.environ['SED'] = 'sed'  # TODO FIXME
    target = os.environ['TARGET']

    packages = autotools.build(
        build_folder='build',
        configure=lambda: configure(
            '--enable-languages=c,c++',
            '--disable-multilib',
            '--disable-bootstrap',
            '--disable-libmpx',
            '--with-system-zlib',
            '--docdir=/usr/share/doc/',
            binary='../configure',
        ),
        install=install_gcc,
        split=split_gcc,
        deplinker=lambda packages: stdlib.deplinker.elf.elf_deplinker(
            packages,
            search_patterns= [
                '{,usr/}bin/*',
                '{,usr/}lib{,32,64}/*',
                f'usr/lib{{,64}}/gcc/{target}/*/*',
            ],
        ),
        check=check_gcc,
    )

    # Move a misplaced file
    packages['sys-dev/gcc'].move(
        'usr/lib{,64}/*-gdb.py',
        'usr/share/gdb/auto-load/usr/lib/',
    )

    # Create a bunch of symlinks required to satisfy external utilities
    packages['sys-dev/cpp'].make_symlink('../usr/bin/cpp', 'lib/cpp')
    packages['sys-dev/gcc'].make_symlink('gcc', 'usr/bin/cc')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/gcc-libs'].rdepends_on('raven-os/corefs', '*')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.manifest import manifest


def patch_bzip2():
    # Apply all patches
    stdlib.patch.patch_all()

    # Ensure the installation of symbolic links are relative
    stdlib.cmd("sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\\1@' Makefile")

    # Ensure the man pages are installed into the correct location
    stdlib.cmd("sed -i 's@(PREFIX)/man@(PREFIX)/share/man@g' Makefile")

    # Clean the installation and use a different Makefile than the default one
    stdlib.cmd('make -f Makefile-libbz2_so')
    make('clean')


def split_bzip2():
    packages = stdlib.split.system.system()

    # Prefer the shared version of bzip2, and not the statically-linked one
    packages['sys-apps/bzip2'].drain_build_cache('bzip2-shared', 'usr/bin/bzip2')

    # Install the shared library
    packages['sys-apps/bzip2'].drain_build_cache('libbz2.so*', 'usr/lib64/')
    packages['sys-apps/bzip2'].make_symlink('libbz2.so.1.0', 'usr/lib64/libbz2.so.1')
    packages['sys-apps/bzip2-dev'].make_symlink('libbz2.so.1.0', 'usr/lib64/libbz2.so')

    # Make bunzip2 and bzcat symlinks to bzip2
    packages['sys-apps/bzip2'].remove('usr/bin/{bzcat,bunzip2}')
    packages['sys-apps/bzip2'].make_symlink('bzip2', 'usr/bin/bunzip2')
    packages['sys-apps/bzip2'].make_symlink('bzip2', 'usr/bin/bzcat')

    return packages


@manifest(
    name='bzip2',
    category='sys-apps',
    description='''
    A high-quality data compression program and library.
    ''',
    tags=['archive', 'compression', 'zip'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.sourceware.org/bzip2/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.6',
            'fetch': [{
                    'url': 'https://sourceware.org/pub/bzip2/bzip2-1.0.6.tar.gz',
                    'sha256': 'a2848f34fcd5d6cf47def00461fcb528a0484d8edef8208d6d2e2909dc61d9cd',
                }, {
                    'file': './install_docs.patch'
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_bzip2,
        configure=None,
        install=lambda: make('install', f'PREFIX={stdlib.build.current_build().install_cache}/usr/'),
        check=None,  # Tests are already run when compiling
        split=split_bzip2,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/bzip2'].rdepends_on('raven-os/corefs', '*')

    return packages

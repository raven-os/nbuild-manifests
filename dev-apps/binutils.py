#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import shutil
import stdlib.split.system
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


def split_binutils():
    packages = stdlib.split.system.system()

    # Binutils creates libraries that have binutils' version in their name *before* the `.so`.
    # The splitter wrongly attribute them to the development version of binutils.
    packages['dev-apps/binutils'].drain_package(
        packages['dev-apps/binutils-dev'],
        'usr/lib64/lib*-*.so'
    )

    return packages


@manifest(
    name='binutils',
    category='dev-apps',
    description='''
    A set of tools to link, assemble and manipulate object files.
    ''',
    tags=['gnu'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2, stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/binutils/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.32.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/binutils/binutils-2.32.tar.xz',
                    'sha256': '0ab6c55dd86a92ed561972ba15b9b70a8b9f75557f896446c82e8b36e473ee04',
                },
            ],
        },
    ],
)
def build(build):
    target = os.environ['TARGET']

    packages = autotools.build(
        configure=lambda: configure(
            '--enable-gold',
            '--enable-ld=default',
            '--enable-plugins',
            '--enable-64-bit-bfd',
            '--with-system-zlib',
        ),
        split=split_binutils,
    )

    # Drain pre-installed link scripts
    packages['dev-apps/binutils'].drain(
        f'usr/{target}/lib/ldscripts/*'
    )

    # Move some folders to a more convenient location
    packages['dev-apps/binutils'].move(
        f'usr/{target}/lib/*',
        f'usr/lib64/{target}/',
    )

    packages['dev-apps/binutils'].move(
        f'usr/{target}/bin/*',
        f'usr/bin/{target}/',
    )

    # Prefer usr/bin/ARCH-xxx instead of usr/bin/ARCH/xxx
    with stdlib.pushd(packages['dev-apps/binutils'].wrap_cache):
        for filename in os.listdir(f'usr/bin/{target}/'):
            shutil.move(f'usr/bin/{target}/{filename}', f'usr/bin/{target}-{filename}')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/binutils'].requires('raven-os/corefs')

    return packages

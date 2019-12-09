#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import shutil
from stdlib.template.cmake import cmake
from stdlib.template import autotools
from stdlib.manifest import manifest


def install_albinos():
    build = stdlib.build.current_build()

    os.makedirs(f'{build.install_cache}/usr/bin/', exist_ok=True)
    os.makedirs(f'{build.install_cache}/usr/lib64/', exist_ok=True)
    os.makedirs(f'{build.install_cache}/usr/include/', exist_ok=True)
    os.makedirs(f'{build.install_cache}/etc/systemd/system/', exist_ok=True)

    with stdlib.pushd(build.build_cache):
        # Copy the service
        shutil.move('build/albinos-service', f'{build.install_cache}/usr/bin/albinos-service')
        shutil.move('service/albinos.service', f'{build.install_cache}/etc/systemd/system/albinos.service')

        # Copy the library
        shutil.move('lib/Albinos.h', f'{build.install_cache}/usr/include/Albinos.h')
        shutil.move('build/libalbinos.so', f'{build.install_cache}/usr/lib64/libalbinos.so.0.0')
        os.symlink('libalbinos.so.0.0', f'{build.install_cache}/usr/lib64/libalbinos.so.0')
        os.symlink('libalbinos.so.0.0', f'{build.install_cache}/usr/lib64/libalbinos.so')


@manifest(
    name='albinos',
    category='sys-libs',
    description='''
    Raven-OS configuration unification service and library.
    ''',
    tags=['raven-os', 'raven', 'configuration', 'service'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://github.com/raven-os/albinos',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.0.224',
            'fetch': [{
                    'git': 'https://github.com/raven-os/albinos.git',
                    'commit': '104faf1294b89d43c6994d644ad300f4043d6622',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'dev-libs/sqlite-dev',
    ]
)
def build(build):
    return autotools.build(
        build_folder='build',
        configure=lambda: cmake('..'),
        install=install_albinos,
    )

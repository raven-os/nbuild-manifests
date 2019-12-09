#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.make import make
from stdlib.template import basic
from stdlib.manifest import manifest


def install_linux():
    build = stdlib.build.current_build()

    boot_dir = f'{build.install_cache}/boot'
    usr_dir = f'{build.install_cache}/usr'

    os.makedirs(boot_dir)
    os.makedirs(usr_dir)

    make('install', f'INSTALL_PATH={boot_dir}/')
    make('modules_install', f'INSTALL_MOD_PATH={usr_dir}/')
    make('headers_install', f'INSTALL_HDR_PATH={usr_dir}/')


@manifest(
    name='linux',
    category='kernel',
    description='''
    The Linux kernel.
    ''',
    tags=['linux', 'kernel'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://www.kernel.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.2.17',
            'fetch': [{
                    'url': 'https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.2.17.tar.xz',
                    'sha256': '7b3b8ad09ea936b4216dd02c5fc2ef39c8f58935d0a81ab9690f0fc451102df9',
                }, {
                    'file': './config-5.2.17',
                    'rename': '.config',
                }
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/flex',
        'sys-libs/openssl-dev',
        'dev-apps/bc',
    ]
)
def build(build):

    # TODO:
    #   - Include the configuration in /boot/
    #   - Symlink or rename vmlinuz to vmlinuz-X.Y.Z.
    #   - Use an initramfs

    packages = basic.build(
        configure=lambda: make('olddefconfig'),
        compile=make,
        install=install_linux,
        deplinker=None,
    )

    packages['kernel/linux'].drain(
        'usr/lib/modules/**/*.ko',
        'usr/lib/modules/**/modules.*',
        'boot/*',
    )

    packages['kernel/linux-dev'].drain(
        'usr/lib/modules/**.dbg',
    )

    # Remove useless files
    with stdlib.pushd(packages['kernel/linux'].wrap_cache):
        stdlib.cmd(f'find \\( -name .install -o -name ..install.cmd \\) -delete')

    # Drain documentation
    packages['kernel/linux-doc'].drain_build_cache('Documentation/*', 'usr/doc/linux/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['kernel/linux'].requires('raven-os/corefs')

    return packages

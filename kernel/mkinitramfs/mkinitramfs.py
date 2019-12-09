#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
from stdlib.template import basic
from stdlib.split.drain_all import drain_all
from stdlib.manifest import manifest


def install_mkinitramfs():
    pass


@manifest(
    name='mkinitramfs',
    category='kernel',
    description='''
    A set of tools to build and install an initramfs.
    ''',
    tags=['linux', 'kernel', 'debian'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://debian.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.0',
            'fetch': [{
                    'file': './mkinitramfs',
                }, {
                    'file': './init',
                },
            ],
        },
    ],
)
def build(build):
    packages = basic.build()

    packages['kernel/mkinitramfs'].drain_build_cache('mkinitramfs', 'usr/bin/')
    packages['kernel/mkinitramfs'].drain_build_cache('init', 'usr/share/mkinitramfs/')

    packages['kernel/mkinitramfs'].requires('sys-apps/coreutils')
    packages['kernel/mkinitramfs'].requires('sys-apps/bash')
    packages['kernel/mkinitramfs'].requires('sys-apps/util-linux')
    packages['kernel/mkinitramfs'].requires('sys-apps/systemd')
    packages['kernel/mkinitramfs'].requires('sys-apps/cpio')

    return packages

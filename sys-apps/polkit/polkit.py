#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import stdlib.split.drain_all
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.patch import patch
from stdlib.manifest import manifest


def patch_polkit():
    stdlib.cmd("groupadd -fg 27 polkitd &&                          \
        useradd -c 'PolicyKit Daemon Owner' -d /etc/polkit-1 -u 27  \
        -g polkitd -s /bin/false polkitd &&                         \
    ")
    patch("-Np1 -i ./polkit-0.116-fix_elogind_detection-1.patch")


@manifest(
    name='polkit',
    category='sys-apps',
    description='''
    Application development toolkit for controlling system-wide privileges.
    ''',
    tags=['privileges', 'polkit'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://gitlab.freedesktop.org/polkit/polkit/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.116.0',
            'fetch': [{
                'url': 'https://www.freedesktop.org/software/polkit/releases/polkit-0.116.tar.gz',
                'sha256': '88170c9e711e8db305a12fdb8234fac5706c61969b94e084d0f117d8ec5d34b1',
            }, {
                'file': './polkit-0.116-fix_elogind_detection-1.patch'
            }
            ],
        },
    ],
    build_dependencies=[
        'dev-libs/glib-dev',
        'sys-libs/libtool-dev',
        'dev-libs/gobject-introspection-dev',
        'dev-apps/js-dev',
        'sys-libs/expat-dev',
        'sys-apps/systemd-dev',
        'sys-libs/pam-dev',
        'dev-perl/xml-parser'
    ]
)
def build(build):
    packages = autotools.build(
        patch=patch_polkit,
        configure=lambda: configure('--with-os-type=LFS',
                                    '--enable-libsystemd-login=yes',
                                    '--disable-man-pages')
    )

    packages['sys-apps/polkit-dev'].drain('usr/lib64/')
    packages['sys-apps/polkit-dev'].drain('usr/lib/')
    packages['sys-apps/polkit'].drain('usr/share/')

    return packages

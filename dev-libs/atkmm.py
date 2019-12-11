#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='atkmm',
    category='dev-libs',
    description='''
    C++ bindings for ATK.
    ''',
    tags=['atk', 'cpp', 'bindings'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtkmm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.28.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/atkmm/2.28/atkmm-2.28.0.tar.xz',
                'sha256': '4c4cfc917fd42d3879ce997b463428d6982affa0fb660cafcc0bc2d9afcedd3a',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/glib-dev',
        'dev-libs/glibmm-dev',
        'dev-libs/atk-dev',
        'dev-libs/libsigc++-dev',
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/atkmm-dev'].drain(
        'usr/lib64/atkmm-*/{include,proc}'
    )

    return packages

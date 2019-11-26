#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libinput',
    category='dev-libs',
    description='''
    A library that handles input devices for display servers and other applications that need to directly deal with input devices.
    ''',
    tags=['input', 'mouse', 'keyboard'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT, stdlib.license.License.CUSTOM],
    upstream_url='https://bitmath.org/code/mtdev/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.5',
            'fetch': [{
                    'url': 'https://www.freedesktop.org/software/libinput/libinput-0.5.0.tar.xz',
                    'sha256': '349c63d8819ddfc1a35fc8bcf352256b952ae22b1ff370fd819a16f67e801ea7',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-libs/evdev-dev',
        'dev-libs/mtdev-dev',
        'sys-apps/systemd-dev',
    ]
)
def build(build):
    return autotools.build()

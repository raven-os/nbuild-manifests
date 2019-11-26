#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='libinput',
    category='dev-libs',
    description='''
    A library that handles input devices for display servers and other applications that need to directly deal with input devices.
    ''',
    tags=['input', 'mouse', 'keyboard'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.freedesktop.org/wiki/Software/libinput/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.14.3',
            'fetch': [{
                    'url': 'https://www.freedesktop.org/software/libinput/libinput-1.14.3.tar.xz',
                    'sha256': '0feb3a0589709cc1032893bfaf4c49150d5360bd9782bec888f9e4dd9044c5b7',
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
    return meson_ninja.build()

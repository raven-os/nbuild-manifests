#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='evdev',
    category='dev-libs',
    description='''
    A handler library for evdev events and devices.
    ''',
    tags=['evdev', 'device'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.freedesktop.org/wiki/Software/libevdev/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.8.0',
            'fetch': [{
                    'url': 'https://www.freedesktop.org/software/libevdev/libevdev-1.8.0.tar.xz',
                    'sha256': '20d3cae4efd277f485abdf8f2a7c46588e539998b5a08c2c4d368218379d4211',
                },
            ],
        },
    ],
)
def build(build):
    return autotools.build()

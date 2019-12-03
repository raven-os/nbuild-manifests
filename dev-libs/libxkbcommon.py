#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxkbcommon',
    category='dev-libs',
    description='''
    A keymap compiler and support library which processes a reduced subset of keymaps as defined by the XKB specification.
    ''',
    tags=['x11', 'xorg', 'keyboard', 'keymap'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xkbcommon.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.8.4',
            'fetch': [{
                'url': 'https://xkbcommon.org/download/libxkbcommon-0.8.4.tar.xz',
                'sha256': '60ddcff932b7fd352752d51a5c4f04f3d0403230a584df9a2e0d5ed87c486c8b',
            }],
        },
    ],
    build_dependencies=[
        'dev-resources/xkeyboard-config',
        'dev-libs/xcb-dev',
        'sys-libs/x11-dev',
    ]
)
def build(build):
    return autotools.build()

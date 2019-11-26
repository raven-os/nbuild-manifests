#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure


@manifest(
    name='xcb',
    category='dev-libs',
    description='''
    The libxcb package provides an interface to the X Window System protocol.
    ''',
    tags=['dev', 'protocol', 'xorg', 'x11'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.13.1',
            'fetch': [{
                'url': 'https://xcb.freedesktop.org/dist/libxcb-1.13.1.tar.bz2',
                'sha256': 'a89fb7af7a11f43d2ce84a844a4b38df688c092bf4b67683aef179cdf2a647c4',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorg-util-macros-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/xcb-proto',
        'dev-python/xcbgen',
        'dev-libs/xau-dev',
        'dev-libs/xdmcp-dev'
    ]
)
def build(build):
    return autotools.build(
        patch=lambda: stdlib.cmd('sed -i "s/pthread-stubs//" configure'),
        configure=lambda: configure('--without-doxygen'),
    )

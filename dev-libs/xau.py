#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xau',
    category='dev-libs',
    description='''
    The Xau package contains a library implementing the X11 Authorization Protocol.
    ''',
    tags=['dev', 'protocol', 'xorg', 'x11'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.9',
            'fetch': [{
                'url': 'https://www.x.org/pub/individual/lib/libXau-1.0.9.tar.bz2',
                'sha256': 'ccf8cbf0dbf676faa2ea0a6d64bcc3b6746064722b606c8c52917ed00dcb73ec',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorgproto-dev'
    ]
)
def build(build):
    return autotools.build()

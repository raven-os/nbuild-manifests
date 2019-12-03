#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxinerama',
    category='dev-libs',
    description='''
    A Xinerama extension library for X.
    ''',
    tags=['x11', 'xorg', 'xinerama'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.4',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXinerama-1.1.4.tar.bz2',
                'sha256': '0008dbd7ecf717e1e507eed1856ab0d9cf946d03201b85d5dcf61489bb02d720',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
    ]
)
def build(build):
    return autotools.build()

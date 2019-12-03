#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxcursor',
    category='dev-libs',
    description='''
    A cursor management library for X.
    ''',
    tags=['x11', 'xorg', 'cursor'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXcursor-1.2.0.tar.bz2',
                'sha256': '3ad3e9f8251094af6fe8cb4afcf63e28df504d46bfa5a5529db74a505d628782',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'dev-libs/libxfixes-dev',
        'dev-libs/libxrender-dev',
    ]
)
def build(build):
    return autotools.build()

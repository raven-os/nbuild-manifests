#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxfont2',
    category='dev-libs',
    description='''
    A font rasterisation library for X.
    ''',
    tags=['x11', 'xorg', 'font', 'rasterisation'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.0.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXfont2-2.0.3.tar.bz2',
                'sha256': '0e8ab7fd737ccdfe87e1f02b55f221f0bd4503a1c5f28be4ed6a54586bac9c4e',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/freetype-dev',
        'sys-libs/zlib-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/xtrans-dev',
        'dev-libs/libfontenc-dev',
    ]
)
def build(build):
    return autotools.build()

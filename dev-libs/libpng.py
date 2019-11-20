#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libpng',
    category='dev-libs',
    description='''
    The libpng package contains libraries used for reading and writing PNG files.
    ''',
    tags=['png', 'image'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='http://www.libpng.org/pub/png/libpng.html',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.6.37',
            'fetch': [{
                'url': 'https://downloads.sourceforge.net/libpng/libpng-1.6.37.tar.xz',
                'sha256': '505e70834d35383537b6491e7ae8641f1a4bed1876dbfe361201fc80868d88ca',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev'
    ]
)
def build(build):
    return autotools.build()

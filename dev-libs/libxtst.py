#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxtst',
    category='dev-libs',
    description='''
    An xlib-based client library for the XTEST and XRECORD extensions library.
    ''',
    tags=['x11', 'xorg'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXtst-1.2.3.tar.bz2',
                'sha256': '4655498a1b8e844e3d6f21f3b2c4e2b571effb5fd83199d428a6ba7ea4bf5204',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxi-dev',
        'dev-libs/libxfixes-dev',
    ]
)
def build(build):
    return autotools.build()

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxdamage',
    category='dev-libs',
    description='''
    A damaged region extension library.
    ''',
    tags=['x11', 'xorg', 'damage', 'region'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.5',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXdamage-1.1.5.tar.bz2',
                'sha256': 'b734068643cac3b5f3d2c8279dd366b5bf28c7219d9e9d8717e1383995e0ea45',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'dev-libs/libxfixes-dev',
        'sys-libs/xext-dev',
    ]
)
def build(build):
    return autotools.build()

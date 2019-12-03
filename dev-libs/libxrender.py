#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxrender',
    category='dev-libs',
    description='''
    A rendering extension client library for X.
    ''',
    tags=['x11', 'xorg', 'rendering', 'extension'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.9.10',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXrender-0.9.10.tar.bz2',
                'sha256': 'c06d5979f86e64cabbde57c223938db0b939dff49fdb5a793a1d3d0396650949',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
    ]
)
def build(build):
    return autotools.build()

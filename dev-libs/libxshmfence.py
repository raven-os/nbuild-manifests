#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxshmfence',
    category='dev-libs',
    description='''
    A library that exposes a event API on top of Linux futexes.
    ''',
    tags=['x11', 'xorg', 'futexe', 'shm', 'shared', 'memory', 'fence'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.3.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libxshmfence-1.3.tar.bz2',
                'sha256': 'b884300d26a14961a076fbebc762a39831cb75f92bed5ccf9836345b459220c7',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorgproto-dev',
    ]
)
def build(build):
    return autotools.build()

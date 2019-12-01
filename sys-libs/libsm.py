#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libsm',
    category='sys-libs',
    description='''
    A session management library for X.
    ''',
    tags=['x11', 'xorg', 'sm', 'session', 'management'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libSM-1.2.3.tar.bz2',
                'sha256': '2d264499dcb05f56438dee12a1b4b71d76736ce7ba7aa6efbf15ebb113769cbb',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libice-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/xtrans-dev',
        'sys-apps/util-linux-dev',
    ]
)
def build(build):
    return autotools.build()

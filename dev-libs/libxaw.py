#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxaw',
    category='dev-libs',
    description='''
    The Athena Widget library.
    ''',
    tags=['x11', 'xorg', 'athena', 'widget'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.13',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXaw-1.0.13.tar.bz2',
                'sha256': '8ef8067312571292ccc2bbe94c41109dcf022ea5a4ec71656a83d8cce9edb0cd',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxmu-dev',
        'sys-libs/libxpm-dev',
        'dev-libs/libxt-dev',
        'sys-libs/libsm-dev',
        'dev-libs/libice-dev',
    ]
)
def build(build):
    return autotools.build()

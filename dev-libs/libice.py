#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libice',
    category='dev-libs',
    description='''
    An Inter-Client Exchange library for X.
    ''',
    tags=['x11', 'xorg', 'ice', 'ipc'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.10',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libICE-1.0.10.tar.bz2',
                'sha256': '6f86dce12cf4bcaf5c37dddd8b1b64ed2ddf1ef7b218f22b9942595fb747c348',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorgproto-dev',
        'dev-libs/xtrans-dev',
    ]
)
def build(build):
    return autotools.build(
        configure=lambda: configure(
            'ICE_LIBS=-lpthread',
        )
    )

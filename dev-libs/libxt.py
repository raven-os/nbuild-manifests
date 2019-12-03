#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxt',
    category='dev-libs',
    description='''
    A toolkit library for X.
    ''',
    tags=['x11', 'xorg', 'toolkit'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXt-1.2.0.tar.bz2',
                'sha256': 'b31df531dabed9f4611fc8980bc51d7782967e2aff44c4105251a1acb5a77831',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/libsm-dev',
        'sys-libs/x11-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/libice-dev',
    ]
)
def build(build):
    return autotools.build()

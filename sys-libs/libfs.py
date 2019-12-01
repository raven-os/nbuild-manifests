#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libfs',
    category='sys-libs',
    description='''
    A Font Service client library for X.
    ''',
    tags=['x11', 'xorg', 'font'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.8',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libFS-1.0.8.tar.bz2',
                'sha256': 'c8e13727149b2ddfe40912027459b2522042e3844c5cd228c3300fe5eef6bd0f',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xtrans-dev',
    ]
)
def build(build):
    return autotools.build()

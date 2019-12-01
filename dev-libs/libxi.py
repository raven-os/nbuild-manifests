#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxi',
    category='dev-libs',
    description='''
    An input library for X.
    ''',
    tags=['x11', 'xorg', 'input'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.7.10',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXi-1.7.10.tar.bz2',
                'sha256': '36a30d8f6383a72e7ce060298b4b181fd298bc3a135c8e201b7ca847f5f81061',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxfixes-dev',
    ]
)
def build(build):
    return autotools.build()

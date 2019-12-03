#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libfontenc',
    category='dev-libs',
    description='''
    A font encoding library for X.
    ''',
    tags=['x11', 'xorg', 'font', 'encoding'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.4',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libfontenc-1.1.4.tar.bz2',
                'sha256': '2cfcce810ddd48f2e5dc658d28c1808e86dcf303eaff16728b9aa3dbc0092079',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'dev-libs/xorgproto-dev',
    ]
)
def build(build):
    return autotools.build()

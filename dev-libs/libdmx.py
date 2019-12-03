#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libdmx',
    category='dev-libs',
    description='''
    A Distributed Multihead extension library for X.
    ''',
    tags=['x11', 'xorg', 'distributed', 'multihead'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.4',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libdmx-1.1.4.tar.bz2',
                'sha256': '253f90005d134fa7a209fbcbc5a3024335367c930adf0f3203e754cf32747243',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
    ]
)
def build(build):
    return autotools.build()

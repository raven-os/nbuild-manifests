#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxkbfile',
    category='dev-libs',
    description='''
    A keyboard file manipulation library for X.
    ''',
    tags=['x11', 'xorg', 'keyboard', 'kb'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libxkbfile-1.1.0.tar.bz2',
                'sha256': '758dbdaa20add2db4902df0b1b7c936564b7376c02a0acd1f2a331bd334b38c7',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
    ]
)
def build(build):
    return autotools.build()

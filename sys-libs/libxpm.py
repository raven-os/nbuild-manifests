#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxpm',
    category='sys-libs',
    description='''
    A pixmap library for X.
    ''',
    tags=['x11', 'xorg', 'pixel', 'pixmap'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.5.12',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXpm-3.5.12.tar.bz2',
                'sha256': 'fd6a6de3da48de8d1bb738ab6be4ad67f7cb0986c39bd3f7d51dd24f7854bdec',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
    ]
)
def build(build):
    return autotools.build()

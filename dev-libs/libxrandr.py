#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxrandr',
    category='dev-libs',
    description='''
    A RandR extension library for X.
    ''',
    tags=['x11', 'xorg', 'randr'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.5.2',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXrandr-1.5.2.tar.bz2',
                'sha256': '8aea0ebe403d62330bb741ed595b53741acf45033d3bda1792f1d4cc3daee023',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxrender-dev',
    ]
)
def build(build):
    return autotools.build()

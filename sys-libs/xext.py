#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xext',
    category='sys-libs',
    description='''
    Miscellaneous extensions library.
    ''',
    tags=['x11', 'xorg', 'extensions'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.3.4',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXext-1.3.4.tar.bz2',
                'sha256': '59ad6fcce98deaecc14d39a672cf218ca37aba617c9a0f691cac3bcd28edf82b',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'dev-libs/xau-dev',
    ]
)
def build(build):
    return autotools.build()

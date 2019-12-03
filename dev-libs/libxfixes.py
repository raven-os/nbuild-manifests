#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxfixes',
    category='dev-libs',
    description='''
    A miscellaneous 'fixes' extension library for X.
    ''',
    tags=['x11', 'xorg', 'fixes', 'extension'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.0.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXfixes-5.0.3.tar.bz2',
                'sha256': 'de1cd33aff226e08cefd0e6759341c2c8e8c9faf8ce9ac6ec38d43e287b22ad6',
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

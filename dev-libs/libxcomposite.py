#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxcomposite',
    category='dev-libs',
    description='''
    A composite extension library for X.
    ''',
    tags=['x11', 'xorg', 'composite', 'extension'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.4.5',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXcomposite-0.4.5.tar.bz2',
                'sha256': 'b3218a2c15bab8035d16810df5b8251ffc7132ff3aa70651a1fba0bfe9634e8f',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libxfixes-dev',
        'sys-libs/x11-dev',
    ]
)
def build(build):
    return autotools.build()

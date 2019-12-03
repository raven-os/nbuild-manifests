#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxmu',
    category='dev-libs',
    description='''
    A miscellaneous micro-utility library for X.
    ''',
    tags=['x11', 'xorg', 'utility'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXmu-1.1.3.tar.bz2',
                'sha256': '9c343225e7c3dc0904f2122b562278da5fed639b1b5e880d25111561bac5b731',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxt-dev',
        'sys-libs/libsm-dev',
        'dev-libs/libice-dev',
    ]
)
def build(build):
    return autotools.build()

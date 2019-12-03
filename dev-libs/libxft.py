#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxft',
    category='dev-libs',
    description='''
    A FreeType-based font drawing library for X.
    ''',
    tags=['x11', 'xorg', 'font', 'freetype'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.3.3',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXft-2.3.3.tar.bz2',
                'sha256': '225c68e616dd29dbb27809e45e9eadf18e4d74c50be43020ef20015274529216',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libxrender-dev',
        'sys-libs/x11-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
    ]
)
def build(build):
    return autotools.build()

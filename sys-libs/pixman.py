#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='pixman',
    category='sys-libs',
    description='''
    A library to manipulate pixels at a low-level, such as image compositing and trapezoid rasterization.
    ''',
    tags=['pixel', 'graphic'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://cgit.freedesktop.org/pixman/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.38.4',
            'fetch': [{
                    'url': 'https://www.cairographics.org/releases/pixman-0.38.4.tar.gz',
                    'sha256': 'da66d6fd6e40aee70f7bd02e4f8f76fc3f006ec879d346bae6a723025cfbdde7',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-libs/libpng-dev',
        'sys-libs/zlib-dev',
    ]
)
def build(build):
    return meson_ninja.build()

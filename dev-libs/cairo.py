#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools
from stdlib.template.configure import configure


@manifest(
    name='cairo',
    category='dev-libs',
    description='''
    2D graphics library with support for multiple output devices.
    ''',
    tags=['text', 'shaping'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://www.cairographics.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.16.0',
            'fetch': [{
                'url': 'https://www.cairographics.org/releases/cairo-1.16.0.tar.xz',
                'sha256': '5e7b29b3f113ef870d1e3ecf8adf21f923396401604bda16d44be45e66052331',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'dev-libs/libpng-dev',
        'sys-libs/pixman-dev',
        'dev-libs/glib-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/xcb-dev',
        'dev-libs/harfbuzz-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure('--enable-tee'),
        check=lambda: None
    )

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='cairomm',
    category='dev-libs',
    description='''
    C++ bindings for Cairo.
    ''',
    tags=['cairo', 'cpp', 'bindings'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL, stdlib.license.License.CUSTOM],
    upstream_url='https://www.cairographics.org/cairomm/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.12.2',
            'fetch': [{
                'url': 'https://www.cairographics.org/releases/cairomm-1.12.2.tar.gz',
                'sha256': '45c47fd4d0aa77464a75cdca011143fea3ef795c4753f6e860057da5fb8bd599',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'sys-libs/x11-dev',
        'dev-libs/xorgproto-dev',
        'sys-libs/xext-dev',
        'dev-libs/libpng-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/cairo-dev',
        'dev-libs/libsigc++-dev',
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/cairomm-dev'].drain(
        'usr/lib64/cairomm-*/include/cairommconfig.h'
    )

    return packages

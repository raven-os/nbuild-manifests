#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import basic
from stdlib.template.cmake import cmake
from stdlib.template.ninja import ninja, ninja_install, ninja_test


@manifest(
    name='libtiff',
    category='dev-libs',
    description='''
    Library for manipulation of TIFF images
    ''',
    tags=['tiff', 'image', 'manipulation'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='http://www.libtiff.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.0.10',
            'fetch': [{
                'url': 'http://download.osgeo.org/libtiff/tiff-4.0.10.tar.gz',
                'sha256': '2c52d11ccaf767457db0c46795d9c7d1a8d8f76f68b0b800a3dfe45786b996e4',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'dev-apps/ninja',
        'dev-libs/freeglut-dev',
        'dev-libs/libjpeg-turbo-dev',
        'sys-libs/zlib-dev',
    ]
)
def build(build):
    return basic.build(
        build_folder='libtiff-build',
        configure=lambda: cmake(folder='..', generator='Ninja'),
        compile=ninja,
        install=ninja_install,
        check=ninja_test,
    )

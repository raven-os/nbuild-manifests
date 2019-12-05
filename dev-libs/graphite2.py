#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import basic
from stdlib.template.cmake import cmake
from stdlib.template.make import make


@manifest(
    name='graphite2',
    category='dev-libs',
    description='''
    Rendering engine for graphite fonts.
    ''',
    tags=['rendering', 'fonts', 'truetype'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM, stdlib.license.License.GPL, stdlib.license.License.LGPL],
    upstream_url='https://github.com/silnrsi/graphite',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.3.13',
            'fetch': [{
                'url': 'https://github.com/silnrsi/graphite/releases/download/1.3.13/graphite2-1.3.13.tgz',
                'sha256': 'dd63e169b0d3cf954b397c122551ab9343e0696fb2045e1b326db0202d875f06',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'dev-libs/freetype-dev'
    ]
)
def build(build):
    packages = basic.build(
        build_folder='build',
        configure=lambda: cmake(folder='..'),
        compile=make,
        install=lambda: make('install')
    )

    packages['dev-libs/graphite2-dev'].drain(
        'usr/local/{share,include}/',
        'usr/share/graphite2/*.cmake'
    )

    return packages

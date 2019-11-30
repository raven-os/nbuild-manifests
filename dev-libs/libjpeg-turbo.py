#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import basic
from stdlib.manifest import manifest
from stdlib.template.cmake import cmake
from stdlib.template.make import make
from stdlib.pushd import pushd


def configure_cmake():
    os.mkdir('build')
    with pushd('build'):
        cmake(folder='..')


@manifest(
    name='libjpeg-turbo',
    category='dev-libs',
    description='''
    The libjpeg-turbo package contains a library implementing JPEG image encoding, decoding and transcoding.
    ''',
    tags=['jpeg', 'dev'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.nasm.us/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.0.2',
            'fetch': [{
                'url': 'https://downloads.sourceforge.net/libjpeg-turbo/libjpeg-turbo-2.0.2.tar.gz',
                'sha256': 'acb8599fe5399af114287ee5907aea4456f8f2c1cc96d26c28aebfdf5ee82fed',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'dev-apps/nasm'
    ]
)
def build(build):
    return basic.build(
        configure=configure_cmake,
        compile=lambda: make(folder='build'),
        install=lambda: make('install', folder='build')
    )

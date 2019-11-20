#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.template.make import make
from stdlib.manifest import manifest


@manifest(
    name='cmake',
    category='dev-apps',
    description='''
    CMake is an open-source, cross-platform family of tools designed to build, test and package software.
    ''',
    tags=['build', 'compilation'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://cmake.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.15.5',
            'fetch': [{
                'url': 'https://cmake.org/files/v3.15/cmake-3.15.5.tar.gz',
                'sha256': 'fbdd7cef15c0ced06bb13024bfda0ecc0dedbcaaaa6b8a5d368c75255243beb4',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/expat-dev',
        'dev-libs/xml2-dev',
        'sys-libs/zlib-dev',
        'sys-apps/curl-dev',
        'dev-libs/archive-dev',
        'dev-libs/uv-dev',
    ]
)
def build(build):
    packages = basic.build(
        configure=lambda: stdlib.cmd(
            "./bootstrap --prefix=/usr          \
            --system-libs                       \
            --mandir=/share/man                 \
            --no-system-jsoncpp                 \
            --no-system-librhash                \
            --docdir=/share/doc/cmake-3.15.5"
        ),
        compile=make,
        install=lambda: make('install', f'DESTDIR={build.install_cache}'),
    )

    packages['dev-apps/cmake'].drain(
        'usr/share/cmake-3.15/'
    )

    return packages

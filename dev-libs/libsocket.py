#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.cmake import cmake
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libsocket',
    category='dev-libs',
    description='''
    The ultimate socket library for C and C++.
    ''',
    tags=['socket', 'c', 'cpp'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://dermesser.github.io/libsocket/doc/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.5.0',
            'fetch': [{
                    'url': 'https://github.com/dermesser/libsocket/archive/v2.5.0.tar.gz',
                    'sha256': '0afe2ece985caa0b44546d10426b15a506164d5b96d7242890c7d0337f479689',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
    ]
)
def build(build):
    packages = autotools.build(
        configure=cmake,
    )

    packages['dev-libs/libsocket'].drain_package(
        packages['dev-libs/libsocket-dev'],
        'usr/lib/*.so',
    )

    return packages

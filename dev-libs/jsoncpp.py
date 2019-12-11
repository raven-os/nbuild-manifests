#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='jsoncpp',
    category='dev-libs',
    description='''
    A C++ library for interacting with JSON.
    ''',
    tags=['json', 'cpp', 'parser'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.PUBLIC_DOMAIN, stdlib.license.License.MIT],
    upstream_url='https://github.com/open-source-parsers/jsoncpp',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.8.4',
            'fetch': [{
                'url': 'https://github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz',
                'sha256': 'c49deac9e0933bcb7044f08516861a2d560988540b23de2ac1ad443b219afdb6',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
    ],
)
def build(build):
    return meson_ninja.build(
        build_folder='build',
    )

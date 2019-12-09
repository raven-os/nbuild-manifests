#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='epoxy',
    category='dev-libs',
    description='''
    Library handling OpenGL function pointer management.
    ''',
    tags=['opengl', 'wrapper'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/anholt/libepoxy',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.5.3',
            'fetch': [{
                'url': 'https://github.com/anholt/libepoxy/releases/download/1.5.3/libepoxy-1.5.3.tar.xz',
                'sha256': '002958c5528321edd53440235d3c44e71b5b1e09b9177e8daf677450b6c4433d',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/mesa-dev',
        'sys-libs/x11-dev',
        'dev-apps/ninja',
    ]
)
def build(build):
    return meson_ninja.build(
        build_folder='build'
    )

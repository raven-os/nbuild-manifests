#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import basic
from stdlib.template.cmake import cmake
from stdlib.template.make import make


@manifest(
    name='freeglut',
    category='dev-libs',
    description='''
    Window-system-independent toolkit for writing OpenGL programs
    ''',
    tags=['opengl', 'windowing', 'toolkit'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='http://freeglut.sourceforge.net/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.0.0',
            'fetch': [{
                'url': 'https://downloads.sourceforge.net/freeglut/freeglut-3.0.0.tar.gz',
                'sha256': '2a43be8515b01ea82bcfa17d29ae0d40bd128342f0930cd1f375f1ff999f76a2',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'sys-libs/mesa-dev',
        'dev-libs/glu-dev',
        'sys-libs/x11-dev',
        'dev-libs/libxi-dev'
    ]
)
def build(build):
    return basic.build(
        build_folder='build',
        configure=lambda: cmake('-DFREEGLUT_BUILD_DEMOS=OFF', folder='..'),
        compile=make,
        install=lambda: make('install')
    )

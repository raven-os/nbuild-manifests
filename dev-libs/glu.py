#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools


@manifest(
    name='glu',
    category='dev-libs',
    description='''
    Mesa OpenGL Utility library.
    ''',
    tags=['mesa', 'opengl', 'utility'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://cgit.freedesktop.org/mesa/glu/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '9.0.1',
            'fetch': [{
                'url': 'ftp://ftp.freedesktop.org/pub/mesa/glu/glu-9.0.1.tar.xz',
                'sha256': 'fb5a4c2dd6ba6d1c21ab7c05129b0769544e1d68e1e3b0ffecb18e73c93055bc',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/mesa-dev'
    ]
)
def build(build):
    return autotools.build()

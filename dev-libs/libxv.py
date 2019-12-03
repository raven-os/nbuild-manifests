#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxv',
    category='dev-libs',
    description='''
    A video extension library for X.
    ''',
    tags=['x11', 'xorg', 'video'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.11',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXv-1.0.11.tar.bz2',
                'sha256': 'd26c13eac99ac4504c532e8e76a1c8e4bd526471eb8a0a4ff2a88db60cb0b088',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
    ]
)
def build(build):
    return autotools.build()

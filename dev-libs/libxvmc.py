#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxvmc',
    category='dev-libs',
    description='''
    A Video Motion Compensation extension library for X.
    ''',
    tags=['x11', 'xorg', 'video', 'motion', 'compensation', 'vmc'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.11',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXvMC-1.0.11.tar.bz2',
                'sha256': '4a2e34d444a683a7c010b01b23cefe2b8043a063ce4dc6a9b855836b5262622d',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
        'sys-libs/xext-dev',
        'dev-libs/libxv-dev',
    ]
)
def build(build):
    return autotools.build()

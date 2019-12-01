#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxxf86dga',
    category='dev-libs',
    description='''
    A Direct Graphics Access extension library for X.
    ''',
    tags=['x11', 'xorg', 'direct', 'graphics', 'access', 'dga'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.5',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXxf86dga-1.1.5.tar.bz2',
                'sha256': '2b98bc5f506c6140d4eddd3990842d30f5dae733b64f198a504f07461bdb7203',
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

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='x11',
    category='sys-libs',
    description='''
    The X11 client-side library.
    ''',
    tags=['x11', 'xorg', 'client'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.6.8',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libX11-1.6.8.tar.bz2',
                'sha256': 'b289a845c189e251e0e884cc0f9269bbe97c238df3741e854ec4c17c21e473d5',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorgproto-dev',
        'dev-libs/xcb-dev',
        'dev-libs/xtrans-dev',
    ]
)
def build(build):
    packages = autotools.build()

    packages['sys-libs/x11'].drain('usr/share/X11')
    packages['sys-libs/x11-dev'].requires('dev-libs/xorgproto-dev')

    return packages

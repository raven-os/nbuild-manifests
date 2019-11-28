#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.manifest import manifest


@manifest(
    name='wayland-protocols',
    category='dev-libs',
    description='''
    Additional Wayland protocols that add functionality outside of protocols already in the Wayland core.
    ''',
    tags=['wayland', 'protocols', 'graphics', 'compositor'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://swaywm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.18.0',
            'fetch': [{
                    'url': 'https://wayland.freedesktop.org/releases/wayland-protocols-1.18.tar.xz',
                    'sha256': '3d73b7e7661763dc09d7d9107678400101ecff2b5b1e531674abfa81e04874b3',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/wayland-dev',
    ]
)
def build(build):
    return autotools.build(
        split=drain_all_with_doc,
    )

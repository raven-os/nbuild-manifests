#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='dmenu-wl',
    category='sys-apps',
    description='''
    A dmenu implementation for wayland-compositors.
    ''',
    tags=['dmenu', 'menu', 'launcher', 'wayland', 'wlroots'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/nyyManni/dmenu-wayland',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.1.42',
            'fetch': [{
                    'git': 'https://github.com/nyyManni/dmenu-wayland.git',
                    'commit': '3d73262076eaba16446675f0dec557a81e6eaffa',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'dev-libs/cairo-dev',
        'dev-libs/pango-dev',
        'dev-libs/libxkbcommon-dev',
        'dev-libs/glib-dev',
        'sys-libs/x11-dev',
        'dev-libs/harfbuzz-dev',
    ]
)
def build(build):
    return meson_ninja.build()

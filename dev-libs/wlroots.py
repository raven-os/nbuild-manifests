#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='wlroots',
    category='dev-libs',
    description='''
    A modular Wayland compositor library.
    ''',
    tags=['wayland', 'compositor', 'sway', 'swaywm'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://swaywm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.8.1',
            'fetch': [{
                    # FIXME TODO: We require a specific commit because of Feathers. Ideally, we'd want to get rid of that.
                    'git': 'https://github.com/swaywm/wlroots.git',
                    'commit': '8681e4ab8a2d4c95abd34abf0e0eed3351d11bf0',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-apps/cmake',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'sys-apps/systemd-dev',
        'sys-libs/pixman-dev',
        'sys-libs/libcap-dev',
        'sys-libs/mesa-dev',
        'sys-libs/x11-dev',
        'dev-libs/libinput-dev',
        'dev-libs/xcb-dev',
        'dev-libs/libdrm-dev',
        'dev-libs/libpng-dev',
        'sys-libs/zlib-dev',
        'dev-libs/libxkbcommon-dev',
    ],
)
def build(build):
    return meson_ninja.build()

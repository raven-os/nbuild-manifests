#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='waybar',
    category='dev-libs',
    description='''
    Highly customizable Wayland bar for Sway and Wlroots based compositors.
    ''',
    tags=['wayland', 'wlroots', 'bar'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/Alexays/Waybar',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.8.0',
            'fetch': [{
                'url': 'https://github.com/Alexays/Waybar/archive/0.8.0.tar.gz',
                'sha256': '2de2f0cec243da0d9ff2255ceb9dac9d95e8be06d6ea13926fae460d72e4b8aa',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/mesa-dev',
        'dev-libs/libxtst-dev',
        'dev-resources/shared-mime-info',
        'dev-libs/libinput-dev',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'dev-libs/xorgproto-dev',
        'dev-libs/gtk3-dev',
        'dev-libs/gtkmm3-dev',
        'dev-libs/glib-dev',
        'dev-libs/glibmm-dev',
        'dev-libs/jsoncpp-dev',
        'dev-libs/libsigc++-dev',
        'dev-libs/pango-dev',
        'dev-libs/pangomm-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/cairo-dev',
        'dev-libs/cairomm-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/gdk-pixbuf-dev',
        'dev-libs/atk-dev',
        'dev-libs/atkmm-dev',
        'sys-apps/systemd-dev',
        'dev-apps/ninja',
    ]
)
def build(build):
    return meson_ninja.build(
        build_folder='build',
    )

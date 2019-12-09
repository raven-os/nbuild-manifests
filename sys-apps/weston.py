#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
import stdlib.split.system
from stdlib.template.meson import meson
from stdlib.template.ninja import ninja_test
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


def split_weston():
    packages = stdlib.split.system.system()

    packages['sys-apps/weston'].drain_package(
        packages['sys-apps/weston-dev'],
        'usr/lib64/**/*.so',
    )

    packages['sys-apps/weston'].drain(
        'usr/share/',
        'usr/lib64/weston-*',
    )

    return packages


@manifest(
    name='weston',
    category='sys-apps',
    description='''
    A reference compositor for Wayland.
    ''',
    tags=['weston', 'compositor', 'wlroots'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://wayland.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '7.0.91',
            'fetch': [{
                    'url': 'https://github.com/wayland-project/weston/archive/7.0.91.tar.gz',
                    'sha256': '802a799019711e7a6f8bdef380cbcc5c237f260b3ffc78075e769e9c1b0e0e2b',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-libs/libxkbcommon-dev',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'sys-libs/pixman-dev',
        'dev-libs/libinput-dev',
        'dev-libs/libdrm-dev',
        'dev-libs/cairo-dev',
        'sys-libs/x11-dev',
        'dev-libs/pango-dev',
        'dev-libs/libjpeg-turbo-dev',
        'dev-libs/libwebp-dev',
        'sys-libs/mesa-dev',
        'sys-libs/pam-dev',
        'dev-libs/libxcursor-dev',
        'dev-libs/lcms2-dev',
        'dev-libs/libpng-dev',
        'sys-apps/systemd-dev',
        'dev-libs/glib-dev',
        'dev-libs/harfbuzz-dev',
        'sys-apps/dbus-dev',
        'dev-libs/xcb-dev',
        'sys-libs/zlib-dev',
        'dev-libs/evdev-dev',
        'dev-libs/xml2-dev',
    ]
)
def build(build):
    return meson_ninja.build(
        configure=lambda: meson(
            '-Dbackend-drm-screencast-vaapi=false',
            '-Dbackend-rdp=false',
            '-Dcolor-management-colord=false',
            '-Dremoting=false',
            '-Dpipewire=false',
        ),
        check=lambda: ninja_test(fail_ok=True),
        split=split_weston,
    )

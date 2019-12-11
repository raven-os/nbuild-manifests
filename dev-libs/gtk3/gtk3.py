#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja, meson
from stdlib.split.system import system


def split_gtk():
    packages = system()

    packages['dev-libs/gtk3'].drain(
        'usr/share/applications/',
        'usr/share/glib-2.0/schemas/',
        'usr/share/icons/hicolor/',
        'usr/share/themes/',
        'usr/share/gettext/',
        'usr/share/gtk-3.0/',
        'usr/lib64/girepository-*/*.typelib',
    )

    packages['dev-libs/gtk3-dev'].drain(
        'usr/share/gir-1.0/*.gir'
    )

    packages['dev-libs/gtk3'].drain_package(
        packages['dev-libs/gtk3-dev'],
        'usr/lib64/gtk-3.0/3.0.0/{immodules,printbackends}/'
    )

    return packages


@manifest(
    name='gtk3',
    category='dev-libs',
    description='''
    GObject-based multi-platform GUI toolkit
    ''',
    tags=['graphical', 'interface', 'applications', 'gobject'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtk.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.24.10',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/gtk+/3.24/gtk+-3.24.10.tar.xz',
                'sha256': '35a8f107e2b90fda217f014c0c15cb20a6a66678f6fd7e36556d469372c01b03',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/atk-dev',
        'dev-libs/at-spi2-atk-dev',
        'dev-libs/epoxy-dev',
        'dev-libs/gdk-pixbuf-dev',
        'dev-libs/pango-dev',
        'ui-resources/hicolor-icon-theme',
        'dev-libs/gobject-introspection-dev',
        'dev-libs/gobject-introspection',
        'dev-libs/xorgproto-dev',
        'dev-libs/libxkbcommon-dev',
        'dev-libs/libxrandr-dev',
        'sys-libs/x11-dev',
        'dev-libs/libxi-dev',
        'dev-libs/libxfixes-dev',
        'dev-libs/libxcursor-dev',
        'dev-libs/libxdamage-dev',
        'dev-libs/libxcomposite-dev',
        'dev-libs/libxtst-dev',
        'dev-libs/libxrender-dev',
        'sys-libs/xext-dev',
        'dev-resources/shared-mime-info',
        'sys-apps/util-linux-dev',
        'dev-libs/libxinerama-dev',
        'dev-libs/glib-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/cairo-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/freetype-dev',
        'dev-libs/libpng-dev',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'dev-resources/iso-codes',
        'dev-libs/libxslt',
        'dev-libs/libdrm-dev',
        'sys-libs/pixman-dev',
        'sys-apps/dbus-dev',
        'dev-libs/at-spi2-core-dev',
        'sys-libs/mesa-dev',
        'dev-libs/fribidi-dev',
        'dev-apps/ninja',
    ]
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
        configure=lambda: meson.meson(
            '-Dcolord=no',
            '-Dgtk_doc=false',
            '-Dman=false',
            '-Dbroadway_backend=false'
        ),
        check=None,  # tests attempt to open an X window
        split=split_gtk,
    )

    packages['dev-libs/gtk3'].load_instructions('./instructions.sh')

    return packages

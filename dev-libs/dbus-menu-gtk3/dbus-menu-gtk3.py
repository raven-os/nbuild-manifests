#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure


@manifest(
    name='dbus-menu-gtk3',
    category='dev-libs',
    description='''
    Library to pass a menu structure across DBus.
    ''',
    tags=['dbus', 'menu'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3, stdlib.license.License.LGPL_V2_1, stdlib.license.License.LGPL_V3],
    upstream_url='https://launchpad.net/libdbusmenu',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '16.04.0',
            'fetch': [
                {
                    'url': 'https://launchpad.net/libdbusmenu/16.04/16.04.0/+download/libdbusmenu-16.04.0.tar.gz',
                    'sha256': 'b9cc4a2acd74509435892823607d966d424bd9ad5d0b00938f27240a1bfa878a',
                },
                {
                    'file': 'dbus-menu-gtk3-remove-werror.patch'
                }
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/libtool',
        'dev-perl/xml-parser',
        'dev-resources/shared-mime-info',
        'dev-libs/wayland-protocols',
        'dev-libs/glib-dev',
        'dev-libs/gtk3-dev',
        'dev-libs/gtk2-dev',
        'dev-libs/atk-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/libxrender-dev',
        'sys-libs/xext-dev',
        'sys-libs/mesa-dev',
        'dev-libs/libxtst-dev',
        'sys-libs/x11-dev',
        'dev-libs/json-glib-dev',
        'dev-libs/gobject-introspection',
        'dev-libs/gobject-introspection-dev',
        'dev-libs/pango-dev',
        'dev-libs/cairo-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/gdk-pixbuf-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-vala',
            make_configure=lambda: stdlib.cmd('autoreconf -vi'),
        )
    )

    packages['dev-libs/dbus-menu-gtk3'].drain(
        'usr/share/libdbusmenu/json/test-gtk-label.json',
        'usr/lib64/dbusmenu-dumper',
        'usr/lib64/dbusmenu-bench',
        'usr/lib64/dbusmenu-testapp',
        'usr/lib64/girepository-1.0',
    )

    packages['dev-libs/dbus-menu-gtk3-dev'].drain(
        'usr/share/gir-1.0/*.gir',
    )

    packages['dev-libs/dbus-menu-gtk3-doc'].drain(
        'usr/share/gtk-doc/'
    )

    return packages

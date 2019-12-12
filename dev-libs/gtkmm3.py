#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gtkmm3',
    category='dev-libs',
    description='''
    C++ bindings for GTK+ 3.
    ''',
    tags=['gtk3', 'cpp', 'bindings'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtkmm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.24.1',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/gtkmm/3.24/gtkmm-3.24.1.tar.xz',
                'sha256': 'ddfe42ed2458a20a34de252854bcf4b52d3f0c671c045f56b42aa27c7542d2fd',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/mesa-dev',
        'sys-libs/x11-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/libxtst-dev',
        'dev-libs/gtk3-dev',
        'dev-libs/gdk-pixbuf-dev',
        'dev-resources/shared-mime-info',
        'dev-libs/wayland-protocols',
        'dev-libs/harfbuzz-dev',
        'dev-libs/glib-dev',
        'dev-libs/glibmm-dev',
        'dev-libs/atk-dev',
        'dev-libs/atkmm-dev',
        'dev-libs/cairo-dev',
        'dev-libs/cairomm-dev',
        'dev-libs/pango-dev',
        'dev-libs/pangomm-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/libsigc++-dev',
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/gtkmm3-dev'].drain(
        'usr/lib64/gtkmm-*/{include,proc}',
        'usr/lib64/gdkmm-*/include'
    )

    return packages

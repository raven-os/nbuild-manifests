#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools
from stdlib.split.system import system


def split_gtk():
    packages = system()

    packages['dev-libs/gtk2'].drain_package(
        packages['dev-libs/gtk2-dev'],
        'usr/lib64/gtk-2.0/2.10.0/**/*.so'
    )

    packages['dev-libs/gtk2'].drain(
        'usr/share/themes/'
    )

    packages['dev-libs/gtk2-dev'].drain(
        'usr/share/gir-1.0/*.gir',
        'usr/lib64/gtk-2.0/include/'
    )

    return packages


@manifest(
    name='gtk2',
    category='dev-libs',
    description='''
    Libraries used for creating graphical user interfaces for applications.
    ''',
    tags=['graphical', 'interface', 'applications'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtk.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.24.32',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/gtk+/2.24/gtk+-2.24.32.tar.xz',
                'sha256': 'b6c8a93ddda5eabe3bfee1eb39636c9a03d2a56c7b62828b359bf197943c582e',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/atk-dev',
        'dev-libs/gdk-pixbuf-dev',
        'dev-libs/pango-dev',
        'ui-resources/hicolor-icon-theme',
        'dev-libs/gobject-introspection-dev',
        'dev-libs/gobject-introspection',
        'sys-libs/x11-dev',
        'dev-libs/libxrender-dev',
        'sys-libs/xext-dev',
        'dev-resources/shared-mime-info',
        'dev-libs/glib-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/cairo-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/freetype-dev',
        'dev-libs/libtiff-dev',
        'dev-libs/libpng-dev',
    ]
)
def build(build):
    packages = autotools.build(
        patch=lambda: stdlib.cmd("sed -e 's#l \\(gtk-.*\\).sgml#& -o \\1#' -i docs/{faq,tutorial}/Makefile.in"),
        check=None,  # tests attempt to open an X window
        split=split_gtk,
    )

    packages['dev-libs/gtk2'].load_instructions('./instructions.sh')

    return packages

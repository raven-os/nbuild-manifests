#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja
from stdlib.split.system import system


def split_gdk_pixbuf():
    packages = system()

    packages['dev-libs/gdk-pixbuf'].drain(
        'usr/lib64/girepository-*/*.typelib',
    )

    packages['dev-libs/gdk-pixbuf'].drain_package(
        packages['dev-libs/gdk-pixbuf-dev'],
        "usr/lib64/gdk-pixbuf-2.0/2.10.0/loaders/",
    )

    packages['dev-libs/gdk-pixbuf-dev'].drain(
        'usr/share/gir-1.0/*.gir'
    )

    return packages


@manifest(
    name='gdk-pixbuf',
    category='dev-libs',
    description='''
    Toolkit for image loading and pixel buffer manipulation
    ''',
    tags=['image', 'pixel', 'toolkit'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL_V2_1],
    upstream_url='https://wiki.gnome.org/Projects/GdkPixbuf',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.38.1',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/gdk-pixbuf/2.38/gdk-pixbuf-2.38.1.tar.xz',
                'sha256': 'f19ff836ba991031610dcc53774e8ca436160f7d981867c8c3a37acfe493ab3a',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-libs/glib-dev',
        'dev-libs/libjpeg-turbo-dev',
        'dev-libs/libpng-dev',
        'dev-libs/libtiff-dev',
        'sys-libs/x11-dev',
        'dev-resources/shared-mime-info',
        'dev-libs/gobject-introspection',
        'dev-libs/gobject-introspection-dev',
        'sys-libs/zlib-dev',
        'dev-resources/shared-mime-info'
    ]
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
        split=split_gdk_pixbuf,
    )

    packages['dev-libs/gdk-pixbuf'].load_instructions('./instructions.sh')

    return packages

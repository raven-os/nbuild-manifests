#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


def split_gobject_introspection():
    packages = stdlib.split.system.system()

    packages['dev-libs/gobject-introspection'].drain(
        'usr/lib64/girepository-*/*.typelib',
        'usr/lib64/gobject-introspection/giscanner/',
        'usr/share/gir-1.0/',
    )

    packages['dev-libs/gobject-introspection'].drain_package(
        packages['dev-libs/gobject-introspection-dev'],
        'usr/lib64/gobject-introspection/giscanner/*.so',
    )

    packages['dev-libs/gobject-introspection-dev'].drain(
        'usr/share/gobject-introspection-*/',
    )

    return packages


@manifest(
    name='gobject-introspection',
    category='dev-libs',
    description='''
    Machine readable introspection data of the API of C libraries.
    ''',
    tags=['gnome', 'introspection'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL],
    upstream_url='https://wiki.gnome.org/Projects/GObjectIntrospection',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.60.2',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/gobject-introspection/1.60/gobject-introspection-1.60.2.tar.xz',
                'sha256': 'ffdfe2368fb2e34a547898b01aac0520d52d8627fdeb1c306559bcb503ab5e9c',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/flex-dev',
        'dev-libs/glib-dev',
        'dev-apps/ninja',
        'sys-apps/util-linux-dev',
    ]
)
def build(build):
    return meson_ninja.build(
        build_folder='build',
        split=split_gobject_introspection,
    )

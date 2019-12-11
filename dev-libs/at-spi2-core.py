#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='at-spi2-core',
    category='dev-libs',
    description='''
    Protocol definitions and daemon for D-Bus at-spi.
    ''',
    tags=['at-spi', 'dbus', 'protocol'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://gitlab.gnome.org/GNOME/at-spi2-core',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.32.1',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/at-spi2-core/2.32/at-spi2-core-2.32.1.tar.xz',
                'sha256': '3c2aa937ebfaca2c86569bce9b16a34fbe20d69ef0c58846313b1c42f53b0d53',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/gobject-introspection-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/libxtst-dev',
        'dev-libs/libxfixes-dev',
        'dev-libs/libxi-dev',
        'dev-libs/glib-dev',
        'sys-apps/dbus-dev',
        'sys-libs/x11-dev',
        'dev-apps/ninja'
    ]
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
        check=None,
    )

    packages['dev-libs/at-spi2-core'].drain(
        'usr/share/{defaults,dbus-1}/',
        'usr/lib64/{at-spi-bus-launcher,at-spi2-registryd,girepository-*}',
        'usr/lib/systemd',
    )

    packages['dev-libs/at-spi2-core-dev'].drain(
        'usr/share/gir-1.0/*.gir'
    )

    return packages

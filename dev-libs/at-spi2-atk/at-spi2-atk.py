#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='at-spi2-atk',
    category='dev-libs',
    description='''
    A GTK+ module that bridges ATK to D-Bus at-spi.
    ''',
    tags=['gtk', 'atk', 'dbus', 'at-spi'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://wiki.gnome.org/Accessibility',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.32.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/at-spi2-atk/2.32/at-spi2-atk-2.32.0.tar.xz',
                'sha256': '0b51e6d339fa2bcca3a3e3159ccea574c67b107f1ac8b00047fa60e34ce7a45c',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/gobject-introspection-dev',
        'dev-libs/atk-dev',
        'dev-libs/at-spi2-core-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/libxtst-dev',
        'dev-libs/libxfixes-dev',
        'dev-libs/libxi-dev',
        'dev-libs/glib-dev',
        'sys-apps/dbus-dev',
        'sys-libs/x11-dev',
        'dev-libs/xml2-dev',
        'dev-apps/ninja'
    ]
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
        check=None,
    )

    packages['dev-libs/at-spi2-atk'].drain(
        'usr/lib64/gnome-settings-daemon-3.0/gtk-modules/'
    )

    packages['dev-libs/at-spi2-atk'].make_keepers(
        'usr/share/glib-2.0/schemas/'
    )

    packages['dev-libs/at-spi2-atk'].load_instructions('./instructions.sh')

    return packages

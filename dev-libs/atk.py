#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='atk',
    category='dev-libs',
    description='''
    Accessibility toolkit providing interface definitions for accessibility infrastructure.
    ''',
    tags=['accessibility', 'toolkit'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://gitlab.gnome.org/GNOME/atk',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.32.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/atk/2.32/atk-2.32.0.tar.xz',
                'sha256': 'cb41feda7fe4ef0daa024471438ea0219592baf7c291347e5a858bb64e4091cc',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/glib-dev',
        'dev-libs/gobject-introspection-dev',
        'dev-apps/ninja',
    ]
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
    )

    packages['dev-libs/atk'].drain(
        'usr/lib64/girepository-*/*.typelib',
    )

    packages['dev-libs/atk-dev'].drain(
        'usr/share/gir-1.0'
    )

    return packages

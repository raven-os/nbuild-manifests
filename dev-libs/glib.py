#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
from stdlib.template.ninja import ninja_test
from stdlib.manifest import manifest


@manifest(
    name='glib',
    category='dev-libs',
    description='''
    Low level core library.
    ''',
    tags=['core', 'data', 'structure' 'c', 'threads', 'objects'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.LGPL_V2_1],
    upstream_url='https://wiki.gnome.org/Projects/GLib',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.62.3',
            'fetch': [{
                    'url': 'http://ftp.gnome.org/pub/gnome/sources/glib/2.62/glib-2.62.3.tar.xz',
                    'sha256': '4400adc9f0d3ffcfe8e84225210370ce3f9853afb81812ddadb685325aa655c4',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'dev-libs/libxslt-dev',
        'dev-libs/pcre-dev',
        'sys-apps/util-linux-dev',
        'sys-apps/dbus-dev',
        'dev-apps/ninja',
    ],
)
def build(build):
    packages = meson_ninja.build(
        check=lambda: ninja_test(fail_ok=True),
    )

    packages['dev-libs/glib-dev'].drain(
        'usr/share/',
        'usr/lib64/glib-*/include/',
    )

    packages['dev-libs/glib-doc'].drain_build_cache('docs/reference/{NEWS,gio,glib,gobject}', 'usr/share/doc/glib/')

    return packages

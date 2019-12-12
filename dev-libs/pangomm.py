#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='pangomm',
    category='dev-libs',
    description='''
    C++ bindings for Pango.
    ''',
    tags=['pango', 'cpp', 'bindings'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtkmm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.42.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/pangomm/2.42/pangomm-2.42.0.tar.xz',
                'sha256': 'ca6da067ff93a6445780c0b4b226eb84f484ab104b8391fb744a45cbc7edbf56',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/cairo-dev',
        'dev-libs/cairomm-dev',
        'dev-libs/glibmm-dev',
        'dev-libs/xorgproto-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/freetype-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/glib-dev',
        'dev-libs/libsigc++-dev',
        'dev-libs/pango-dev',
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/pangomm-dev'].drain(
        'usr/lib64/pangomm-*/{include,proc}'
    )

    return packages

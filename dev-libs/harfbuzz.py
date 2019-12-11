#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools
from stdlib.template.configure import configure


@manifest(
    name='harfbuzz',
    category='dev-libs',
    description='''
    OpenType text shaping engine.
    ''',
    tags=['text', 'shaping'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://www.freedesktop.org/wiki/Software/HarfBuzz',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.6.0',
            'fetch': [{
                'url': 'https://www.freedesktop.org/software/harfbuzz/release/harfbuzz-2.6.0.tar.xz',
                'sha256': '9cf7d117548265f95ca884e2f4c9fafaf4e17d45a67b11107147b79eed76c966',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/glib-dev',
        'dev-libs/freetype-dev',
        'dev-libs/icu-dev',
        'dev-libs/graphite2-dev',
        'dev-libs/gobject-introspection-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure('--with-gobject --with-graphite2')
    )

    packages['dev-libs/harfbuzz'].drain(
        'usr/lib64/girepository-*/*.typelib',
    )

    packages['dev-libs/harfbuzz-dev'].drain(
        'usr/lib64/cmake/harfbuzz/*.cmake',
        'usr/share/gir-1.0/*.gir'
    )

    return packages

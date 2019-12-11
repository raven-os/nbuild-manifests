#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.ninja import ninja_test
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='pango',
    category='dev-libs',
    description='''
    A library for layout and rendering of text.
    ''',
    tags=['x11', 'xorg', 'gtk', 'text', 'rendering', 'font'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.pango.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.44.7',
            'fetch': [{
                    'url': 'http://ftp.gnome.org/pub/gnome/sources/pango/1.44/pango-1.44.7.tar.xz',
                    'sha256': '66a5b6cc13db73efed67b8e933584509f8ddb7b10a8a40c3850ca4a985ea1b1f',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-libs/cairo-dev',
        'dev-libs/fontconfig-dev',
        'dev-libs/fribidi-dev',
        'dev-libs/glib-dev',
        'dev-libs/gobject-introspection-dev',
        'dev-libs/harfbuzz-dev',
        'dev-libs/freetype-dev',
        'dev-libs/libxft-dev',
        'dev-libs/libpng-dev',
        'sys-apps/util-linux-dev',
        'sys-libs/x11-dev',
        'dev-libs/libxrender-dev',
        'sys-libs/pixman-dev',
    ],
)
def build(build):
    packages = meson_ninja.build(
        check=lambda: ninja_test(fail_ok=True),
    )

    packages['dev-libs/pango-dev'].drain(
        'usr/share/**/*.gir',
    )

    return packages

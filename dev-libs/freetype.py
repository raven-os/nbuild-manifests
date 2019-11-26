#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.pushd import pushd
from stdlib.extract import flat_extract
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


def extract_freetype():
    flat_extract('freetype-2.10.1.tar.xz')
    with pushd('docs/'):
        flat_extract('../freetype-doc-2.10.1.tar.xz')


def patch_freetype():
    stdlib.cmd('sed -ri "s:.*(AUX_MODULES.*valid):\\1:" modules.cfg')
    stdlib.cmd('sed -r "s:.*(#.*SUBPIXEL_RENDERING) .*:\\1:" -i include/freetype/config/ftoption.h')


@manifest(
    name='freetype',
    category='dev-libs',
    description='''
    FreeType2 is a library which allows applications to properly render TrueType fonts.
    ''',
    tags=['fonts', 'render', 'truetype'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.freetype.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.10.1',
            'fetch': [
                {
                    'url': 'https://downloads.sourceforge.net/freetype/freetype-2.10.1.tar.xz',
                    'sha256': '16dbfa488a21fe827dc27eaf708f42f7aa3bb997d745d31a19781628c36ba26f',
                },
                {
                    'url': 'https://downloads.sourceforge.net/freetype/freetype-doc-2.10.1.tar.xz',
                    'sha256': '2fc160eda64cb6ee9f357c3fd6ef5f1f2b6039f10da650c726b0db49f863341f',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'dev-libs/libpng-dev'
    ]
)
def build(build):
    packages = autotools.build(
        extract=extract_freetype,
        patch=patch_freetype,
        configure=lambda: configure(
            '--enable-freetype-config'
        ),
    )

    packages['dev-libs/freetype-doc'].drain_build_cache(
        'docs/*',
        'usr/share/doc/freetype-2.10.1/'
    )

    return packages

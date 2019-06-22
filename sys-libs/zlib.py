#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='zlib',
    category='sys-libs',
    description='''
    A compression and decompression library.
    ''',
    tags=['gnu', 'compression', 'decompression', 'gzip'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://zlib.net/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.11',
            'fetch': [{
                    'url': 'https://zlib.net/fossils/zlib-1.2.11.tar.gz',
                    'sha256': 'c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: stdlib.cmd('''
            ./configure \
                --prefix="/usr" \
                --includedir="/usr/include" \
        '''),
    )

    # Packages member of `raven-os/essentials` should explicitely state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/zlib'].rdepends_on('raven-os/corefs', '*')

    return packages

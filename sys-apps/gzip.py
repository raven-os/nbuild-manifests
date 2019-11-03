#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gzip',
    category='sys-apps',
    description='''
    A set of tools for compressing and decompressing files.
    ''',
    tags=['gnu', 'compression', 'decompression'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/gzip/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.10.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/gzip/gzip-1.10.tar.xz',
                    'sha256': '8425ccac99872d544d4310305f915f5ea81e04d0f437ef1a230dc9d1c819d7c0',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/gzip'].requires('raven-os/corefs')

    return packages

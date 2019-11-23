#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='lzip',
    category='sys-apps',
    description='''
    Lzip is a lossless data compressor with a user interface similar to the one of gzip or bzip2.
    ''',
    tags=['compression', 'decompression'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.nongnu.org/lzip/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.21.0',
            'fetch': [
                {
                    'url': 'http://download.savannah.gnu.org/releases/lzip/lzip-1.21.tar.gz',
                    'sha256': 'e48b5039d3164d670791f9c5dbaa832bf2df080cb1fbb4f33aa7b3300b670d8b',
                }
            ],
        },
    ]
)
def build(build):
    return autotools.build()

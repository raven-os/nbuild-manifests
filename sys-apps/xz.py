#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xz',
    category='sys-apps',
    description='''
    A bunch of programs to compress and decompress files.
    ''',
    tags=['xz', 'compression', 'decompression'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.CUSTOM, stdlib.license.License.LGPL],
    upstream_url='https://tukaani.org/xz/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.2.4',
            'fetch': [{
                    'url': 'https://tukaani.org/xz/xz-5.2.4.tar.xz',
                    'sha256': '9717ae363760dedf573dad241420c5fea86256b65bc21d2cf71b2b12f0544f4b',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/xz'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='file',
    category='sys-apps',
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
            'semver': '5.36.0',
            'fetch': [{
                    'url': 'ftp://ftp.astron.com/pub/file/file-5.36.tar.gz',
                    'sha256': 'fb608290c0fd2405a8f63e5717abf6d03e22e183fb21884413d1edd918184379',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitely state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/file'].rdepends_on('raven-os/corefs', '*')

    return packages

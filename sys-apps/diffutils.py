#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='diffutils',
    category='sys-apps',
    description='''
    A bunch of programs to show the differences between files or directories.
    ''',
    tags=['gnu', 'diff', 'compare'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/diffutils',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.7.0',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/diffutils/diffutils-3.7.tar.xz',
                    'sha256': 'b3a7a6221c3dc916085f0d205abf6b8e1ba443d4dd965118da364a1dc1cb3a26',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/diffutils'].requires('raven-os/corefs')

    return packages

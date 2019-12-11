#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libsigc++',
    category='dev-libs',
    description='''
    A typesafe callback system for standard C++.
    ''',
    tags=['callback', 'cpp'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='http://libsigc.sourceforge.net/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.10.2',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/libsigc++/2.10/libsigc++-2.10.2.tar.xz',
                'sha256': 'b1ca0253379596f9c19f070c83d362b12dfd39c0a3ea1dd813e8e21c1a097a98',
            }],
        },
    ],
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/libsigc++-dev'].drain(
        'usr/lib64/sigc++-2.0/include/sigc++config.h'
    )

    return packages

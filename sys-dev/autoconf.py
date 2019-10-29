#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='autoconf',
    category='sys-dev',
    description='''
    A tool for automatically configuring source code.
    ''',
    tags=['gnu', 'generator', 'configuration', 'configure', 'makefile', 'make'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2, stdlib.license.License.CUSTOM, stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/autoconf/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.69.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz',
                    'sha256': '64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Drain some shared files
    packages['sys-dev/autoconf'].drain('usr/share/autoconf/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-dev/autoconf'].rdepends_on('raven-os/corefs', '*')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='automake',
    category='dev-apps',
    description='''
    A tool for automatically generating Makefiles to use with dev-apps/autoconf.
    ''',
    tags=['gnu', 'generator', 'configuration', 'configure', 'autoconf', 'makefile', 'make'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.gnu.org/software/automake/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.16.1',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/automake/automake-1.16.1.tar.xz',
                    'sha256': '5d05bb38a23fd3312b10aea93840feec685bdf4a41146e78882848165d3ae921',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Drain shared files
    packages['dev-apps/automake'].drain('usr/share/*')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/automake'].requires('raven-os/corefs')

    return packages

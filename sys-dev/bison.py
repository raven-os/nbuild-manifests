#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='bison',
    category='sys-dev',
    description='''
    A general-purpose parser generator.
    ''',
    tags=['gnu', 'parser', 'generator'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/bison/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.4.1',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/bison/bison-3.4.1.tar.xz',
                    'sha256': '27159ac5ebf736dffd5636fd2cd625767c9e437de65baa63cb0de83570bd820d',
                },
            ],
        },
    ],
)
def build(build):

    # There's a race condition in the Makefile of Bison which prevents paralelle compilation
    os.environ['MAKEFLAGS'] += ' -j1'

    packages = autotools.build()

    packages['sys-dev/bison'].drain(
        'usr/share/bison/',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-dev/bison'].rdepends_on('raven-os/corefs', '*')

    return packages

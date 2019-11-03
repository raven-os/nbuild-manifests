#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='grep',
    category='sys-apps',
    description='''
    A tool to search one or more input files for lines containing a match to a specified pattern.
    ''',
    tags=['gnu', 'lexer', 'generator'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/grep/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.3.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/grep/grep-3.3.tar.xz',
                    'sha256': 'b960541c499619efd6afe1fa795402e4733c8e11ebf9fafccc0bb4bccdc5b514',
                },
            ],
        },
    ],
)
def build(build):

    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/grep'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='groff',
    category='sys-apps',
    description='''
    A typesetting system that reads plain text mixed with formatting commands and produces formatted output.
    ''',
    tags=['gnu', 'formatting'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='http://www.gnu.org/software/groff/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.22.4',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/groff/groff-1.22.4.tar.gz',
                    'sha256': 'e78e7b4cb7dec310849004fa88847c44701e8d133b5d4c13057d876c1bad0293',
                },
            ],
        },
    ],
)
def build(build):

    # Set the default page size to A4.
    # Hopefully, the installer will set that to a more context-aware default value.
    os.environ['PAGE'] = 'A4'

    # This package doesn't support parallel compilation
    os.environ['MAKEFLAGS'] += ' -j1'

    packages = autotools.build(
        check=None,  # The package doesn't come with a test suite.
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/groff'].requires('raven-os/corefs')

    return packages

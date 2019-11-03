#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='patch',
    category='dev-apps',
    description='''
    A utility to apply patch files to original source code.
    ''',
    tags=['gnu', 'patch', 'diff'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://savannah.gnu.org/projects/patch/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.7.6',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/patch/patch-2.7.6.tar.xz',
                    'sha256': 'ac610bda97abe0d9f6b7c963255a11dcb196c25e337c61f94e4778d632f1d8fd',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/patch'].requires('raven-os/corefs')

    return packages

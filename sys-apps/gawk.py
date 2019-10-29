#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gawk',
    category='sys-apps',
    description='''
    A bunch of programs to manipulate text files.
    ''',
    tags=['gnu', 'text', 'awk'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='http://www.gnu.org/software/gawk/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.0.1',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/gawk/gawk-5.0.1.tar.xz',
                    'sha256': '8e4e86f04ed789648b66f757329743a0d6dfb5294c3b91b756a474f1ce05a794',
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
    packages['sys-apps/gawk'].rdepends_on('raven-os/corefs', '*')

    return packages

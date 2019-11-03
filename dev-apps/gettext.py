#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gettext',
    category='dev-apps',
    description='''
    GNU internationalization library and utilities.
    ''',
    tags=['gnu', 'internationalization', 'language', 'locale'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.gnu.org/software/gettext/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.20.1',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/pub/gnu/gettext/gettext-0.20.1.tar.gz',
                    'sha256': '66415634c6e8c3fa8b71362879ec7575e27da43da562c798a8a2f223e6e47f5c',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        split=drain_all_with_doc,
    )

    # Make it executable
    with stdlib.pushd(packages['dev-apps/gettext'].wrap_cache):
        os.chmod('usr/lib64/preloadable_libintl.so', 0o0755)

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/gettext'].requires('raven-os/corefs')

    return packages

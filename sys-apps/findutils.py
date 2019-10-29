#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='findutils',
    category='sys-apps',
    description='''
    Utilities to locate files.
    ''',
    tags=['gnu', 'find', 'files'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.gnu.org/software/findutils/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.7.0',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/findutils/findutils-4.7.0.tar.xz',
                    'sha256': 'c5fefbdf9858f7e4feb86f036e1247a54c79fc2d8e4b7064d5aaa1f47dfa789a',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--localstatedir=/var/lib/locate',
        ),
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/findutils'].rdepends_on('raven-os/corefs', '*')

    return packages

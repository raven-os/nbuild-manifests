#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='man-db',
    category='sys-apps',
    description='''
    A utility for reading man pages.
    ''',
    tags=['man', 'page', 'reader'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL],
    upstream_url='https://www.nongnu.org/man-db/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.8.7',
            'fetch': [{
                    'url': 'http://download.savannah.gnu.org/releases/man-db/man-db-2.8.7.tar.xz',
                    'sha256': 'b9cd5bb996305d08bfe9e1114edc30b4c97be807093b88af8033ed1cf9beb326',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-setuid',
            '--enable-cache-owner=bin',
            '--with-browser=/usr/bin/lynx',
            '--with-vgrind=/usr/bin/vgrind',
            '--with-grap=/usr/bin/grap',
        ),
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/man-db'].requires('raven-os/corefs')

    return packages

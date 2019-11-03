#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='curl',
    category='sys-apps',
    description='''
    A command line tool and library for transferring data with URLs.
    ''',
    tags=['url', 'web', 'download'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://curl.haxx.se/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '7.66.0',
            'fetch': [{
                    'url': 'https://curl.haxx.se/download/curl-7.66.0.tar.xz',
                    'sha256': 'dbb48088193016d079b97c5c3efde8efa56ada2ebf336e8a97d04eb8e2ed98c1',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--enable-threaded-resolver',
            '--with-ca-path=/etc/ssl/certs',
        ),
        check=None,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/curl'].requires('raven-os/corefs')

    return packages

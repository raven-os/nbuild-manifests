#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='psmisc',
    category='sys-apps',
    description='''
    A bunch of tools to display information about running processes.
    ''',
    tags=['gnu', 'tool', 'process'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='http://psmisc.sourceforge.net/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '23.2.0',
            'fetch': [{
                    'url': 'https://netix.dl.sourceforge.net/project/psmisc/psmisc/psmisc-23.2.tar.xz',
                    'sha256': '4b7cbffdc9373474da49b85dc3457ae511c43dc7fa7d94513fe06f89dcb87880',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/psmisc'].rdepends_on('raven-os/corefs', '*')

    return packages

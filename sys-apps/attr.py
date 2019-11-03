#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='attr',
    category='sys-apps',
    description='''
    A collection of utilities to administer the extended attributes on filesystem objects.
    ''',
    tags=['gnu', 'attributes', 'filesystem', 'security'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://savannah.nongnu.org/projects/attr',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.4.48',
            'fetch': [{
                    'url': 'https://download.savannah.nongnu.org/releases/attr/attr-2.4.48.tar.gz',
                    'sha256': '5ead72b358ec709ed00bbf7a9eaef1654baad937c001c044fe8b74c57f5324e7',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/attr'].requires('raven-os/corefs')

    return packages

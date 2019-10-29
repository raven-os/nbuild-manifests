#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='acl',
    category='sys-apps',
    description='''
    A collection of utilities to administer Access Control Lists.
    ''',
    tags=['gnu', 'acl', 'access', 'security'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://savannah.nongnu.org/projects/acl/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.2.53',
            'fetch': [{
                    'url': 'https://download.savannah.nongnu.org/releases/acl/acl-2.2.53.tar.gz',
                    'sha256': '06be9865c6f418d851ff4494e12406568353b891ffe1f596b34693c387af26c7',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/acl'].rdepends_on('raven-os/corefs', '*')

    return packages

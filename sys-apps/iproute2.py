#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='iproute2',
    category='sys-apps',
    description='''
    An IP routing utility.
    ''',
    tags=['linux', 'kernel', 'internet', 'ip', 'route', 'routing'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://git.kernel.org/pub/scm/network/iproute2/iproute2.git',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.2.0',
            'fetch': [{
                    'url': 'https://www.kernel.org/pub/linux/utils/net/iproute2/iproute2-5.2.0.tar.xz',
                    'sha256': 'a5b95dec26353fc71dba9bb403e9343fad2a06bd69fb154a22a2aa2914f74da8',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=None,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/iproute2'].rdepends_on('raven-os/corefs', '*')

    return packages

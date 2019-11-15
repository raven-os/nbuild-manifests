#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='less',
    category='sys-apps',
    description='''
    A terminal-based text file viewer.
    ''',
    tags=['gnu', 'text', 'viewer'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.greenwoodsoftware.com/less/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '551.0.0',
            'fetch': [{
                    'url': 'http://www.greenwoodsoftware.com/less/less-551.tar.gz',
                    'sha256': 'e8544662b3373bf1467489f2338f65c419f6c3b996cb29befc0c424bacd56751',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/less'].requires('raven-os/corefs')

    return packages

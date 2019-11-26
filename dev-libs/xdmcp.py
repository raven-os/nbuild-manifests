#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xdmcp',
    category='dev-libs',
    description='''
    The libXdmcp package contains a library implementing the X Display Manager Control Protocol.
    ''',
    tags=['dev', 'protocol', 'xorg', 'x11', 'display'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.3',
            'fetch': [{
                'url': 'https://www.x.org/pub/individual/lib/libXdmcp-1.1.3.tar.bz2',
                'sha256': '20523b44aaa513e17c009e873ad7bbc301507a3224c232610ce2e099011c6529',
            }],
        },
    ]
)
def build(build):
    return autotools.build()

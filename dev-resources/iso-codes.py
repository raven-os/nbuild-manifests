#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='iso-codes',
    category='dev-resources',
    description='''
    Lists of the country, language, and currency names.
    ''',
    tags=['country', 'language', 'currency'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://salsa.debian.org/iso-codes-team/iso-codes',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.3.0',
            'fetch': [{
                'url': 'http://anduin.linuxfromscratch.org/BLFS/iso-codes/iso-codes-4.3.tar.xz',
                'sha256': 'aeca92e64e0c51d76989b6219a2604f42c0d8b9c02734a1177a56e9580c9e907',
            }],
        },
    ]
)
def build(build):
    return autotools.build(
        split=drain_all
    )

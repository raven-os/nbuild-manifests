#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='mtdev',
    category='dev-libs',
    description='''
    A Multitouch Protocol Translation Library which transforms all variants of kernel MT events to the slotted type B protocol
    ''',
    tags=['input', 'multitouch', 'protocol', 'translater', 'mt'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT, stdlib.license.License.CUSTOM],
    upstream_url='https://bitmath.org/code/mtdev/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.5',
            'fetch': [{
                    'url': 'https://bitmath.org/code/mtdev/mtdev-1.1.5.tar.gz',
                    'sha256': 'a662924dd09cf538c8df66514da345e40c3cbfa880cc7262bc3b55ee46d0c1f4',
                },
            ],
        },
    ],
)
def build(build):
    return autotools.build()

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='nasm',
    category='dev-apps',
    description='''
    The NASM (Netwide Assembler) package contains an 80x86 assembler designed for portability and modularity.
    ''',
    tags=['assembler', 'asm', 'dev'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://www.nasm.us/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.14.2',
            'fetch': [{
                'url': 'http://www.nasm.us/pub/nasm/releasebuilds/2.14.02/nasm-2.14.02.tar.xz',
                'sha256': 'e24ade3e928f7253aa8c14aa44726d1edf3f98643f87c9d72ec1df44b26be8f5',
            }],
        },
    ]
)
def build(build):
    return autotools.build()

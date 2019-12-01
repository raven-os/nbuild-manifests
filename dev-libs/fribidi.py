#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import meson_ninja


@manifest(
    name='fribidi',
    category='dev-libs',
    description='''
    Implementation of the Unicode Bidirectional Algorithm (BIDI).
    ''',
    tags=['unicode', 'alphabets'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://github.com/fribidi/fribidi/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.5',
            'fetch': [{
                'url': 'https://github.com/fribidi/fribidi/releases/download/v1.0.5/fribidi-1.0.5.tar.bz2',
                'sha256': '6a64f2a687f5c4f203a46fa659f43dd43d1f8b845df8d723107e8a7e6158e4ce',
            }],
        },
    ]
)
def build(build):
    return meson_ninja.build(
        build_folder='build',
    )

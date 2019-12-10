#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libwebp',
    category='dev-libs',
    description='''
    A library and support programs to encode and decode images in WebP format
    ''',
    tags=['webp', 'image'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://developers.google.com/speed/webp/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.3',
            'fetch': [{
                'url': 'http://downloads.webmproject.org/releases/webp/libwebp-1.0.3.tar.gz',
                'sha256': 'e20a07865c8697bba00aebccc6f54912d6bc333bb4d604e6b07491c1a226b34f',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libpng-dev',
        'dev-libs/libjpeg-turbo-dev',
        'dev-libs/libtiff-dev',
        'dev-libs/freeglut-dev',
    ]
)
def build(build):
    return autotools.build(
        configure=lambda: configure(
            '--enable-libwebpmux',
            '--enable-libwebpdemux',
            '--enable-libwebpdecoder',
            '--enable-libwebpextras',
            '--enable-swap-16bit-csp',
        )
    )

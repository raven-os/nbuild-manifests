#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='archive',
    category='dev-libs',
    description='''
    Multi-format archive and compression library
    ''',
    tags=['archive', 'compression'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://www.libarchive.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.4.0',
            'fetch': [{
                'url': 'https://github.com/libarchive/libarchive/releases/download/v3.4.0/libarchive-3.4.0.tar.gz',
                'sha256': '8643d50ed40c759f5412a3af4e353cffbce4fdf3b5cf321cb72cacf06b2d825e',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xml2-dev',
        'sys-libs/zlib-dev'
    ]
)
def build(build):
    return autotools.build(
        configure=lambda: configure(
            '--without-nettle'
        )
    )

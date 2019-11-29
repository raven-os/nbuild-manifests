#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='shared-mime-info',
    category='dev-resources',
    description='''
    The shared-mime-info package contains a MIME database.
    ''',
    tags=['mime', 'database'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://freedesktop.org/wiki/Software/shared-mime-info/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.12.0',
            'fetch': [{
                'url': 'https://gitlab.freedesktop.org/xdg/shared-mime-info/uploads/80c7f1afbcad2769f38aeb9ba6317a51/shared-mime-info-1.12.tar.xz',
                'sha256': '18b2f0fe07ed0d6f81951a5fd5ece44de9c8aeb4dc5bb20d4f595f6cc6bd403e',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/glib-dev',
        'dev-libs/xml2-dev',
        'dev-perl/xml-parser'
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-resources/shared-mime-info'].drain(
        'usr/share/{mime,pkgconfig}'
    )

    return packages

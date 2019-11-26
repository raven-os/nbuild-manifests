#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.package import Package, PackageID
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xcb-proto',
    category='dev-libs',
    description='''
    The xcb-proto package provides the XML-XCB protocol used by xcb.
    ''',
    tags=['dev', 'protocol', 'xorg', 'x11', 'xcb', 'xml'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xcb.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.13.0',
            'fetch': [{
                'url': 'https://xcb.freedesktop.org/dist/xcb-proto-1.13.tar.bz2',
                'sha256': '7b98721e669be80284e9bbfeab02d2d0d54cd11172b72271e47a2fe875e2bde1',
            }],
        },
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/xcb-proto'].drain(
        'usr/share/xcb'
    )

    packages['dev-python/xcbgen'] = Package(PackageID('xcbgen', 'dev-python'))

    packages['dev-python/xcbgen'].drain(
        'usr/lib/python3*/site-packages/xcbgen/*.py'
    )

    return packages

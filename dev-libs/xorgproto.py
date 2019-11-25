#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.package import Package, PackageID
from stdlib.split.drain_all import drain_all_with_doc_into
from stdlib.manifest import manifest


@manifest(
    name='xorgproto',
    category='dev-libs',
    description='''
    The xorgproto package contains header files for the X.Org X11 protocol.
    ''',
    tags=['dev', 'protocol', 'xorg', 'x11'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2019.2.0',
            'fetch': [{
                'url': 'https://xorg.freedesktop.org/archive/individual/proto/xorgproto-2019.2.tar.bz2',
                'sha256': '46ecd0156c561d41e8aa87ce79340910cdf38373b759e737fcbba5df508e7b8e',
            }],
        },
    ]
)
def build(build):
    packages = autotools.build(
        split=lambda: drain_all_with_doc_into(
            Package(PackageID('xorgproto-dev')),
            Package(PackageID('xorgproto-doc')),
        )
    )

    packages['dev-libs/xorgproto-dev'].drain(
        'usr/share/pkgconfig'
    )

    return packages

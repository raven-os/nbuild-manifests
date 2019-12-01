#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import meson_ninja
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
            'semver': '2019.1.0',
            'fetch': [{
                'url': 'https://xorg.freedesktop.org/archive/individual/proto/xorgproto-2019.1.tar.bz2',
                'sha256': 'a6daaa7a6cbc8e374032d83ff7f47d41be98f1e0f4475d66a4da3aa766a0d49b',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xorg-util-macros-dev',
        'dev-apps/ninja',
    ]
)
def build(build):
    packages = meson_ninja.build(
        split=lambda: drain_all_with_doc_into(
            Package(PackageID('xorgproto-dev')),
            Package(PackageID('xorgproto-doc')),
        )
    )

    packages['dev-libs/xorgproto-dev'].drain(
        'usr/share/pkgconfig'
    )

    return packages

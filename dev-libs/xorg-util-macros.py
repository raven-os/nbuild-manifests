#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.package import Package, PackageID
from stdlib.split.drain_all import drain_all_into
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xorg-util-macros',
    category='dev-libs',
    description='''
    The util-macros package contains the m4 macros used by all of the Xorg packages.
    ''',
    tags=['dev', 'macros', 'm4', 'xorg'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.19.2',
            'fetch': [{
                'url': 'https://www.x.org/pub/individual/util/util-macros-1.19.2.tar.bz2',
                'sha256': 'd7e43376ad220411499a79735020f9d145fdc159284867e99467e0d771f3e712',
            }],
        },
    ]
)
def build(build):
    return autotools.build(
        split=lambda: drain_all_into(Package(PackageID('xorg-util-macros-dev')))
    )

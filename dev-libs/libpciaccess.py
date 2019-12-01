#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libpciaccess',
    category='dev-libs',
    description='''
    A PCI access library for X.
    ''',
    tags=['x11', 'xorg', 'pci'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.16.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libpciaccess-0.16.tar.bz2',
                'sha256': '214c9d0d884fdd7375ec8da8dcb91a8d3169f263294c9a90c575bf1938b9f489',
            }],
        },
    ],
)
def build(build):
    return autotools.build()

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.package import Package, PackageID
from stdlib.split.drain_all import drain_all_with_doc_into
from stdlib.manifest import manifest


@manifest(
    name='xtrans',
    category='dev-libs',
    description='''
    X transport library.
    ''',
    tags=['x11', 'xorg', 'transport'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.4.0',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/xtrans-1.4.0.tar.bz2',
                'sha256': '377c4491593c417946efcd2c7600d1e62639f7a8bbca391887e2c4679807d773',
            }],
        },
    ],
)
def build(build):
    return autotools.build(
        split=lambda: drain_all_with_doc_into(
            Package(PackageID('xtrans-dev')),
            Package(PackageID('xtrans-doc')),
        )
    )

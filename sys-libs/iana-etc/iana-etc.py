#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib.fetch
from stdlib.package import Package, PackageID
from stdlib.manifest import manifest


@manifest(
    name='iana-etc',
    category='sys-libs',
    description='''
    A set of configuration files provided by IANA.
    ''',
    tags=['iana', 'network', 'database'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.iana.org/protocols',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.30.0',
            'fetch': [{
                    'file': './protocols',
                }, {
                    'file': './services',
                },
            ],
        },
    ],
)
def build(build):

    stdlib.fetch.fetch()

    iana = Package(
        PackageID(
            build.manifest.metadata.name,
        ),
    )

    # Drain protocols and services
    iana.drain_build_cache('protocols', 'etc/')
    iana.drain_build_cache('services', 'etc/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    iana.rdepends_on('raven-os/corefs', '*')

    return {
        iana.id.short_name(): iana,
    }

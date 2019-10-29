#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='check',
    category='dev-libs',
    description='''
    A unit testing framework for C.
    ''',
    tags=['unit', 'test', 'ci', 'framework'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://libcheck.github.io/check/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.12.0',
            'fetch': [{
                    'url': 'https://github.com/libcheck/check/releases/download/0.12.0/check-0.12.0.tar.gz',
                    'sha256': '464201098bee00e90f5c4bdfa94a5d3ead8d641f9025b560a27755a83b824234',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # TODO FIXME Remove this when Raven is self-hosted
    with stdlib.pushd(packages['dev-libs/check'].wrap_cache):
        stdlib.cmd("sed -i '1 s/tools/usr/' usr/bin/checkmk")

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-libs/check'].rdepends_on('raven-os/corefs', '*')

    return packages

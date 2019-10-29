#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.template.make import make
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
                    'url': 'http://anduin.linuxfromscratch.org/LFS/iana-etc-2.30.tar.bz2',
                    'sha256': 'b9a6874fb20012836efef75452ef2acae624022d680feeb1994d73facba3f20d',
                },
            ],
        },
    ],
)
#                    'file': './protocols',
#                }, {
#                    'file': './services',
def build(build):

    packages = basic.build(
        compile=make,
    )

    # Drain protocols and services
    packages['sys-libs/iana-etc'].drain_build_cache('protocols', 'etc/')
    packages['sys-libs/iana-etc'].drain_build_cache('services', 'etc/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/iana-etc'].rdepends_on('raven-os/corefs', '*')

    return packages

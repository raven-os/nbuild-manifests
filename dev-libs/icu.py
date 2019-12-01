#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools


@manifest(
    name='icu',
    category='dev-libs',
    description='''
    Libraries providing Unicode and Globalization support.
    ''',
    tags=['unicode', 'globalization'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='http://site.icu-project.org/home',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '64.2.0',
            'fetch': [{
                'url': 'http://download.icu-project.org/files/icu4c/64.2/icu4c-64_2-src.tgz',
                'sha256': '627d5d8478e6d96fc8c90fed4851239079a561a6a8b9e48b0892f24e82d31d6c',
            }],
        },
    ]
)
def build(build):
    packages = autotools.build(
        build_folder='source',
    )

    packages['dev-libs/icu-dev'].drain(
        'usr/{lib64,share}/icu/'
    )

    return packages

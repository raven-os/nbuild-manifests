#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.cmake import cmake
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='z3',
    category='dev-libs',
    description='''
    An efficient theorem prover.
    ''',
    tags=['maths', 'theorem', 'prover', 'solver'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.License.MIT],
    upstream_url='https://github.com/Z3Prover/z3',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.8.7',
            'fetch': [{
                'url': 'https://github.com/Z3Prover/z3/archive/z3-4.8.7.tar.gz',
                'sha256': '8c1c49a1eccf5d8b952dadadba3552b0eac67482b8a29eaad62aa7343a0732c3',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'sys-libs/gmp-dev',
    ]
)
def build(build):
    packages = autotools.build(
        build_folder='build',
        configure=lambda: cmake(folder='..'),
    )

    packages['dev-libs/z3-dev'].drain('usr/lib64/cmake/')

    return packages

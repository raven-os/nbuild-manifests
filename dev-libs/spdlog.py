#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.cmake import cmake
from stdlib.package import Package, PackageID
from stdlib.split.drain_all import drain_all_with_doc_into
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='spdlog',
    category='dev-libs',
    description='''
    A Fast C++ logging library.
    ''',
    tags=['cpp', 'log', 'logging'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/gabime/spdlog',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.4.2',
            'fetch': [{
                'url': 'https://github.com/gabime/spdlog/archive/v1.4.2.tar.gz',
                'sha256': '821c85b120ad15d87ca2bc44185fa9091409777c756029125a02f81354072157',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'sys-apps/systemd-dev',
    ]
)
def build(build):
    return autotools.build(
        configure=cmake,
        split=lambda: drain_all_with_doc_into(
            Package(PackageID('spdlog-dev')),
            Package(PackageID('spdlog-doc')),
        ),
    )

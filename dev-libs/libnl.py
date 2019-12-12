#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


def split_libnl():
    packages = stdlib.split.system.system()

    packages['dev-libs/libnl'].drain_package(
        packages['dev-libs/libnl-dev'],
        'usr/lib64/libnl/',
    )

    return packages


@manifest(
    name='libnl',
    category='dev-libs',
    description='''
    A handler library for evdev events and devices.
    ''',
    tags=['network', 'events', 'devices', 'netlink'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://github.com/thom311/libnl/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.4.0',
            'fetch': [{
                    'url': 'https://github.com/thom311/libnl/releases/download/libnl3_4_0/libnl-3.4.0.tar.gz',
                    'sha256': 'b7287637ae71c6db6f89e1422c995f0407ff2fe50cecd61a312b6a9b0921f5bf',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/flex',
    ]
)
def build(build):
    return autotools.build(
        split=split_libnl,
    )

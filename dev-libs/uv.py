#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='uv',
    category='dev-libs',
    description='''
    libuv is a multi-platform support library with a focus on asynchronous I/O.
    ''',
    tags=['events', 'io', 'async'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://libuv.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.33.1',
            'fetch': [{
                'url': 'https://dist.libuv.org/dist/v1.33.1/libuv-v1.33.1.tar.gz',
                'sha256': 'b4b5dc15103f7bbfecb81a0a9575841fdb7217b9f709634be8118972c1c8ce27',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/automake',
        'sys-libs/libtool'
    ]
)
def build(build):
    return autotools.build(
        configure=lambda: configure(make_configure=lambda: stdlib.cmd("./autogen.sh"))
    )

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='wayland',
    category='sys-libs',
    description='''
    Wayland is intended as a simpler replacement for X, easier to develop and maintain.
    ''',
    tags=['wayland', 'graphics', 'compositor'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://wayland.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.17.0',
            'fetch': [{
                'url': 'https://wayland.freedesktop.org/releases/wayland-1.17.0.tar.xz',
                'sha256': '72aa11b8ac6e22f4777302c9251e8fec7655dc22f9d94ee676c6b276f95f91a4',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/expat-dev',
        'dev-libs/xml2-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-documentation'
        ),
    )

    packages['sys-libs/wayland-dev'].drain(
        'usr/share/wayland/'
    )

    return packages

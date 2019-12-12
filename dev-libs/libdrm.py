#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.meson import meson
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


@manifest(
    name='libdrm',
    category='dev-libs',
    description='''
    A user-space library for accessing the Direct Rendering Manager.
    ''',
    tags=['graphic', 'card', 'drm', 'kernel', 'ioctl', 'opengl', 'vulkan'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://dri.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.4.100',
            'fetch': [{
                    'url': 'https://dri.freedesktop.org/libdrm/libdrm-2.4.100.tar.bz2',
                    'sha256': 'c77cc828186c9ceec3e56ae202b43ee99eb932b4a87255038a80e8a1060d0a5d',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-libs/libpciaccess-dev',
        'dev-libs/libatomic-ops-dev',
        'dev-apps/ninja',
        'dev-libs/libxslt',
    ]
)
def build(build):
    packages = meson_ninja.build(
        configure=lambda: meson(
            '-Dudev=true'
        ),
    )

    packages['dev-libs/libdrm'].drain('./usr/share/libdrm/')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
import stdlib.split.system
from stdlib.template.meson import meson
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


def split_mesa():
    packages = stdlib.split.system.system()

    # Drivers are .so files wrongly attributed to mesa-dev by the package splitter.
    packages['sys-libs/mesa'].drain_package(
        packages['sys-libs/mesa-dev'],
        'usr/lib64/**/*.so'
    )

    return packages


@manifest(
    name='mesa',
    category='sys-libs',
    description='''
    An open-source implementation of OpenGL for Linux.
    ''',
    tags=['opengl', 'graphics'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.mesa3d.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '19.1.4',
            'fetch': [{
                'url': 'https://mesa.freedesktop.org/archive/mesa-19.1.4.tar.xz',
                'sha256': 'a6d268a7d9edcfd92b6da80f2e34e6e0a7baaa442efbeba2fc66c404943c6bfb',
            }],
        },
    ],
    build_dependencies=[
        'dev-apps/ninja',
        'dev-apps/flex',
        'dev-apps/cmake',
        'dev-libs/libdrm-dev',
        'dev-python/mako',
        'dev-libs/libxvmc-dev',
        'dev-libs/llvm-bin-dev',
        'sys-libs/wayland-dev',
        'dev-libs/wayland-protocols',
        'sys-libs/x11-dev',
        'dev-libs/libxdamage-dev',
        'dev-libs/libxshmfence-dev',
        'dev-libs/libxxf86vm-dev',
        'dev-libs/libxrandr-dev',
        'sys-libs/zlib-dev',
        'sys-libs/expat-dev',
        'dev-libs/xcb-dev',
        'dev-libs/libxfixes-dev',
        'dev-libs/libxrender-dev',
        'dev-libs/libxv-dev',
        'sys-libs/xext-dev',
    ]
)
def build(build):
    # TODO FIXME: Split this package, one per graphic card vendor.
    packages = meson_ninja.build(
        configure=lambda: meson(
            '-Ddri-drivers=auto',
            '-Dgallium-drivers=auto',
            '-Dgallium-nine=false',
            '-Dglx=dri',
            '-Dosmesa=gallium',
            '-Dvalgrind=false',
        ),
        split=split_mesa,
    )

    packages['sys-libs/mesa'].drain('usr/share')

    # XXX FIXME TODO: This line is required because both llvm-bin and llvm-bin-dev
    # provide libLLVM-7.so.1, therefore confusing the dependency linker.
    packages['sys-libs/mesa'].requires('dev-libs/llvm-bin')

    return packages

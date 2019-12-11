#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os  # TODO FIXME
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.cmake import cmake
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='feathers',
    category='sys-apps',
    description='''
    A graphical compositor for Raven-OS.
    ''',
    tags=['raven-os', 'raven', 'compositor', 'wayland'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://github.com/raven-os/feathers',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.0.220',
            'fetch': [{
                    'git': 'https://github.com/raven-os/feathers.git',
                    'commit': '2372cc20ea08387f5e4dcc8c4eb7147597e8b551',
                },
            ],
        },
    ],
    build_dependencies=[
        'dev-apps/cmake',
        'sys-libs/wayland-dev',
        'dev-libs/wlroots-dev',
        'sys-libs/pixman-dev',
        'dev-libs/libsocket-dev',
        'sys-libs/mesa-dev',
        'sys-libs/x11-dev',
        'dev-libs/libinput-dev',
        'sys-apps/systemd-dev',
        'dev-libs/xcb-dev',
        'dev-libs/libxkbcommon-dev',
        'sys-libs/albinos-dev',
    ]
)
def build(build):
    return autotools.build(
        build_folder='build',
        patch=lambda: stdlib.cmd('sed "s/Supscription/Subscription/g" -i source/conf/*.cpp'),
        configure=lambda: cmake('..'),
        split=drain_all_with_doc,
    )

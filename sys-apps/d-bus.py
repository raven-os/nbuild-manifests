#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='d-bus',
    category='sys-apps',
    description='''
    A bunch of programs and utilities for controlling the startup, running and shutdown of the system.
    ''',
    tags=['init', 'boot', 'startup', 'daemon', 'journal', 'system', 'log', 'logging'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2, stdlib.license.License.LGPL2_1],
    upstream_url='https://www.freedesktop.org/wiki/Software/systemd/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '241.0.0',
            'fetch': [{
                    'url': 'https://github.com/systemd/systemd/archive/v241/systemd-241.tar.gz',
                    'sha256': 'b2561a8e1d10a2c248253f0dda31a85dd6d69f2b54177de55e02cd1d2778316e',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/d-bus'].requires('raven-os/corefs')

    return packages

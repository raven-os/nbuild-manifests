#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='procps',
    category='sys-apps',
    description='''
    Utilities for monitoring the system and its processes.
    ''',
    tags=['monitoring', 'process', 'activity'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL],
    upstream_url='https://sourceforge.net/projects/procps-ng',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.3.15',
            'fetch': [{
                    'url': 'https://sourceforge.net/projects/procps-ng/files/Production/procps-ng-3.3.15.tar.xz',
                    'sha256': '10bd744ffcb3de2d591d2f6acf1a54a7ba070fdcc432a855931a5057149f0465',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-static',
            '--disable-kill',
            '--with-systemd',
        ),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/procps'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='dbus',
    category='sys-apps',
    description='''
    A message bus system.
    ''',
    tags=['bus', 'message', 'ipc', 'daemon'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM, stdlib.license.License.GPL],
    upstream_url='https://www.freedesktop.org/wiki/Software/dbus',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.12.16',
            'fetch': [{
                    'url': 'https://dbus.freedesktop.org/releases/dbus/dbus-1.12.16.tar.gz',
                    'sha256': '54a22d2fa42f2eb2a871f32811c6005b531b9613b1b93a0d269b05e7549fec80',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-doxygen-docs',
            '--disable-xml-docs',
            '--docdir=/usr/share/doc/dbus',
            '--with-console-auth-dir=/run/console',
        ),
    )

    # Drain common and shared files
    packages['sys-apps/dbus'].drain(
        'usr/share/',
        'usr/lib64/dbus-daemon-launch-helper',
    )

    # Drain the development files laying in unusual places
    packages['sys-apps/dbus-dev'].drain(
        'usr/lib64/**/*.cmake',
        'usr/lib64/**/*.h',
        'usr/lib64/**/*.dtd',
    )

    # Create a symlink, so that D-Bus and systemd can use the same machine-id file:
    packages['sys-apps/dbus'].make_symlink('/etc/machine-id', 'var/lib/dbus/machine-id')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/dbus'].rdepends_on('raven-os/corefs', '*')

    return packages

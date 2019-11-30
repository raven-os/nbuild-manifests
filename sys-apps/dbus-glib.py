#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='dbus-glib',
    category='dev-libs',
    description='''
    GLib interfaces to the D-Bus API.
    ''',
    tags=['glib', 'dbus', 'interface'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.freedesktop.org/wiki/Software/DBusBindings',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.110.0',
            'fetch': [{
                    'url': 'https://dbus.freedesktop.org/releases/dbus-glib/dbus-glib-0.110.tar.gz',
                    'sha256': '7ce4760cf66c69148f6bd6c92feaabb8812dee30846b24cd0f7395c436d7e825',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-apps/dbus-dev',
        'dev-libs/glib-dev',
        'sys-libs/expat-dev'
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/dbus-glib'].drain('usr/lib64/dbus-bash-completion-helper')

    return packages

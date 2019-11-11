#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='emacs',
    category='editor',
    description='''
    GNU Emacs is the extensible self-documenting text editor.
    ''',
    tags=['emacs', 'editor', 'gnu'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/emacs/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '26.2.0',
            'fetch': [{
                'url': 'https://ftp.gnu.org/gnu/emacs/emacs-26.2.tar.xz',
                'sha256': '151ce69dbe5b809d4492ffae4a4b153b2778459de6deb26f35691e1281a9c58e',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/ncurses-dev',
        'sys-apps/dbus-dev',
        'sys-apps/systemd-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-gnutls=no'
        ),
    )

    packages['editor/emacs'].drain(
        'usr/lib64/',
        'usr/share/{applications,icons,emacs}'
    )

    return packages

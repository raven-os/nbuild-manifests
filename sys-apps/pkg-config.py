#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.manifest import manifest


@manifest(
    name='pkg-config',
    category='sys-apps',
    description='''
    A tool to help compiling applications and libraries.
    ''',
    tags=['compiler', 'tool', 'library'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.freedesktop.org/wiki/Software/pkg-config/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.29.2',
            'fetch': [{
                    'url': 'https://pkgconfig.freedesktop.org/releases/pkg-config-0.29.2.tar.gz',
                    'sha256': '6fc69c01688c9458a57eb9a1664c9aba372ccda420a02bf4429fe610e7e7d591',
                },
            ],
        },
    ],
)
def build(build):
    target = os.environ['TARGET']

    packages = autotools.build(
        configure=lambda: configure(
            '--with-internal-glib',
            '--disable-host-tool',
            '--docdir=/usr/share/doc/pkg-config-0.29.2',
        ),
    )

    packages['sys-apps/pkg-config'].drain('usr/share/aclocal/*')
    packages['sys-apps/pkg-config'].make_symlink(
        'pkg-config',
        f'usr/bin/{target}-pkg-config',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/pkg-config'].rdepends_on('raven-os/corefs', '*')

    return packages


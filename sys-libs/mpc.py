#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.manifest import manifest


@manifest(
    name='mpc',
    category='sys-libs',
    description='''
    A library for the arithmetic of complex numbers with arbitrarily high precision and correct rounding.
    ''',
    tags=['gnu', 'math', 'computation', 'complex'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.multiprecision.org/mpc/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz',
                    'sha256': '6985c538143c1208dcb1ac42cedad6ff52e267b47e5f970183a3e75125b43c2e',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--infodir="/usr/share/info/mpc/"',
            '--docdir="/usr/share/doc/"',
        ),
        install=lambda: make('install', 'install-html', f'DESTDIR={stdlib.build.current_build().install_cache}'),
    )

    # Rename documentation directory to match the other packages.
    packages['sys-libs/mpc-doc'].move('usr/share/doc/mpc.html', 'usr/share/doc/mpc')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/mpc'].requires('raven-os/corefs')

    return packages

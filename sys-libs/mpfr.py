#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.manifest import manifest


@manifest(
    name='mpfr',
    category='sys-libs',
    description='''
    A library for multiple-precision floating-point computations with correct rounding.
    ''',
    tags=['gnu', 'math', 'floating-point', 'computation'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.mpfr.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.0.2',
            'fetch': [{
                    'url': 'https://www.mpfr.org/mpfr-current/mpfr-4.0.2.tar.xz',
                    'sha256': '1d3be708604eae0e42d578ba93b390c2a145f17743a744d8f3f8c2ad5855a38a',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--enable-thread-safe',
            '--infodir="/usr/share/info/mpfr/"',
            '--docdir="/usr/share/doc/"'
        ),
        install=lambda: make('install', 'install-html', f'DESTDIR={stdlib.build.current_build().install_cache}'),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/mpfr'].rdepends_on('raven-os/corefs', '*')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='readline',
    category='sys-libs',
    description='''
    A set of libraries that offers command-line editing and history capabilities.
    ''',
    tags=['gnu', 'cli'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://tiswww.case.edu/php/chet/readline/rltop.html',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.0.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/readline/readline-8.0.tar.gz',
                    'sha256': 'e339f51971478d369f8a053a330a190781acb9864cf4c541060f12078948e461',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/ncurses-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-ncurses',
            '--enable-multibyte',
        ),
        compile=lambda: make('SHLIB_LIBS=-lncursesw'),  # Ensures readline is linked against the libncursesw library
        install=lambda: make('install', 'SHLIB_LIBS=-lncursesw', f'DESTDIR={build.install_cache}'),
    )

    # Drain examples in readline-dev
    packages['sys-libs/readline-dev'].drain(
        'usr/share/readline/*.c',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/readline'].requires('raven-os/corefs')

    return packages

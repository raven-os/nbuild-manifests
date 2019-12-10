#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='js',
    category='dev-apps',
    description='''
    JavaScript interpreter and libraries - Version 60.
    ''',
    tags=['JavaScript', 'Mozilla', 'JS'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.MOZILLA],
    upstream_url='https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '60.8.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/teams/releng/tarballs-needing-help/mozjs/mozjs-60.8.0.tar.bz2',
                'sha256': '697331336c3d65b80ded9ca87b4a8ceb804e5342b476eaa133ac638102a9dc5d',
            },
            ],
        },
    ],
    build_dependencies=[
        'dev-libs/icu-dev',
        'sys-apps/which',
        'dev-lang/python2',
        'sys-libs/readline-dev',
        'dev-apps/autoconf2-13'
    ]
)
def build(build):
    packages = autotools.build(
        # export SHELL is required because we're building the package in the chroot environment
        configure=lambda: stdlib.cmd("SHELL=/bin/bash && export SHELL &&\
            mkdir mozjs-build &&                                        \
            cd mozjs-build &&                                           \
            ../js/src/configure --prefix=/usr                           \
            --with-intl-api                                             \
            --with-system-zlib                                          \
            --with-system-icu                                           \
            --disable-jemalloc                                          \
            --enable-readline                                           \
        "),
        compile=lambda: stdlib.cmd("SHELL=/bin/bash && export SHELL &&\
            cd mozjs-build && make"),
        install=lambda: stdlib.cmd("cd mozjs-build && make install")
    )

    packages['dev-apps/js-dev'].drain('usr/lib/libjs_static.ajs')

    return packages

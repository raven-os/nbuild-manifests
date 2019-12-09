#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.patch import patch


def patch_autoconf():
    patch("-Np1 -i ./autoconf-2.13-consolidated_fixes-1.patch")
    stdlib.cmd("mv -v autoconf.texi autoconf213.texi && \
        rm -v autoconf.info")


@manifest(
    name='autoconf2-13',
    category='dev-apps',
    description='''
    A tool for automatically configuring source code (Legacy 2.1x version).
    ''',
    tags=['gnu', 'generator', 'configuration', 'configure', 'makefile', 'make', 'legacy'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://www.gnu.org/software/autoconf/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.13.5',
            'fetch': [{
                'url': 'https://ftp.gnu.org/gnu/autoconf/autoconf-2.13.tar.gz',
                'sha256': 'f0611136bee505811e9ca11ca7ac188ef5323a8e2ef19cffd3edb3cf08fd791e',
            }, {
                'file': './autoconf-2.13-consolidated_fixes-1.patch'
            }
            ],
        },
    ],
    build_dependencies=[
        'sys-apps/texinfo'
    ]
)
def build(build):
    packages = autotools.build(
        patch=lambda: patch_autoconf(),
        # The configure script of autoconf2-13 doesn't have all the usual flags, so we can't
        # rely on the template to help us here. A manual call is required.
        configure=lambda: stdlib.cmd("./configure --program-suffix=2.13"),
        compile=lambda: stdlib.cmd("make"),
        install=lambda: stdlib.cmd(f"make install && \
            install -v -m644 autoconf213.info /usr/local/share/info && \
            install-info --info-dir={build.install_cache}/usr/local/share/info autoconf213.info"),
    )

    packages['dev-apps/autoconf2-13'].drain('usr/local/share/autoconf-2-13/')
    packages['dev-apps/autoconf2-13'].drain('usr/local/share/info/dir')

    return packages

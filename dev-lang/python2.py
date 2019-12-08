#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.manifest import manifest


@manifest(
    name='python2',
    category='dev-lang',
    description='''
        A programming language that lets you work quickly and integrate systems more effectively.
    ''',
    tags=['python', 'python2', 'language', 'scripting'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.python.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.7.17',
            'fetch': [{
                'url': 'https://www.python.org/ftp/python/2.7.17/Python-2.7.17.tar.xz',
                'sha256': '4d43f033cdbd0aa7b7023c81b0e986fd11e653b5248dac9144d508f11812ba41',
            },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'sys-libs/ncurses-dev',
        'sys-libs/readline-dev',
        'sys-libs/expat-dev',
        'sys-libs/gdbm-dev',
        'sys-libs/openssl-dev',
        'sys-apps/bzip2-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-system-expat',
            '--with-system-ffi',
            '--without-ensurepip',
            '--enable-unicode=ucs4',
            '--enable-optimizations'),
        split=drain_all_with_doc,
    )

    with stdlib.pushd(packages['dev-lang/python2'].wrap_cache):
        # Fixes permissions for libraries to be consistent with other libraries
        for lib in glob.glob('usr/lib64/libpython{build.major}.{build.minor}.so.*.*'):
            os.chmod(lib, 0o755)
        # Renaming to avoid conflicts with the binaries installed by Python3
        os.rename('usr/bin/2to3', 'usr/bin/2to3-2')
        os.rename('usr/bin/idle', 'usr/bin/idle2')
        os.rename('usr/bin/pydoc', 'usr/bin/pydoc2')

    return packages

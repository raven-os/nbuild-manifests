#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libedit',
    category='sys-libs',
    description='''
    A line editor library providing generic line editing, history, and tokenization functions.
    ''',
    tags=['bsd', 'cli', 'history'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='http://thrysoee.dk/editline/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.1.20191025',
            'fetch': [{
                'url': 'http://thrysoee.dk/editline/libedit-20191025-3.1.tar.gz',
                'sha256': '6dff036660d478bfaa14e407fc5de26d22da1087118c897b1a3ad2e90cb7bf39',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/ncurses-dev',
    ]
)
def build(build):
    packages = autotools.build()

    # Debian changed the SO version to libedit.so.2.
    # Create a compatibility symlink to ensure binaries built on debian can run on Raven-OS.
    packages['sys-libs/libedit'].make_symlink('libedit.so.0', 'usr/lib64/libedit.so.2')

    return packages

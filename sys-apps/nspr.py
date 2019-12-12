#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.split.system import system


def split_nspr():
    packages = system()

    packages['sys-apps/nspr'].drain_package(
        packages['sys-apps/nspr-dev'],
        'usr/lib64/*.so'
    )
    return packages


@manifest(
    name='nspr',
    category='sys-apps',
    description='''
    A platform-neutral API for system level and libc like functions.
    ''',
    tags=['nspr', 'api', 'mozilla'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.MOZILLA],
    upstream_url='https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.24.0',
            'fetch': [{
                'url': 'https://archive.mozilla.org/pub/nspr/releases/v4.24/src/nspr-4.24.tar.gz',
                'sha256': '90a59a0df6a11528749647fe18401cc7e03881e3e63c309f8c520ce06dd413d0',
            }],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure('--with-mozilla',
                                    '--with-pthreads',
                                    '--enable-64bit'),
        split=split_nspr
    )

    return packages

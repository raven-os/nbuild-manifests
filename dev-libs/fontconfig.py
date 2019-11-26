#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure


@manifest(
    name='fontconfig',
    category='dev-libs',
    description='''
    The fontconfig package contains a library and programs for configuring and customizing font access.
    ''',
    tags=['dev', 'font', 'fonts', 'configuration'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.freedesktop.org/wiki/Software/fontconfig/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.13.1',
            'fetch': [{
                'url': 'https://www.freedesktop.org/software/fontconfig/release/fontconfig-2.13.1.tar.bz2',
                'sha256': 'f655dd2a986d7aa97e052261b36aa67b0a64989496361eca8d604e6414006741',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/freetype-dev',
        'sys-libs/expat-dev',
        'sys-libs/gperf',
        'sys-apps/util-linux-dev'
    ]
)
def build(build):
    packages = autotools.build(
        patch=lambda: stdlib.cmd('rm -f src/fcobjshash.h'),
        configure=lambda: configure('--disable-docs'),
    )

    packages['dev-libs/fontconfig'].drain(
        'usr/share/{fontconfig,gettext,xml}'
    )

    return packages

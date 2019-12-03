#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xkeyboard-config',
    category='dev-resources',
    description='''
    A keyboard configuration database for X.
    ''',
    tags=['x11', 'xorg', 'keyboard', 'configuration', 'database'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.freedesktop.org/wiki/Software/XKeyboardConfig',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.27.0',
            'fetch': [{
                'url': 'https://www.x.org/pub/individual/data/xkeyboard-config/xkeyboard-config-2.27.tar.bz2',
                'sha256': '690daec8fea63526c07620c90e6f3f10aae34e94b6db6e30906173480721901f',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/x11-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-xkb-rules-symlink=xorg',
        )
    )

    packages['dev-resources/xkeyboard-config'].drain('usr/share/*')

    return packages

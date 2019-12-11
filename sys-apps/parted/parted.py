#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


def patch_parted():
    stdlib.patch.patch_all()

    # Fix some includes to prevent a linking error
    stdlib.cmd(r'''sed -i '/utsname.h/a#include <sys/sysmacros.h>' libparted/arch/linux.c''')


@manifest(
    name='parted',
    category='sys-apps',
    description='''
    A disk partitioning and partition resizing tool
    ''',
    tags=['gnu', 'partition', 'gpt', 'disk'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/parted/parted.html',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.2.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/parted/parted-3.2.tar.xz',
                    'sha256': '858b589c22297cacdf437f3baff6f04b333087521ab274f7ab677cb8c6bb78e4',
                }, {
                    'file': 'parted-3.2-devmapper-1.patch',
                }
            ],
        },
    ],
    build_dependencies=[
        'sys-apps/util-linux-dev',
        'sys-libs/ncurses-dev',
        'sys-libs/readline-dev',
    ]
)
def build(build):
    return autotools.build(
        patch=patch_parted,
        configure=lambda: configure(
            '--disable-device-mapper'
        )
    )

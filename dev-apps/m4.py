#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


def patch_m4():
    build = stdlib.build.current_build()

    # Fix a bug introduced by glibc 2.28
    # http://www.linuxfromscratch.org/lfs/view/stable/chapter06/m4.html
    with stdlib.pushd(build.build_cache):
        stdlib.cmd("sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' lib/*.c")
        stdlib.cmd('echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h')


@manifest(
    name='m4',
    category='dev-apps',
    description='''
    An implementation of the traditional Unix macro processor.
    ''',
    tags=['gnu', 'macro', 'preprocessor'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/m4/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.4.18',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.xz',
                    'sha256': 'f2c1e86ca0a404ff281631bdc8377638992744b175afb806e25871a24a934e07',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_m4,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/m4'].requires('raven-os/corefs')

    return packages

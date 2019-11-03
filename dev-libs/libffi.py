#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
import stdlib.patch
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


def patch_libffi():
    stdlib.patch.patch_all()

    # Modify the Makefile to install headers into the standard /usr/include directory
    stdlib.cmd("sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' -i include/Makefile.in")
    stdlib.cmd("""
        sed -e '/^includedir/ s/=.*$/=@includedir@/' \
            -e 's/^Cflags: -I${includedir}/Cflags:/' \
            -i libffi.pc.in
    """)


@manifest(
    name='libffi',
    category='dev-libs',
    description='''
    A library that provides a portable, high level programming interface to various calling conventions.
    ''',
    tags=['elf', 'ffi', 'calling', 'convention', 'binary'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://sourceware.org/libffi/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.2.1',
            'fetch': [{
                    'url': 'https://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz',
                    'sha256': 'd06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_libffi,
        configure=lambda: configure(
            '--with-gcc-arch=generic',
        ),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-libs/libffi'].requires('raven-os/corefs')

    return packages

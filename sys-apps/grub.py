#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='grub',
    category='sys-apps',
    description='''
    The GRand Unified Bootloader.
    ''',
    tags=['gnu', 'bootloader', 'boot'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.gnu.org/software/grub/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.4.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/grub/grub-2.04.tar.xz',
                    'sha256': 'e5292496995ad42dabe843a0192cf2a2c502e7ffcc7479398232b10a472df77d',
                },
            ],
        },
    ],
)
def build(build):
    # TODO FIXME
    del os.environ['CFLAGS']
    del os.environ['CXXFLAGS']
    del os.environ['LDFLAGS']

    # stdlib.fetch.fetch()
    # stdlib.extract.flat_extract_all()
    # stdlib.patch.patch_all()

    packages = autotools.build_all(
        compilations=[
            {
                'configure': lambda: configure(
                    '--disable-efiemu',
                    '--with-platform=pc',
                ),
            }, {
                'clean_before': lambda: make('clean'),
                'configure': lambda: configure(
                    '--disable-efiemu',
                    '--with-platform=efi',
                ),
            }
        ],
        split=drain_all_with_doc,
    )

    # common_conf = [
    #     '--disable-efiemu',
    # ]

    # # Run once for each target

    # autotools.build(
    #     fetch=None,
    #     extract=None,
    #     patch=None,
    #     configure=lambda: configure(
    #         *common_conf,
    #         '--with-platform=pc',
    #     ),
    #     split=None,
    #     deplinker=None,
    # )

    # make('clean')

    # packages = autotools.build(
    #     fetch=None,
    #     extract=None,
    #     patch=None,
    #     configure=lambda: configure(
    #         *common_conf,
    #         '--with-platform=efi',
    #     ),
    #     split=drain_all_with_doc,
    # )

    # # Move a file to a more typical location
    # packages['sys-apps/grub'].move('etc/bash_completion.d/grub', 'usr/share/bash-completion/completions/')

    # # Packages member of `raven-os/essentials` should explicitly state all
    # # of their dependencies, including indirect ones.
    # packages['sys-apps/grub'].rdepends_on('raven-os/corefs', '*')

    return packages

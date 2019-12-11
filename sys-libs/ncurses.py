#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='ncurses',
    category='sys-libs',
    description='''
    A free software emulation of curses.
    ''',
    tags=['ncurse', 'terminal', 'tui'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.License.MIT],
    upstream_url='https://www.gnu.org/software/ncurses/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '6.1.0',
            'fetch': [{
                'url': 'https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.1.tar.gz',
                'sha256': 'aa057eeeb4a14d470101eff4597d5833dcef5965331be3528c08d99cebaa0d17',
                },
            ],
        },
    ],
)
def build(build):
    stdlib.fetch.fetch()
    stdlib.extract.flat_extract_all()
    stdlib.patch.patch_all()

    common_conf = [
        '--with-cxx-shared',
        '--without-debug',
        '--disable-termcap',
        '--enable-symlinks',
        '--enable-colorfgbg',
        '--enable-pc-files',
    ]

    # Ncurses
    autotools.build(
        fetch=None,
        extract=None,
        patch=None,
        configure=lambda: configure(*common_conf),
        split=None,
        deplinker=None,
    )

    # Ncursesw
    autotools.build(
        fetch=None,
        extract=None,
        patch=None,
        configure=lambda: configure(
            '--enable-widec',
            '--includedir=/usr/include/ncursesw',
            *common_conf,
        ),
        split=None,
        deplinker=None,
    )

    # Ncursest
    autotools.build(
        fetch=None,
        extract=None,
        patch=None,
        configure=lambda: configure(
            '--with-pthread',
            '--includedir=/usr/include/ncursest',
            *common_conf,
        ),
        split=None,
        deplinker=None,
    )

    # Ncursestw
    packages = autotools.build(
        fetch=None,
        extract=None,
        patch=None,
        configure=lambda: configure(
            '--with-pthread',
            '--enable-widec',
            '--includedir=/usr/include/ncursestw',
            *common_conf,
        ),
    )

    # Create the libtinfo symlinks required by some binaries
    #   TODO FIXME : Find a better solution to this... When we won't be rushing the beta!
    packages['sys-libs/ncurses-dev'].make_symlink('libncurses.so', 'usr/lib64/libtinfo.so')
    packages['sys-libs/ncurses'].make_symlink(f'libncurses.so.{build.major}', f'usr/lib64/libtinfo.so.{build.major}')
    packages['sys-libs/ncurses'].make_symlink(f'libncurses.so.{build.major}.{build.minor}', f'usr/lib64/libtinfo.so.{build.major}.{build.minor}')

    packages['sys-libs/ncurses'].drain(
        'usr/share/terminfo/',
        'usr/share/tabset/',
    )

    packages['sys-libs/ncurses-doc'].drain_build_cache(
        'doc/*',
        'usr/share/doc/ncurses/',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/ncurses'].requires('raven-os/corefs')

    return packages

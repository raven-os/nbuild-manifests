#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='elfutils',
    category='sys-dev',
    description='''
    Utilities to handle ELF object files and DWARF debugging informations.
    ''',
    tags=['elf', 'dwarf', 'object', 'binary'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://sourceware.org/elfutils/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.177.0',
            'fetch': [{
                    'url': 'https://sourceware.org/ftp/elfutils/0.177/elfutils-0.177.tar.bz2',
                    'sha256': 'fa489deccbcae7d8c920f60d85906124c1989c591196d90e0fd668e3dc05042e',
                },
            ],
        },
    ],
)
def build(build):

    # TODO FIXME Install only libelf

    packages = autotools.build(
        install=lambda: make('install', f'DESTDIR={stdlib.build.current_build().install_cache}', folder='libelf'),
        split=drain_all_with_doc,
    )

    # Manually install missing PC files
    packages['sys-dev/elfutils'].drain_build_cache(
        'config/libelf.pc',
        'usr/lib/pkgconfig/'
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-dev/elfutils'].rdepends_on('raven-os/corefs', '*')

    return packages

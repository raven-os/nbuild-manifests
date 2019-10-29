#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import textwrap
from stdlib.template import autotools
from stdlib.template.make import make
from stdlib.manifest import manifest


def patch_gmp():
    # The default settings of GMP produce libraries optimized for the host processor.
    # This enabled a more generic configuration so the library can be used on less capable processors.
    os.rename('configfsf.guess', 'config.guess')
    os.rename('configfsf.sub', 'config.sub')


@manifest(
    name='gmp',
    category='sys-libs',
    description='''
    The GNU Multiple Precision Arithmetic Library.
    ''',
    tags=['gnu', 'math', 'arithmetic'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://gmplib.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '6.1.2',
            'fetch': [{
                    'url': 'https://gmplib.org/download/gmp/gmp-6.1.2.tar.xz',
                    'sha256': '87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_gmp,
        configure=lambda: stdlib.cmd(f'''\
            ./configure \\
                --enable-cxx \\
                --enable-shared \\
                --enable-static \\
                {' '.join(stdlib.template.configure.get_dir_flags())} \\
                --infodir="/usr/share/info/gmp/" \\
                --docdir="/usr/share/doc/" \\
        '''),
        install=lambda: make('install', 'install-html', f'DESTDIR={stdlib.build.current_build().install_cache}'),
    )

    # Rename documentation directory to match the other packages.
    packages['sys-libs/gmp-doc'].move('usr/share/doc/gmp.html', 'usr/share/doc/gmp')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/gmp'].rdepends_on('raven-os/corefs', '*')

    return packages

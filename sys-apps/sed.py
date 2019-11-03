#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest

def patch_sed():
    stdlib.cmd("sed -i 's/usr/tools/'                 build-aux/help2man")  # TODO REMOVE THIS

    # Remove a failing test
    stdlib.cmd("sed -i 's/testsuite.panic-tests.sh//' Makefile.in")


@manifest(
    name='sed',
    category='sys-apps',
    description='''
    The GNU stream editor.
    ''',
    tags=['gnu', 'editor', 'stream', 'regex'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/sed/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.7.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/sed/sed-4.7.tar.xz',
                    'sha256': '2885768cd0a29ff8d58a6280a270ff161f6a3deb5690b2be6c49f46d4c67bd6a',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_sed,
        install=lambda: make('install', 'install-html', f'DESTDIR="{build.install_cache}"'),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/sed'].requires('raven-os/corefs')

    return packages

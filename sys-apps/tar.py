#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


def install_tar():
    make('install', f'DESTDIR={stdlib.build.current_build().install_cache}'),
    make('install-html', f'docdir=/usr/share/doc/tar/', folder='doc')


@manifest(
    name='tar',
    category='sys-apps',
    description='''
    An archiving program.
    ''',
    tags=['gnu', 'tarball', 'archive'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.gnu.org/software/tar/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.32.0',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/tar/tar-1.32.tar.xz',
                    'sha256': 'd0d3ae07f103323be809bc3eac0dcc386d52c5262499fe05511ac4788af1fdd8',
                },
            ],
        },
    ],
)
def build(build):
    os.environ['FORCE_UNSAFE_CONFIGURE'] = '1'

    packages = autotools.build(
        install=install_tar,
        split=drain_all_with_doc,
    )

    packages['sys-apps/tar-doc'].move('usr/share/doc/tar/tar.html/*', 'usr/share/doc/tar/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/tar'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='texinfo',
    category='sys-apps',
    description='''
    The GNU utilities for on-line information and printed output.
    ''',
    tags=['gnu', 'info', 'tex'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.gnu.org/software/texinfo/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '6.6.0',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/texinfo/texinfo-6.6.tar.xz',
                    'sha256': '9bb9ca00da53f26a7e5725eee49689cd4a1e18d25d5b061ac8b2053018d93d66',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        install=lambda: make('install', 'install-tex', f'DESTDIR={stdlib.build.current_build().install_cache}', 'TEXMF=/usr/share/texmf'),
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/texinfo'].rdepends_on('raven-os/corefs', '*')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gdbm',
    category='sys-libs',
    description='''
    A database library that works similar to the standard UNIX dbm.
    ''',
    tags=['gnu', 'database', 'db'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org.ua/software/gdbm/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.18.1',
            'fetch': [{
                    'url': 'ftp://ftp.gnu.org/gnu/gdbm/gdbm-1.18.1.tar.gz',
                    'sha256': '86e613527e5dba544e73208f42b78b7c022d4fa5a6d5498bf18c8d6f745b91dc',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--enable-libgdbm-compat',
        ),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/gdbm'].rdepends_on('raven-os/corefs', '*')

    return packages

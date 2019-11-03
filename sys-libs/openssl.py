#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


def split_openssl():
    packages = stdlib.split.system.system()

    # Drain some annexe libraries.
    packages['sys-libs/openssl'].drain('usr/lib/engines*')

    # Drain the documentation
    packages['sys-libs/openssl-doc'].drain_build_cache('doc/*', 'usr/share/doc/openssl/')

    return packages


@manifest(
    name='openssl',
    category='sys-libs',
    description='''
    Tools and libraries related to cryptography.
    ''',
    tags=['cryptography', 'ssl', 'tls', 'rsa', 'https'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://www.openssl.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.1',
            'fetch': [{
                    'url': 'https://www.openssl.org/source/openssl-1.1.1c.tar.gz',
                    'sha256': 'f6fb3079ad15076154eda9413fed42877d668e7069d9b87396d0804fdb3f4c90',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: stdlib.cmd('''./config    \
            --prefix=/usr                   \
            --openssldir=/etc/ssl           \
            --libdir=lib                    \
            shared                          \
            zlib-dynamic                    \
        '''),
        check=lambda: make('test', fail_ok=True),
        install=lambda: make('install', 'MANSUFFIX=ssl', f'DESTDIR={stdlib.build.current_build().install_cache}'),
        split=split_openssl,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/openssl'].requires('raven-os/corefs')

    return packages

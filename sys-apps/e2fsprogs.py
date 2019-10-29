#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='e2fsprogs',
    category='sys-apps',
    description='''
    Extended file-system utilitites.
    ''',
    tags=['ext2', 'ext3', 'ext4', 'file-system'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL, stdlib.license.License.MIT],
    upstream_url='http://e2fsprogs.sourceforge.net/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.45.3',
            'fetch': [{
                    'url': 'https://downloads.sourceforge.net/project/e2fsprogs/e2fsprogs/v1.45.3/e2fsprogs-1.45.3.tar.gz',
                    'sha256': '3a5556e0cb746c214e4c581951a3c21ba5c145eb53008277f88f1f98ae75983d',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--enable-elf-shlibs',
            '--disable-libblkid',
            '--disable-libuuid',
            '--disable-uuidd',
            '--disable-fsck',
        ),
        install=lambda: make('install', 'install-libs', f'DESTDIR={stdlib.build.current_build().install_cache}'),
    )

    packages['sys-apps/e2fsprogs'].drain(
        'usr/share/*/*.awk',
        'usr/share/*/*.sed',
        'usr/lib64/*',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/e2fsprogs'].rdepends_on('raven-os/corefs', '*')

    return packages

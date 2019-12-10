#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='cpio',
    category='sys-apps',
    description='''
    A set of tools for archiving.
    ''',
    tags=['gnu', 'archive', 'io', 'tools'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.gnu.org/software/cpio',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.13.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/cpio/cpio-2.13.tar.bz2',
                    'sha256': 'eab5bdc5ae1df285c59f2a4f140a98fc33678a0bf61bdba67d9436ae26b46f6d',
                },
            ],
        },
    ],
)
def build(build):
    return autotools.build(
        configure=lambda: configure(
            '--enable-mt',
            '--with-rmt=/usr/libexec/rmt',
        ),
    )

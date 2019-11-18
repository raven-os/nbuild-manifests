#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='intltool',
    category='dev-apps',
    description='''
    A set of tools used to extract translatable strings from source files.
    ''',
    tags=['translation', 'generator', 'internationalization'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://launchpad.net/intltool',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.51.0',
            'fetch': [{
                    'url': 'https://launchpad.net/intltool/trunk/0.51.0/+download/intltool-0.51.0.tar.gz',
                    'sha256': '67c74d94196b153b774ab9f89b2fa6c6ba79352407037c8c14d5aeb334e959cd',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Drain some shared files
    packages['dev-apps/intltool'].drain('usr/share/intltool/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/intltool'].requires('raven-os/corefs')

    return packages

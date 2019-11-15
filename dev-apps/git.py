#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
import textwrap
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all_with_doc


@manifest(
    name='git',
    category='dev-apps',
    description='''
    A fast, distributed version control system.
    ''',
    tags=['git', 'version', 'control', 'system', 'linux'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://git-scm.com/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.23.0',
            'fetch': [{
                    'url': 'https://github.com/git/git/archive/v2.23.0.tar.gz',
                    'sha256': '7d84f5d6f48e95b467a04a8aa1d474e0d21abc7877998af945568d2634fea46a',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            make_configure=lambda: make('configure'),
        ),
        compile=lambda: make('all'),
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/git'].requires('raven-os/corefs')

    return packages

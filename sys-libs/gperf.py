#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='gperf',
    category='sys-libs',
    description='''
    A perfect hash function generator.
    ''',
    tags=['gnu', 'hash', 'generator'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/gperf/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.1.0',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/pub/gnu/gperf/gperf-3.1.tar.gz',
                    'sha256': '588546b945bba4b70b6a3a616e80b4ab466e3f33024a352fc2198112cdbb3ae2',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        check=lambda: make('-j1', 'check'),  # Tests are known to fail if run simultaneously
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/gperf'].rdepends_on('raven-os/corefs', '*')

    return packages


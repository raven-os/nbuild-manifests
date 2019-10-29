#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libpipeline',
    category='sys-libs',
    description='''
    A C library for manipulating pipelines of subprocesses in a flexible and convenient way.
    ''',
    tags=['pipeline', 'subprocess'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://savannah.nongnu.org/projects/libpipeline',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.5.1',
            'fetch': [{
                    'url': 'https://download.savannah.nongnu.org/releases/libpipeline/libpipeline-1.5.1.tar.gz',
                    'sha256': 'd633706b7d845f08b42bc66ddbe845d57e726bf89298e2cee29f09577e2f902f',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/libpipeline'].rdepends_on('raven-os/corefs', '*')

    return packages

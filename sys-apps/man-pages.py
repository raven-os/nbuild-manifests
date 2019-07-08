#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib.split.drain_all
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='man-pages',
    category='sys-apps',
    description='''
    A collection of over 2,200 man pages that document and describe the behavior of the Linux kernel
    and C library interfaces employed by many user-space programs.
    ''',
    tags=['man', 'libc', 'linux', 'kernel'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.CUSTOM],
    upstream_url='https://www.kernel.org/doc/man-pages/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.1.0',
            'fetch': [{
                    'url': 'https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-5.01.tar.xz',
                    'sha256': '7dfce1334e22e2565cf219a83c5cdfa1fc5e877d54ee15a0d1f5f1de5143b627',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=None,
        split=stdlib.split.drain_all.drain_all,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/man-pages'].rdepends_on('raven-os/corefs', '*')

    return packages

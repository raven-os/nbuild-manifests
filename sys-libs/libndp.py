#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure


@manifest(
    name='libndp',
    category='sys-libs',
    description='''
    Library for Neighbor Discovery Protocol.
    ''',
    tags=['network', 'ndptool'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='http://libndp.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.7.0-1',
            'fetch': [{
                    'url': 'http://libndp.org/files/libndp-1.7.tar.gz',
                    'sha256': '2c480afbffb02792dbae3c13bbfb71d89f735562f2795cca0640ed3428b491b6',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--localstatedir=/var',
            '--disable-static'
        ),
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/libndp'].requires('raven-os/corefs')

    return packages

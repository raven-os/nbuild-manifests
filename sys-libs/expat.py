#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='expat',
    category='sys-libs',
    description='''
    A stream-oriented C library for XML parsing.
    ''',
    tags=['xml', 'parser'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://libexpat.github.io/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.2.8',
            'fetch': [{
                    'url': 'https://github.com/libexpat/libexpat/releases/download/R_2_2_8/expat-2.2.8.tar.xz',
                    'sha256': '61caa81a49d858afb2031c7b1a25c97174e7f2009aa1ec4e1ffad2316b91779b',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()

    packages['sys-libs/expat-doc'].drain_build_cache('doc/*.{html,png,css}', 'usr/share/doc/expat/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/expat'].rdepends_on('raven-os/corefs', '*')

    return packages

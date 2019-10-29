#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os  # TODO FIXME
import stdlib
from stdlib.template.configure import configure
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='kbd',
    category='sys-apps',
    description='''
    A collection of keytable files and keyboard utilities.
    ''',
    tags=['keyboard', 'keytable'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='http://kbd-project.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.2.0',
            'fetch': [{
                    'url': 'https://mirrors.edge.kernel.org/pub/linux/utils/kbd/kbd-2.2.0.tar.xz',
                    'sha256': '21a1bc5f6fb3b18ce9fdd717e4533368060a3182a39c7155eaf7ec0f5f83e9f7',
                }, {
                    'file': './kbd-2.2.0-backspace-1.patch'
                }
            ],
        },
    ],
)
def build(build):

    # TODO FIXME
    os.environ['PKG_CONFIG_PATH'] = '/tools/lib/pkgconfig'

    packages = autotools.build(
        configure=lambda: configure(
            '--disable-vlock',  # vlock requires PAM, which, when this manifest was written, wasn't available (Sept. 2019)
        ),
        split=drain_all_with_doc,
    )

    packages['sys-apps/kbd-doc'].drain_build_cache('docs/doc/*',  'usr/share/doc/kbd/')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/kbd'].rdepends_on('raven-os/corefs', '*')

    return packages

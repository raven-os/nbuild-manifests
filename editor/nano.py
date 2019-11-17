#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='nano',
    category='editor',
    description='''
    Pico editor clone with enhancements.
    ''',
    tags=['editor', 'text'],
    maintainer='dorian.trubelle@epiteh.eu',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.nano-editor.org',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.5.0',
            'fetch': [{
                    'url': 'https://www.nano-editor.org/dist/v4/nano-4.5.tar.xz',
                    'sha256': 'ded5c38f5ecd9de2b624e0db8013a375c169d3fbbd49575967b868847df8f533'
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/ncurses-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--enable-color',
            '--enable-nanorc',
            '--enable-multibuffer'
        ),
        split=drain_all_with_doc
    )

    return packages

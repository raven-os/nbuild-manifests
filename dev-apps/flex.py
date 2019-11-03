#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='flex',
    category='dev-apps',
    description='''
    A fast lexical analyser generator.
    ''',
    tags=['gnu', 'lexer', 'generator'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.gnu.org/software/flex/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.6.4',
            'fetch': [{
                    'url': 'https://github.com/westes/flex/files/981163/flex-2.6.4.tar.gz',
                    'sha256': 'e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995',
                },
            ],
        },
    ],
)
def build(build):

    # No package provide help2man yet, so avoid a compilation failure by preveting the generation of manuals.
    # TODO FIXME
    os.environ['HELP2MAN'] = '/tools/bin/true'

    packages = autotools.build()

    # Make a symlink to its predecessor, `lex`.
    packages['dev-apps/flex'].make_symlink('flex', 'usr/bin/lex')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/flex'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='make',
    category='dev-apps',
    description='''
    An utility to automate the compilation of other programs.
    ''',
    tags=['gnu', 'compilation', 'parallel'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/make/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.2.1',
            'fetch': [{
                    'url': 'http://ftp.gnu.org/gnu/make/make-4.2.1.tar.gz',
                    'sha256': 'e40b8f018c1da64edd1cc9a6fce5fa63b2e707e404e20cad91fbae337c98a5b7',
                }, {
                    'file': './make-4.2.1-glibc-2.27.patch',
                }
            ],
        },
    ],
)
def build(build):

    packages = autotools.build(
        check=lambda: make(f'PERL5LIB={os.getcwd()}/tests', 'check'),
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/make'].rdepends_on('raven-os/corefs', '*')

    return packages

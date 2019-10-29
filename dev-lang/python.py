#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='python',
    category='dev-lang',
    description='''
    A programming language that lets you work quickly and integrate systems more effectively.
    ''',
    tags=['python', 'python3', 'script', 'language'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.python.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.7.4',
            'fetch': [{
                    'url': 'https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz',
                    'sha256': 'fb799134b868199930b75f26678f18932214042639cd52b16da7fd134cd9b13f',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-system-expat',
            '--with-system-ffi',
            '--with-ensurepip=yes',
        ),
        split=drain_all_with_doc,
    )

    # Make it executable
    with stdlib.pushd(packages['dev-lang/python'].wrap_cache):
        os.chmod(f'usr/lib64/libpython{build.major}.{build.minor}m.so', 0o0755)
        os.chmod(f'usr/lib64/libpython{build.major}.so', 0o0755)

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-lang/python'].rdepends_on('raven-os/corefs', '*')

    return packages

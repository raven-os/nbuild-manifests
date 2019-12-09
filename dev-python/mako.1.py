#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import distutils
from stdlib.manifest import manifest

PYTHON_MAJOR = '3'
PYTHON_MINOR = '7'


@manifest(
    name='giscanner',
    category='dev-python',
    description='''
    A template library written in Python.
    ''',
    tags=['python', 'python3', 'template'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://www.makotemplates.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.0',
            'fetch': [{
                    'url': 'https://files.pythonhosted.org/packages/source/M/Mako/Mako-1.1.0.tar.gz',
                    'sha256': 'a36919599a9b7dc5d86a7a8988f23a9a3a3d083070023bab23d64f7f1d1e0a4b',
                },
            ],
        },
    ],
    build_dependencies=[
        f'dev-lang/python#~{PYTHON_MAJOR}.{PYTHON_MINOR}',
    ],
)
def build(build):
    packages = distutils.build()

    packages['dev-python/mako'].requires('dev-python/markupsafe')

    return packages

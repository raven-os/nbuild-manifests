#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import textwrap
from stdlib.template import distutils
from stdlib.manifest import manifest

PYTHON_MAJOR = '3'
PYTHON_MINOR = '7'


@manifest(
    name='setuptools',
    category='dev-python',
    description='''
    Easily download, build, install, upgrade, and uninstall Python packages.
    ''',
    tags=['python', 'python3', 'build', 'system'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.PSF],
    upstream_url='https://github.com/pypa/setuptools',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '41.6.0',
            'fetch': [{
                    'url': 'https://github.com/pypa/setuptools/archive/v41.6.0.tar.gz',
                    'sha256': '1b91aa309ffa43656774984557d62fae1fded0491a16ba8084b21c92cd5ad093',
                },
            ],
        },
    ],
    build_dependencies=[
        f'dev-lang/python#~{PYTHON_MAJOR}.{PYTHON_MINOR}',
    ],
)
def build(build):
    packages = distutils.build(
        patch=lambda: stdlib.cmd(f'python{PYTHON_MAJOR}.{PYTHON_MINOR} ./bootstrap.py'),
    )

    packages['dev-python/setuptools'].requires('dev-lang/python#~3.7')

    return packages

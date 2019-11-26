#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import distutils
from stdlib.manifest import manifest

PYTHON_MAJOR = '3'
PYTHON_MINOR = '7'


@manifest(
    name='markupsafe',
    category='dev-python',
    description='''
    A XML/HTML/XHTML Markup safe string for Python.
    ''',
    tags=['python', 'python3', 'xml', 'html', 'xhtml'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://pypi.python.org/pypi/MarkupSafe',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.1',
            'fetch': [{
                    'url': 'https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-1.1.1.tar.gz',
                    'sha256': '29872e92839765e546828bb7754a68c418d927cd064fd4708fab9fe9c8bb116b',
                },
            ],
        },
    ],
    build_dependencies=[
        f'dev-lang/python#~{PYTHON_MAJOR}.{PYTHON_MINOR}',
    ],
)
def build(build):
    return distutils.build()

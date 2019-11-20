#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='which',
    category='sys-apps',
    description='''
    A utility to show the full path of commands
    ''',
    tags=['cli', 'tool'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://savannah.gnu.org/projects/which',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.21.0',
            'fetch': [{
                'url': 'https://ftp.gnu.org/gnu/which/which-2.21.tar.gz',
                'sha256': 'f4a245b94124b377d8b49646bf421f9155d36aa7614b6ebf83705d3ffc76eaad',
            }],
        },
    ]
)
def build(build):
    return autotools.build()

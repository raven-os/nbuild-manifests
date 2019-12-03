#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libxxf86vm',
    category='dev-libs',
    description='''
    A Video Mode extension library for X.
    ''',
    tags=['x11', 'xorg', 'video', 'mode'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://xorg.freedesktop.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.1.4',
            'fetch': [{
                'url': 'https://www.x.org/archive//individual/lib/libXxf86vm-1.1.4.tar.bz2',
                'sha256': 'afee27f93c5f31c0ad582852c0fb36d50e4de7cd585fcf655e278a633d85cd57',
            }],
        },
    ],
)
def build(build):
    return autotools.build()

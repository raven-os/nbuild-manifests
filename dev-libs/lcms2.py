#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='lcms2',
    category='dev-libs',
    description='''
    A small-footprint color management engine
    ''',
    tags=['color', 'management', 'engine', 'system', 'cms', 'cme'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='http://www.littlecms.com/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.9.0',
            'fetch': [{
                'url': 'https://downloads.sourceforge.net/lcms/lcms2-2.9.tar.gz',
                'sha256': '48c6fdf98396fa245ed86e622028caf49b96fa22f3e5734f853f806fbc8e7d20',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libtiff-dev',
        'dev-libs/libjpeg-turbo-dev',
    ]
)
def build(build):
    return autotools.build()

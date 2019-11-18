#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='xml2',
    category='dev-libs',
    description='''
    XML parsing library, version 2
    ''',
    tags=['xml2', 'xml', 'parsing'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='http://www.xmlsoft.org/',  # XMLSoft's website does not support HTTPS
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.9.10',
            'fetch': [{
                'url': 'http://xmlsoft.org/sources/libxml2-2.9.10.tar.gz',  # XMLSoft's website does not support HTTPS
                'sha256': 'aafee193ffb8fe0c82d4afef6ef91972cbaf5feea100edc2f262750611b4be1f',
            }],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'sys-apps/xz-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-history',
        ),
    )

    packages['dev-libs/xml2-dev'].drain(
        'usr/lib64/xml2Conf.sh',
        'usr/lib64/cmake/libxml2/libxml2-config.cmake'
    )

    packages['dev-libs/xml2-doc'].drain(
        'usr/share/gtk-doc/'
    )

    return packages

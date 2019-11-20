#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools
from stdlib.template.configure import configure


def xslt_configure():
    stdlib.cmd('sed -i s/3000/5000/ libxslt/transform.c doc/xsltproc.{1,xml}')
    configure()


@manifest(
    name='libxslt',
    category='dev-libs',
    description='''
    XML stylesheet transformation library.
    ''',
    tags=['xml2', 'xml', 'xslt', 'libxslt'],
    maintainer='dorian.trubelle@epitech.eu',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='http://xmlsoft.org/XSLT/',  # XMLSoft's website does not support HTTPS
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.9.10',
            'fetch': [{
                'url': 'http://xmlsoft.org/sources/libxslt-1.1.34.tar.gz',  # XMLSoft's website does not support HTTPS
                'sha256': '98b1bd46d6792925ad2dfe9a87452ea2adebf69dcb9919ffd55bf926a7f93f7f',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/xml2-dev',
        'sys-libs/zlib-dev',
        'sys-apps/xz-dev'
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: xslt_configure(),
    )

    packages['dev-libs/libxslt'].drain('usr/lib64/xsltConf.sh')

    return packages
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='sqlite',
    category='dev-libs',
    description='''
    A C library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine.
    ''',
    tags=['sql', 'db'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.PUBLIC_DOMAIN],
    upstream_url='https://www.sqlite.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.30.1',
            'fetch': [{
                'url': 'https://sqlite.org/2019/sqlite-autoconf-3300100.tar.gz',
                'sha256': '8c5a50db089bd2a1b08dbc5b00d2027602ca7ff238ba7658fabca454d4298e60',
            }],
        },
    ],
)
def build(build):
    os.environ['CFLAGS'] += '''\
        -DSQLITE_ENABLE_FTS3=1            \
        -DSQLITE_ENABLE_FTS4=1            \
        -DSQLITE_ENABLE_COLUMN_METADATA=1 \
        -DSQLITE_ENABLE_UNLOCK_NOTIFY=1   \
        -DSQLITE_ENABLE_DBSTAT_VTAB=1     \
        -DSQLITE_SECURE_DELETE=1          \
        -DSQLITE_ENABLE_FTS3_TOKENIZER=1\
    '''

    return autotools.build(
        configure=lambda: configure(
            '--enable-fts5',
        )
    )

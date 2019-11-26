#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='pcre',
    category='dev-libs',
    description='''
    Perl Compatible Regular Expression libraries.
    ''',
    tags=['perl', 'regex', 'regular' 'expression'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://www.pcre.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.43.0',
            'fetch': [{
                    'url': 'https://ftp.pcre.org/pub/pcre/pcre-8.43.tar.bz2',
                    'sha256': '91e762520003013834ac1adb4a938d53b22a216341c061b0cf05603b290faf6b',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/zlib-dev',
        'sys-apps/bzip2-dev',
        'sys-libs/readline-dev',
    ],
)
def build(build):
    return autotools.build(
        configure=lambda: configure(
            '--enable-unicode-properties',
            '--enable-pcre16',
            '--enable-pcre32',
            '--enable-pcregrep-libz',
            '--enable-pcregrep-libbz2',
            '--enable-pcretest-libreadline',
        )
    )

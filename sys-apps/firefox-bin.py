#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.manifest import manifest
from stdlib.extract import extract_all
from stdlib.deplinker.elf import elf_deplinker
from stdlib.split.drain_all import drain_all_with_doc


def split_firefox():
    packages = drain_all_with_doc()

    packages['sys-apps/firefox-bin'].drain_build_cache(
        'firefox/*',
        'opt/firefox/',
    )

    packages['sys-apps/firefox-bin'].make_symlink('../firefox/firefox', 'opt/bin/firefox')

    return packages


@manifest(
    name='firefox-bin',
    category='sys-apps',
    description='''
    A web browser from Mozilla.
    ''',
    tags=['web', 'browser', 'mozilla'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL, stdlib.license.License.MOZILLA],
    upstream_url='https://www.mozilla.org/firefox/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '71.0.0',
            'fetch': [{
                    'url': 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/71.0/linux-x86_64/en-US/firefox-71.0.tar.bz2',
                    'sha256': 'a7fc7877926a6487ca7b1a342a832541e2c9070f94fc6cac362a0efd06ad0124',
                },
            ],
        },
    ],
)
def build(build):
    return basic.build(
        extract=extract_all,
        split=split_firefox,
        deplinker=lambda packages: elf_deplinker(
            packages,
            search_patterns=[
                'opt/firefox/**/*',
            ],
        )
    )

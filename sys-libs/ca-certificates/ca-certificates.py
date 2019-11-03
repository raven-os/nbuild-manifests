#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.template.make import make
from stdlib.manifest import manifest


@manifest(
    name='ca-certificates',
    category='sys-libs',
    description='''
    Common CA certificates, provided by Mozilla.
    ''',
    tags=['ca', 'certificates', 'mozilla', 'ssl', 'tls', 'security'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.MOZILLA],
    upstream_url='https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.20190110',
            'fetch': [{
                    'url': 'https://deb.debian.org/debian/pool/main/c/ca-certificates/ca-certificates_20190110.tar.xz',
                    'sha256': 'ee4bf0f4c6398005f5b5ca4e0b87b82837ac5c3b0280a1cb3a63c47555c3a675',
                },
            ],
        },
    ],
)
def build(build):

    packages = basic.build(
        compile=make,
    )

    # Drain certificates and binaries
    packages['sys-libs/ca-certificates'].drain_build_cache('mozilla/*.crt', 'usr/share/ca-certificates/mozilla/')
    packages['sys-libs/ca-certificates'].drain_build_cache('sbin/update-ca-certificates', 'usr/bin/update-ca-certificates')

    packages['sys-libs/ca-certificates'].load_instructions('./instructions.sh')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/ca-certificates'].requires('raven-os/corefs')
    packages['sys-libs/ca-certificates'].requires('sys-apps/bash')
    packages['sys-libs/ca-certificates'].requires('sys-apps/coreutils')
    packages['sys-libs/ca-certificates'].requires('sys-apps/findutils')
    packages['sys-libs/ca-certificates'].requires('sys-apps/sed')
    packages['sys-libs/ca-certificates'].requires('sys-libs/openssl')

    return packages

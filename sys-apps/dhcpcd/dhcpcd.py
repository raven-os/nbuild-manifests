#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='dhcpcd',
    category='sys-apps',
    description='''
    A DHCP client daemon compliant with RFC2131.
    ''',
    tags=['net', 'network', 'dhcp' 'rfc2131'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://roy.marples.name/projects/dhcpcd/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.0.3',
            'fetch': [{
                'url': 'https://roy.marples.name/downloads/dhcpcd/dhcpcd-8.0.3.tar.xz',
                'sha256': '9674971fcd5acd5a3401a0ad8eba7f0b816fec9abb4a2520332b4d8dae068f1d',
                }, {
                    'file': './dhcpcd.service',
                }
            ],
        },
    ],
    build_dependencies=[
        'sys-apps/systemd-dev',
    ]
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-static',
            '--without-static',
        ),
        install=lambda: make('install'),
        split=drain_all_with_doc,
    )

    # Drain the systemd daemon
    packages['sys-apps/dhcpcd'].drain_build_cache('dhcpcd.service', 'usr/lib64/systemd/system/')

    # Start the daemon when the dhcpcd is installed
    packages['sys-apps/dhcpcd'].load_instructions('./instructions.sh')

    return packages

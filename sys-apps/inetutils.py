#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='inetutils',
    category='sys-apps',
    description='''
    A collection of programms for basic networking.
    ''',
    tags=['gnu', 'network', 'util'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='http://www.gnu.org/software/inetutils/,',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.9.4',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/inetutils/inetutils-1.9.4.tar.xz',
                    'sha256': '849d96f136effdef69548a940e3e0ec0624fc0c81265296987986a0dd36ded37',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--disable-logger',
            '--disable-whois',
            '--disable-rcp',
            '--disable-rexec',
            '--disable-rlogin',
            '--disable-rsh',
            '--disable-servers',
        ),
        check=None,  # TODO FIXME: Tests are looping indefinitely
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/inetutils'].rdepends_on('raven-os/corefs', '*')

    return packages

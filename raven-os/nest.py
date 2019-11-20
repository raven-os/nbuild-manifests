#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from textwrap import dedent
from stdlib.template import cargo
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all_with_doc


@manifest(
    name='nest',
    category='raven-os',
    description='''
    Raven's package manager
    ''',
    tags=['nest', 'package', 'manager', 'raven', 'raven-os'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://www.rust-lang.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.0.216',
            'fetch': [{
                'git': 'https://github.com/raven-os/nest.git',
                'commit': 'd2d2d4b9cbb729172b94d2214bb2a18e0c918ec3',
            }]
        },
    ],
    build_dependencies=[
        'dev-lang/rust',
        'sys-libs/openssl-dev',
    ],
)
def build(build):
    packages = cargo.build(
        build=None,  # Let cargo install do the build
        check=None,  # We do not support Nest's unit test for now. (TODO FIXME)
        install=lambda: cargo.cargo_install(
            path='./nest-cli',
        ),
        split=drain_all_with_doc,
    )

    # Move all binaries to usr/bin/
    packages['raven-os/nest'].move('bin/*', 'usr/bin/')

    with stdlib.pushd(packages['raven-os/nest'].wrap_cache):
        os.makedirs('etc/nest/')
        with open('etc/nest/config.toml', 'w') as config:
            config.write(dedent('''\
            #
            # Raven-OS - /etc/nest/config.toml
            # Default configuration file for Nest.
            #

            repositories_order = ["beta"]

            # Stable repository (uncomment to enable)
            # [repositories.stable]
            # mirrors = ["https://stable.raven-os.org"]

            # Beta repository
            [repositories.beta]
            mirrors = ["https://beta.raven-os.org"]

            # Unstable repository (uncomment to enable)
            # [repositories.unstable]
            # mirrors = ["https://unstable.raven-os.org"]
            '''))

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['raven-os/nest'].requires('raven-os/corefs')

    return packages

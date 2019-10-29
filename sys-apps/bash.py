#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.template.configure import configure


def check_bash():
    # Run the bash tests as a non-privileged user
    stdlib.cmd('chown -Rv nobody .')
    stdlib.cmd('su nobody -s /bin/bash -c "PATH=$PATH HOME=/home make tests"', fail_ok=True)


@manifest(
    name='bash',
    category='sys-apps',
    description='''
    The GNU Bourne Again shell.
    ''',
    tags=['gnu', 'shell', 'sh'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://www.gnu.org/software/bash/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.0.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/bash/bash-5.0.tar.gz',
                    'sha256': 'b4a80f2ac66170b2913efbfb9f2594f1f76c7b1afd11f799e22035d63077fb4d',
                },
            ],
        },
    ],
)
def build(build):

    packages = autotools.build(
        configure=lambda: configure(
            '--with-curses',
            '--without-bash-malloc',
            '--with-installed-readline',
        ),
        check=check_bash,
    )

    # Drain the given builtins.
    packages['sys-apps/bash'].drain('usr/lib64/bash/')

    # Make the `sh` symlink for retro-compatibility reasons.
    packages['sys-apps/bash'].make_symlink('bash', 'usr/bin/sh')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/bash'].rdepends_on('raven-os/corefs', '*')

    return packages

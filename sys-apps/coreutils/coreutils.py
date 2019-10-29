#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


def patch_coreutils():
    stdlib.patch.patch_all()

    # Suppress a test which on some machines can loop forever:
    stdlib.cmd("sed -i '/test.lock/s/^/#/' gnulib-tests/gnulib.mk")


def configure_coreutils():
    with stdlib.pushenv():
        os.environ['FORCE_UNSAFE_CONFIGURE'] = '1'

        stdlib.cmd('autoreconf -fiv')

        configure(
            '--enable-no-install-program=kill,uptime'  # Installed by other packages
        )


def check_coreutils():
    make('NON_ROOT_USERNAME=nobody', 'check-root')

    # Fix some permissions so that the non-root user can compile and run the tests
    stdlib.cmd('chown -Rv nobody .')

    stdlib.cmd('su nobody -s /bin/bash -c "PATH=$PATH make RUN_EXPENSIVE_TESTS=yes check"', fail_ok=True)


@manifest(
    name='coreutils',
    category='sys-apps',
    description='''
    Utilities for showing and setting the basic system characteristics.
    ''',
    tags=['system', 'administration', 'sysadmin', 'utilities'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/coreutils/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.31.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/coreutils/coreutils-8.31.tar.xz',
                    'sha256': 'ff7a9c918edce6b4f4b2725e3f9b37b0c4d193531cac49a48b56c4d0d3a9e9fd',
                }, {
                    'file': './coreutils-8.31-i18n-1.patch',
                }
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_coreutils,
        configure=configure_coreutils,
        check=check_coreutils,
        split=drain_all_with_doc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/coreutils'].rdepends_on('raven-os/corefs', '*')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


def check_util_linux():
    # Run the tests as the 'nobody' user.
    stdlib.cmd('chown -Rv nobody .')
    stdlib.cmd('su nobody -s /bin/bash -c "PATH=$PATH make -k check"')


@manifest(
    name='util-linux',
    category='sys-apps',
    description='''
    A bunch of miscellaneous utility programs for handling file systems, consoles, partitions, messages, etc.
    ''',
    tags=['linux', 'utility', 'filesystem', 'partition', 'message'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='http://freecode.com/projects/util-linux',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.34.0',
            'fetch': [{
                    'url': 'https://www.kernel.org/pub/linux/utils/util-linux/v2.34/util-linux-2.34.tar.xz',
                    'sha256': '743f9d0c7252b6db246b659c1e1ce0bd45d8d4508b4dfa427bbb4a3e9b9f62b5',
                },
            ],
        },
    ],
)
def build(build):

    # The FHS recommends using the /var/lib/hwclock directory instead of the usual /etc directory as the location for the adjtime file
    os.environ['ADJTIME_PATH'] = '/var/lib/hwclock/adjtime'

    packages = autotools.build(
        configure=lambda: configure(
            '--disable-chfn-chsh',
            '--disable-login',
            '--disable-nologin',
            '--disable-su',
            '--disable-setpriv',
            '--disable-runuser',
            '--disable-pylibmount',
            '--disable-static',
            '--without-python',
        ),
        check=check_util_linux,
    )

    # Remove the dependencie on systemd to avoid a circular dependency (TODO FIXME)
    del packages['sys-apps/util-linux'].run_dependencies['beta::sys-apps/systemd']

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/util-linux'].requires('raven-os/corefs')

    return packages

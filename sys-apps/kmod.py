#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


def split_kmod():
    packages = stdlib.split.system.system()

    # Create a bunch of symlinks to binaries that previously handled kernel modules, as a way to provide compatibility
    # with Module-Init-Tools.
    for target in ['depmod', 'insmod', 'lsmod', 'modinfo', 'modprobe', 'rmmod']:
        packages['sys-apps/kmod'].make_symlink('kmod', f'usr/bin/{target}')

    return packages


@manifest(
    name='kmod',
    category='sys-apps',
    description='''
    Libraries and utilities for loading kernel modules.
    ''',
    tags=['kernel', 'modules'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://git.kernel.org/pub/scm/utils/kernel/kmod/kmod.git',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '26.0.0',
            'fetch': [{
                    'url': 'https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-26.tar.xz',
                    'sha256': '57bb22c8bb56435991f6b0810a042b0a65e2f1e217551efa58235b7034cdbb9d',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-xz',
            '--with-zlib',
            '--disable-static',  # --enable-static isn't supported by kmod.
        ),
        split=split_kmod,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/kmod'].rdepends_on('raven-os/corefs', '*')

    return packages

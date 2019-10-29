#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import glob
import stdlib
from stdlib.template.configure import configure
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libcap',
    category='sys-libs',
    description='''
    A library that provides user-space interfaces to the POSIX capabilities available in the Linux kernel,
    which are a partitioning of the all powerful root privilege into a set of distinct privileges.
    ''',
    tags=['gnu', 'capabilities', 'privilege', 'security', 'root'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://sites.google.com/site/fullycapable/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.27.0',
            'fetch': [{
                    'url': 'https://git.kernel.org/pub/scm/libs/libcap/libcap.git/snapshot/libcap-2.27.tar.gz',
                    'sha256': '5328e950819e64c2036a67af1d62035ffe7954f8e1ba44bdf2833a13998259e9',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=None,
        install=lambda: make('RAISE_SETFCAP=no', 'prefix=/usr', f'DESTDIR={build.install_cache}/', 'install'),
    )

    # Fix some permissions
    with stdlib.pushd(packages['sys-libs/libcap'].wrap_cache):
        for lib in glob.glob('usr/lib/libcap.so.*'):
            os.chmod(lib, 0o755)

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/libcap'].rdepends_on('raven-os/corefs', '*')

    return packages

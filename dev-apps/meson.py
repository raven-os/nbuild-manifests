#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.split.drain_all import drain_all
from stdlib.manifest import manifest


@manifest(
    name='meson',
    category='dev-apps',
    description='''
    A fast, user friendly build system.
    ''',
    tags=['build', 'system'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.APACHE],
    upstream_url='https://mesonbuild.com/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.51.1',
            'fetch': [{
                    'url': 'https://github.com/mesonbuild/meson/releases/download/0.51.1/meson-0.51.1.tar.gz',
                    'sha256': 'f27b7a60f339ba66fe4b8f81f0d1072e090a08eabbd6aa287683b2c2b9dd2d82',
                },
            ],
        },
    ],
)
def build(build):
    packages = basic.build(
        compile=lambda: stdlib.cmd('python3 setup.py build'),
        install=lambda: stdlib.cmd(f'python3 setup.py install --root={build.install_cache}'),
        split=drain_all,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/meson'].requires('raven-os/corefs')

    return packages

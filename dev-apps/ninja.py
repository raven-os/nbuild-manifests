#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.split.drain_all import drain_all
from stdlib.template import basic
from stdlib.manifest import manifest


def split_ninja():
    packages = drain_all()

    packages['dev-apps/ninja'].drain_build_cache('ninja', 'usr/bin/')
    packages['dev-apps/ninja'].drain_build_cache('misc/bash-completion', 'usr/share/bash-completion/completions/ninja')
    packages['dev-apps/ninja'].drain_build_cache('misc/zsh-completion', 'usr/share/zsh/site-functions/_ninja')

    return packages


@manifest(
    name='ninja',
    category='dev-apps',
    description='''
    A small build system with a focus on speed.
    ''',
    tags=['build', 'system'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.APACHE],
    upstream_url='https://ninja-build.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.9.0',
            'fetch': [{
                    'url': 'https://github.com/ninja-build/ninja/archive/v1.9.0.tar.gz',
                    'sha256': '5d7ec75828f8d3fd1a0c2f31b5b0cea780cdfe1031359228c428c1a48bfcd5b9',
                },
            ],
        },
    ],
)
def build(build):
    packages = basic.build(
        compile=lambda: stdlib.cmd('python3 configure.py --bootstrap'),
        check=lambda: stdlib.cmd('./ninja ninja_test && ./ninja_test --gtest_filter=-SubprocessTest.SetWithLots'),
        split=split_ninja,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-apps/ninja'].rdepends_on('raven-os/corefs', '*')

    return packages

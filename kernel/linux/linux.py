#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import shutil
import stdlib
import stdlib.build
import stdlib.split.system
from stdlib.template import autotools
from stdlib.template.make import make
from stdlib.manifest import manifest


def install_linux():
    build = stdlib.build.current_build()

    boot_dir = os.path.join(build.install_cache, 'boot')
    modules_dir = os.path.join(build.install_cache, 'usr')
    include_dir = os.path.join(build.install_cache, 'usr')

    os.makedirs(boot_dir, exist_ok=True)
    os.makedirs(modules_dir, exist_ok=True)
    os.makedirs(include_dir, exist_ok=True)

    # make(f'INSTALL_PATH={boot_dir}', 'install')
    # make(f'INSTALL_MOD_PATH={modules_dir}', 'modules_install')
    make(f'INSTALL_HDR_PATH={include_dir}', 'headers_install')

    # Remove useless files
    with stdlib.pushd(build.install_cache):
        stdlib.cmd(f'find . \\( -name .install -o -name ..install.cmd \\) -delete')


@manifest(
    name='linux',
    category='kernel',
    description='''
    The Linux kernel.
    ''',
    tags=['linux', 'kernel'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.License.GPL_V2],
    upstream_url='https://www.kernel.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '4.19.49',
            'fetch': [{
                    'url': 'https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.49.tar.xz',
                    'sha256': '92d920b3973c0dbca5516271afa405be6e5822a9b831df8c085f9c9eb838bbcd',
                }, {
                    'file': './config',
                    'rename': '.config',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=None,  # lambda: make('olddefconfig'),
        check=None,
        compile=None,
        install=install_linux,
    )

    # Drain documentation
    # packages['kernel/linux-doc'].drain_build_cache('Documentation/*', 'usr/doc/linux/')

    # Remove the dependency of `kernel/linux-dev` to `kernel/linux`
    packages['kernel/linux-dev'].run_dependencies = dict()

    # Change the description of kernel/linux-dev
    packages['kernel/linux-dev'].description = 'Headers to compile or write software based on the Linux kernel.'

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['kernel/linux'].rdepends_on('raven-os/corefs', '*')

    return packages

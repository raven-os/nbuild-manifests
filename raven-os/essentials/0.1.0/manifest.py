#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Build manifest for the `essential` and `essential-dev` package.
They are virtual packages over the bare-bones essentials packages needed for
a bootable and stable system.
"""

from textwrap import dedent
from nbuild.stdenv.package import package
from nbuild.stdenv.build import current_build


@package(
    id=f'stable::raven-os/essentials#0.1.0',
    description='Core packages needed for a bootable and stable system.',
    run_dependencies={
        'stable::kernel/linux': '*',
        'stable::raven-os/corefs': '*',
        # TODO -- Add essentials packages here
    },
)
def build_essentials():
    package = current_build().current_package

    # Hacky way of making a virtual package until nest and nbuild fully
    # support them
    open(f'{package.install_dir}/.essentials.nestkeep', 'w+')


@package(
    id=f'stable::raven-os/essentials-dev#0.1.0',
    description=dedent('''
        Headers and manuals needed to write or compile softwares
        based on any core libraries.
    '''),
    run_dependencies={
        # TODO -- Add essentials packages here
    },
)
def build_essentials_dev():
    package = current_build().current_package

    # Hacky way of making a virtual package until nest and nbuild fully
    # support them
    open(f'{package.install_dir}/.essentials-dev.nestkeep', 'w+')


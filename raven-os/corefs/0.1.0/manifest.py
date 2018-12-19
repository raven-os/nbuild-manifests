#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Build manifest for the 'corefs' package.
The corefs package contains the basic filesystem of Raven-OS.
"""

from textwrap import dedent
from nbuild.stdenv.package import package
from nbuild.stdenv.install import make_keeper, make_symlink


@package(
    id=f'stable::raven-os/corefs#0.1.0',
    description=dedent('''
        Provides the core filesystem hierarchy for a fresh Raven-OS
        installation.
    ''')
)
def build_essentials():
    # / hierarchy
    make_keeper('/bin')
    make_keeper('/boot')
    make_keeper('/dev')
    make_keeper('/etc')
    make_keeper('/home')
    make_keeper('/lib32')
    make_keeper('/lib64')
    make_symlink('/lib64', '/lib')
    make_keeper('/media')
    make_keeper('/mnt')
    make_keeper('/opt')
    make_keeper('/root')
    make_keeper('/run')
    make_keeper('/sbin')
    make_keeper('/srv')
    make_keeper('/tmp')
    make_keeper('/usr')
    make_keeper('/var')

    # /etc hierarchy
    make_keeper('/etc/opt')

    # /lib hierarchy
    make_keeper('/lib64/modules')

    # /media hierarchy
    make_keeper('/media/floppy')
    make_keeper('/media/cdrom')
    make_keeper('/media/cdrecorder')
    make_keeper('/media/zip')

    # /usr hierarchy
    make_keeper('/usr/bin')
    make_keeper('/usr/games')
    make_keeper('/usr/include')
    make_keeper('/usr/lib64')
    make_keeper('/usr/lib32')
    make_symlink('/usr/lib64', '/usr/lib')
    make_keeper('/usr/libexec')
    make_keeper('/usr/local')
    make_keeper('/usr/sbin')
    make_keeper('/usr/share')
    make_keeper('/usr/src')
    make_symlink('/var/tmp', '/usr/tmp')

    # /usr/local hierarchy
    make_keeper('/usr/local/bin')
    make_keeper('/usr/local/etc')
    make_keeper('/usr/local/games')
    make_keeper('/usr/local/include')
    make_keeper('/usr/local/lib64')
    make_keeper('/usr/local/lib32')
    make_symlink('/usr/local/lib64', '/usr/local/lib')
    make_keeper('/usr/local/man')
    make_keeper('/usr/local/sbin')
    make_keeper('/usr/local/share')
    make_keeper('/usr/local/src')

    # /usr/share hierarchy
    make_keeper('/usr/share')
    make_keeper('/usr/src')

    # /var hierarchy
    make_symlink('/run', '/var/run')

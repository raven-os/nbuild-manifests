#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import stdlib.package
from stdlib.manifest import manifest


@manifest(
    name='corefs',
    category='raven-os',
    description='''
    The core filesystem hierarchy of a stable Raven-OS system.
    ''',
    tags=['raven-os'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://raven-os.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.0',
        },
    ],
)
def build(build):
    corefs = stdlib.package.Package(
        stdlib.package.PackageID('corefs')
    )

    # / hierarchy
    corefs.make_keepers(
        'boot',
        'dev',
        'etc',
        'home',
        'media',
        'mnt',
        'opt',
        'proc',
        'root',
        'run',
        'srv',
        'sys',
        'tmp',
        'usr',
        'var',
    )
    corefs.make_symlink('usr/lib64', 'lib')
    corefs.make_symlink('usr/lib64', 'lib64')
    corefs.make_symlink('usr/lib32', 'lib32')
    corefs.make_symlink('usr/bin', 'bin')
    corefs.make_symlink('usr/bin', 'sbin')

    # /media hierarchy
    corefs.make_keepers(
        'media/floppy',
        'media/cdrom',
        'media/cdrecorder',
        'media/zip',
    )

    # /usr hierarchy
    corefs.make_keepers(
        'usr/bin',
        'usr/games',
        'usr/include',
        'usr/lib64',
        'usr/lib32',
        'usr/libexec',
        'usr/local',
        'usr/share',
        'usr/src',
    )
    corefs.make_symlink('lib64', 'usr/lib')
    corefs.make_symlink('bin', 'usr/sbin')
    corefs.make_symlink('../var/tmp', 'usr/tmp')

    # /usr/lib hierarchy
    corefs.make_keepers('usr/lib64/modules')

    # /usr/local hierarchy
    corefs.make_keepers(
        'usr/local/bin',
        'usr/local/etc',
        'usr/local/games',
        'usr/local/include',
        'usr/local/lib64',
        'usr/local/lib32',
        'usr/local/man',
        'usr/local/share',
        'usr/local/src',
    )
    corefs.make_symlink('lib64', 'usr/local/lib')
    corefs.make_symlink('bin', 'usr/local/sbin')

    # /usr/share hierarchy
    corefs.make_keepers(
        'usr/share',
        'usr/src',
    )

    # /var hierarchy
    corefs.make_keepers(
        'var/tmp'
    )
    corefs.make_symlink('../run', 'var/run')

    # Change permission of /root, /tmp and /var/tmp
    with stdlib.pushd(corefs.wrap_cache):
        os.chmod('root', 0o700)
        os.chmod('tmp', 0o1777)
        os.chmod('var/tmp', 0o1777)

    return {
        corefs.id.full_name(): corefs
    }

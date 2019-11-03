#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import stdlib.package
from textwrap import dedent
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

    with stdlib.pushd(corefs.wrap_cache):

        # Change permission of /root, /tmp and /var/tmp
        os.chmod('root', 0o700)
        os.chmod('tmp', 0o1777)
        os.chmod('var/tmp', 0o1777)

        # Write a default etc/passwd
        with open('etc/passwd', 'w+') as passwd:
            passwd.write(dedent('''\
            root:x:0:0:root:/root:/bin/bash
            nobody:x:65534:65534:nobody:/var/empty:/bin/false
            '''))

        # Write a default etc/group
        with open('etc/group', 'w+') as group:
            group.write(dedent('''\
            root:x:0:
            bin:x:1:
            sys:x:2:
            kmem:x:3:
            tty:x:4:
            tape:x:5:
            daemon:x:6:
            floppy:x:7:
            disk:x:8:
            lp:x:9:
            dialout:x:10:
            audio:x:11:
            video:x:12:
            utmp:x:13:
            usb:x:14:
            wheel:x:15:
            users:x:999:
            '''))

        # Write a default etc/shells
        with open('etc/shells', 'w+') as shells:
            shells.write(dedent('''\
            #
            # Raven-OS - /etc/shells
            #   - Valid login shells -
            #

            /bin/bash
            /bin/csh
            /bin/dash
            /bin/esh
            /bin/fish
            /bin/ksh
            /bin/mksh
            /bin/sash
            /bin/sh
            /bin/tcsh
            /bin/zsh
            '''))

        # Write a default etc/hosts
        with open('etc/hosts', 'w+') as hosts:
            hosts.write(dedent('''\
            #
            # Raven-OS - /etc/hosts
            #

            # IPv4 and IPv6 localhost aliases
            127.0.0.1	localhost.localdomain localhost
            ::1		localhost.localdomain localhost

            '''))

        # Write a default etc/hostname
        with open('etc/hostname', 'w+') as hostname:
            hostname.write(dedent('''\
            raven-os
            '''))

        # Write a default etc/resolv.conf
        with open('etc/resolv.conf', 'w+') as resolv:
            resolv.write(dedent('''\
            #
            # Raven-OS - /etc/resolv.conf
            #

            nameserver 8.8.8.8
            nameserver 8.8.4.4
            '''))

        # Write a default etc/os-release
        with open('etc/os-release', 'w+') as resolv:
            resolv.write(dedent('''\
            #
            # Raven-OS - /etc/os-release
            #

            ID="raven-os"
            NAME="Raven-OS"
            HOME_URL="https://raven-os.org/"
            SUPPORT_URL="https://github.com/raven-os/iso/issues/"
            BUG_REPORT_URL="https://github.com/raven-os/iso/issues/"
            '''))

        # Write a default etc/raven-os-release
        with open('etc/raven-os-release', 'w+') as resolv:
            resolv.write(dedent('''\
            #
            # Raven-OS - /etc/raven-os-release
            #
            Raven-OS release 0.1.0 (Beta)
            '''))

        # Write a default etc/issue
        with open('etc/issue', 'w+') as resolv:
            resolv.write(dedent('''\
            #
            # Raven-OS - /etc/issue
            #
            Welcome to Raven-OS!
            '''))

    return {
        corefs.id.short_name(): corefs
    }

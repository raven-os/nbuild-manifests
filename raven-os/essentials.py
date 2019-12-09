#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest
from textwrap import dedent


@manifest(
    name='essentials',
    category='raven-os',
    description='''
    Core packages needed for a stable Raven-OS system.
    ''',
    tags=['raven-os'],
    maintainer='grange_c@raven-os.org',
    licenses=[],
    upstream_url='https://raven-os.org/',
    kind=stdlib.kind.Kind.VIRTUAL,
    versions_data=[
        {
            'semver': '1.0.0',
        },
    ],
)
def build(build):
    essentials = stdlib.package.Package(
        stdlib.package.PackageID('essentials')
    )

    dev = stdlib.package.Package(
        stdlib.package.PackageID('essentials-dev'),
        description='Core packages needed for most system development needs.',
    )

    boot = stdlib.package.Package(
        stdlib.package.PackageID('essentials-bootable'),
        description='Core packages needed for a stable and bootable Raven-OS system.',
    )

    # Essentials dependencies

    essentials.requires('raven-os/corefs')
    essentials.requires('sys-apps/xz')
    essentials.requires('sys-apps/groff')
    essentials.requires('sys-apps/shadow-dev')
    essentials.requires('sys-apps/man-pages')
    essentials.requires('sys-apps/gzip')
    essentials.requires('sys-apps/shadow')
    essentials.requires('sys-apps/attr')
    essentials.requires('sys-apps/bash')
    essentials.requires('sys-apps/tar')
    essentials.requires('sys-apps/grep')
    essentials.requires('sys-apps/util-linux')
    essentials.requires('sys-apps/findutils')
    essentials.requires('sys-apps/procps')
    essentials.requires('sys-apps/coreutils')
    essentials.requires('sys-apps/diffutils')
    essentials.requires('sys-apps/which')
    essentials.requires('sys-apps/acl')
    essentials.requires('sys-apps/pkg-config')
    essentials.requires('sys-apps/sed')
    essentials.requires('sys-apps/bzip2')
    essentials.requires('sys-apps/gawk')
    essentials.requires('sys-apps/grub')
    essentials.requires('sys-apps/dbus')
    essentials.requires('sys-apps/kbd')
    essentials.requires('sys-apps/file')
    essentials.requires('sys-apps/kmod')
    essentials.requires('sys-apps/less')
    essentials.requires('sys-apps/man-db')
    essentials.requires('sys-apps/inetutils')
    essentials.requires('sys-apps/e2fsprogs')
    essentials.requires('sys-apps/psmisc')
    essentials.requires('dev-lang/python')
    essentials.requires('dev-lang/perl')
    essentials.requires('sys-libs/iana-etc')
    essentials.requires('sys-libs/ca-certificates')
    essentials.requires('raven-os/nest')

    # Essentials-dev dependencies

    dev.depends_on(essentials)
    dev.requires('dev-apps/gcc')
    dev.requires('dev-apps/g++')
    dev.requires('dev-apps/autoconf')
    dev.requires('dev-apps/automake')
    dev.requires('dev-apps/binutils')
    dev.requires('dev-apps/elfutils')
    dev.requires('dev-apps/gettext')
    dev.requires('dev-apps/git')
    dev.requires('dev-apps/intltool')
    dev.requires('dev-apps/m4')
    dev.requires('dev-apps/make')
    dev.requires('dev-apps/meson')
    dev.requires('dev-apps/bison')
    dev.requires('dev-apps/patch')
    dev.requires('dev-python/pip')
    dev.requires('kernel/linux-dev')
    dev.requires('sys-libs/glibc-dev')
    dev.requires('dev-libs/libffi-dev')

    # Essentials-bootable dependencies

    # Mandatory packages to make a system bootable
    boot.requires('kernel/linux')
    boot.requires('sys-apps/grub')
    boot.requires('sys-apps/systemd')
    boot.requires('sys-apps/feathers')
    boot.requires('sys-apps/dmenu-wl')
    boot.requires('ui-resources/dejavu')
    boot.requires('sys-libs/dhcpcd')
    boot.depends_on(essentials)

    # Convenient packages to make Raven-OS smoother to use.
    boot.requires('editor/vim')  # TODO FIXME Switch to nano when packaged
    boot.requires('sys-apps/curl')

    return {
        essentials.id.short_name(): essentials,
        dev.id.short_name(): dev,
        boot.id.short_name(): boot,
    }

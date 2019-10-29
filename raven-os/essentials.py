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

    devel = stdlib.package.Package(
        stdlib.package.PackageID('essentials-dev')
    )

    # Essentials dependencies

    essentials.rdepends_on('raven-os/corefs', '*')
    essentials.rdepends_on('sys-apps/xz', '*')
    essentials.rdepends_on('sys-apps/groff', '*')
    essentials.rdepends_on('sys-apps/shadow-dev', '*')
    essentials.rdepends_on('sys-apps/systemd', '*')
    essentials.rdepends_on('sys-apps/man-pages', '*')
    essentials.rdepends_on('sys-apps/gzip', '*')
    essentials.rdepends_on('sys-apps/shadow', '*')
    essentials.rdepends_on('sys-apps/attr', '*')
    essentials.rdepends_on('sys-apps/bash', '*')
    essentials.rdepends_on('sys-apps/tar', '*')
    essentials.rdepends_on('sys-apps/grep', '*')
    essentials.rdepends_on('sys-apps/util-linux', '*')
    essentials.rdepends_on('sys-apps/findutils', '*')
    essentials.rdepends_on('sys-apps/procps', '*')
    essentials.rdepends_on('sys-apps/coreutils', '*')
    essentials.rdepends_on('sys-apps/diffutils', '*')
    essentials.rdepends_on('sys-apps/acl', '*')
    essentials.rdepends_on('sys-apps/pkg-config', '*')
    essentials.rdepends_on('sys-apps/sed', '*')
    essentials.rdepends_on('sys-apps/bzip2', '*')
    essentials.rdepends_on('sys-apps/gawk', '*')
    essentials.rdepends_on('sys-apps/grub', '*')
    essentials.rdepends_on('sys-apps/dbus', '*')
    essentials.rdepends_on('sys-apps/kbd', '*')
    essentials.rdepends_on('sys-apps/file', '*')
    essentials.rdepends_on('sys-apps/kmod', '*')
    essentials.rdepends_on('sys-apps/less', '*')
    essentials.rdepends_on('sys-apps/man-db', '*')
    essentials.rdepends_on('sys-apps/inetutils', '*')
    essentials.rdepends_on('sys-apps/e2fsprogs', '*')
    essentials.rdepends_on('sys-apps/psmisc', '*')
    essentials.rdepends_on('sys-apps/curl', '*')
    essentials.rdepends_on('dev-lang/python', '*')
    essentials.rdepends_on('dev-lang/perl', '*')
    essentials.rdepends_on('editor/vim', '*')

    # Essentials-Devel dependencies

    devel.depends_on(essentials)

    # TODO FIXME: Add more dependencies to essentials-dev

    return {
        essentials.id.full_name(): essentials,
        devel.id.full_name(): devel,
    }

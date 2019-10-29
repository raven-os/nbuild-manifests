#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
import stdlib.patch
import stdlib.split.system
import stdlib.deplinker.elf
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import basic
from stdlib.manifest import manifest


def extract_systemd():
    stdlib.extract.flat_extract(glob.glob('systemd-2*.tar.*')[0])
    stdlib.extract.extract(glob.glob('systemd-man-pages-2*.tar.*')[0])


def patch_systemd():
    stdlib.patch.patch_all()

    # Remove tests that cannot be built in chroot
    stdlib.cmd("sed '177,$ d' -i src/resolve/meson.build")

    # Remove an unneeded group, render, from the default udev rules:
    stdlib.cmd("""sed -i 's/GROUP="render", //' rules/50-udev-default.rules.in""")


def split_systemd():
    packages = stdlib.split.system.system()

    packages['sys-apps/systemd'].drain(
        'usr/share/',
        '{,usr/}lib/',
    )

    packages['sys-apps/systemd'].drain_package(
        packages['sys-apps/systemd-dev'],
        'usr/lib64/systemd/libsystemd-shared-*.so',
    )

    return packages


@manifest(
    name='systemd',
    category='sys-apps',
    description='''
    A bunch of programs and utilities for controlling the startup, running and shutdown of the system.
    ''',
    tags=['init', 'boot', 'startup', 'daemon', 'journal', 'system', 'log', 'logging'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2, stdlib.license.License.LGPL_V2_1],
    upstream_url='https://www.freedesktop.org/wiki/Software/systemd/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '241.0.0',
            'fetch': [{
                    'url': 'https://github.com/systemd/systemd/archive/v241/systemd-241.tar.gz',
                    'sha256': 'b2561a8e1d10a2c248253f0dda31a85dd6d69f2b54177de55e02cd1d2778316e',
                }, {
                    'url': 'http://anduin.linuxfromscratch.org/LFS/systemd-man-pages-241.tar.xz',
                    'sha256': 'd545660f50e5c56a331f67bc7a91a62b565e9db18e6152ebb982b3a1a412c748',
                }, {
                    'file': './systemd-241-networkd_and_rdrand_fixes-1.patch',
                }
            ],
        },
    ],
)
def build(build):

    os.environ['PKG_CONFIG_PATH'] = '/usr/lib/pkgconfig:/tools/lib/pkgconfig'  # TODO FIXME
    os.environ['LANG'] = 'en_US.UTF-8'

    packages = basic.build(
        build_folder='build',
        extract=extract_systemd,
        patch=patch_systemd,
        configure=lambda: stdlib.cmd('''meson \
            --prefix=/usr                   \
            --sysconfdir=/etc               \
            --localstatedir=/var            \
            -Dblkid=true                    \
            -Dbuildtype=release             \
            -Ddefault-dnssec=no             \
            -Dfirstboot=false               \
            -Dinstall-tests=false           \
            -Dkmod-path=/usr/bin/kmod       \
            -Dldconfig=false                \
            -Dmount-path=/usr/bin/mount     \
            -Drootprefix=                   \
            -Drootlibdir=/usr/lib           \
            -Dsplit-usr=true                \
            -Dsulogin-path=/usr/bin/sulogin \
            -Dsysusers=false                \
            -Dumount-path=/usr/bin/umount   \
            -Db_lto=false                   \
            -Drpmmacrosdir=no               \
            ..
        '''),
        compile=lambda: stdlib.cmd('ninja'),
        install=lambda: stdlib.cmd('ninja install'),
        split=split_systemd,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/systemd'].rdepends_on('raven-os/corefs', '*')

    packages['sys-apps/systemd'].rdepends_on('sys-apps/shadow', '*')

    packages['sys-apps/systemd'].load_instructions('./instructions.sh')

    return packages

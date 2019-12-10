#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
import textwrap
import stdlib.patch
import stdlib.split.system
import stdlib.deplinker.elf
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template.ninja import ninja_test
from stdlib.template.meson import meson
from stdlib.template import meson_ninja
from stdlib.manifest import manifest


def extract_systemd():
    stdlib.extract.flat_extract(glob.glob('systemd-2*.tar.*')[0])
    stdlib.extract.extract(glob.glob('systemd-man-pages-2*.tar.*')[0])


def patch_systemd():
    stdlib.patch.patch_all()

    # Fix an incompatibility with the latest version of libseccomp:
    stdlib.cmd(r"""sed -i '1506,1508 s/</>/' src/shared/seccomp-util.c""")

    # Remove an unneeded group, render, from the default udev rules:
    stdlib.cmd(r"""sed -i 's/GROUP="render", //' rules/50-udev-default.rules.in""")


def split_systemd():
    packages = stdlib.split.system.system()

    packages['sys-apps/systemd'].drain(
        'usr/share/',
        '{,usr/}lib/',
    )

    packages['sys-apps/systemd'].drain_package(
        packages['sys-apps/systemd-dev'],
        'usr/lib64/systemd/libsystemd-shared-*.so',
        'usr/lib/systemd/*.so',
        'usr/lib64/security/*.so',
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
    build_dependencies=[
        'kernel/linux-dev',
        'dev-apps/ninja',
        'dev-libs/glib-dev',
        'dev-libs/libxkbcommon-dev',
        'dev-libs/pcre-dev',
        'sys-apps/dbus-dev',
        'sys-apps/shadow-dev',
        'sys-apps/bzip2-dev',
        'sys-apps/xz-dev',
        'sys-apps/util-linux-dev',
        'sys-apps/acl-dev',
        'sys-apps/kmod-dev',
        'sys-apps/curl-dev',
        'sys-libs/gperf',
        'sys-libs/pam-dev',
        'sys-libs/libcap-dev',
        'sys-libs/openssl-dev',
        'sys-libs/zlib-dev',
    ],
)
def build(build):
    packages = meson_ninja.build(
        build_folder='build',
        extract=extract_systemd,
        patch=patch_systemd,
        configure=lambda: meson(
            '-Dblkid=true',
            '-Ddefault-dnssec=no',
            '-Dfirstboot=false',
            '-Dinstall-tests=false',
            '-Dkmod-path=/usr/bin/kmod',
            '-Dldconfig=false',
            '-Dmount-path=/usr/bin/mount',
            '-Drootprefix=',
            '-Drootlibdir=/usr/lib64',
            '-Dsulogin-path=/usr/bin/sulogin',
            '-Dsysusers=false',
            '-Dumount-path=/usr/bin/umount',
            '-Db_lto=false',
            '-Drpmmacrosdir=no',
            '-Dgnutls=false',
            '..',
        ),
        check=lambda: ninja_test(fail_ok=True),
        split=split_systemd,
    )

    # Write a default configuration file for PAM
    with stdlib.pushd(packages['sys-apps/systemd'].wrap_cache):
        os.makedirs('etc/pam.d/', exist_ok=True)

        with open('etc/pam.d/systemd-user', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/systemd-user
            #

            account  required    pam_access.so
            account  include     system-account

            session  required    pam_env.so
            session  required    pam_limits.so
            session  required    pam_unix.so
            session  required    pam_loginuid.so
            session  optional    pam_keyinit.so force revoke
            session  optional    pam_systemd.so

            auth     required    pam_deny.so
            password required    pam_deny.so
            '''))

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-apps/systemd'].requires('raven-os/corefs')
    packages['sys-apps/systemd'].requires('sys-apps/shadow')
    packages['sys-apps/systemd'].requires('sys-apps/bash')
    packages['sys-apps/systemd'].requires('sys-apps/coreutils')
    packages['sys-apps/systemd'].requires('sys-apps/sed')

    packages['sys-apps/systemd'].load_instructions('./instructions.sh')

    return packages

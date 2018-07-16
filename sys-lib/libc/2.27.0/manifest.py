#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Build manifest for the GNU libc
"""

import os
from textwrap import dedent
from nbuild.cmd import cmd
from nbuild.log import ilog
from nbuild.pushd import pushd
from nbuild.pushenv import pushenv
from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_urls
from nbuild.stdenv.install import install_file, make_keeper
from nbuild.stdenv.extract import extract_tarballs
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.autotools.autoconf import do_configure


def install_libc():
    package = get_package()

    # TODO FIXME Remove this
    cmd('sed \'/test-installation/s@$(PERL)@echo not running@\' -i Makefile')

    # Install most parts of glibc
    do_make(target='install')

    # Install nscd
    with pushd(package.source_dir):
        install_file('nscd/nscd.conf', '/etc/nscd.conf')
        install_file('nscd/nscd.tmpfiles', '/usr/lib/tmpfiles.d/nscd.conf')
        install_file('nscd/nscd.service', '/lib/systemd/system/nscd.service')
    make_keeper('/var/cache/nscd')

    # Install locales
    do_make(target='localedata/install-locales')

    # Setup a default /etc/nsswitch.conf
    with open(f'{package.install_dir}/etc/nsswitch.conf', 'w+') as ld_conf:
        content = """\
        #
        # Raven-OS - /etc/nsswitch.conf
        #

        passwd:         compat files
        group:          compat files
        shadow:         compat files

        hosts:          files dns
        networks:       files dns

        services:       db files
        protocols:      db files
        rpc:            db files
        ethers:         db files
        netmasks:       files
        netgroup:       files
        bootparams:     files

        automount:      files
        aliases:        files
        """
        ld_conf.write(dedent(content))

    # Setup a default /etc/ld.so.conf
    with open(f'{package.install_dir}/etc/ld.so.conf', 'w+') as ld_conf:
        content = """\
        #
        # Raven-OS - /etc/ld.so.conf
        #

        include /etc/ld.so.conf.d/*.conf
        /usr/local/lib
        /opt/lib
        """
        ld_conf.write(dedent(content))


@package(
    id="stable::sys-lib/libc#2.27.0",
    run_dependencies={
        "stable::kernel/linux-headers": "=4.15.3",
    },
)
def build_libc():
    package = get_package()
    version = package.version.split('.0')[0]

    os.environ['libc_cv_c_cleanup'] = 'yes'
    os.environ['libc_cv_forced_unwind'] = 'yes'
    os.environ['libc_cv_rootsbindir'] = '/sbin'
    os.environ['libc_cv_slibdir'] = '/lib64'

    build_autotools_package(
        fetch=lambda: fetch_urls([
            {
                'url': f"http://ftp.gnu.org/gnu/glibc/glibc-{version}.tar.xz",
                'md5': "898cd5656519ffbc3a03fe811dd89e82",
            },
            # Fixes some FHS compliency-issues.
            {
                'url': f"http://www.linuxfromscratch.org/patches/lfs/8.2/glibc-{version}-fhs-1.patch",
                'md5': "9a5997c3452909b1769918c759eff8a2",
            },
        ]),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--enable-kernel=3.2',
                '--with-headers=/usr/include',
            ]
        ),
        install=install_libc,
    )

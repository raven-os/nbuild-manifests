#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import shutil
import stdlib
import stdlib.extract
import stdlib.split.system
from textwrap import dedent
from stdlib.template import autotools
from stdlib.template.make import make
from stdlib.template.configure import configure
from stdlib.manifest import manifest


def extract_glibc():
    stdlib.extract.flat_extract(glob.glob('glibc-*')[0])

    os.makedirs('tzdata')
    with stdlib.pushd('tzdata'):
        stdlib.extract.flat_extract(glob.glob('../tzdata*.tar*')[0])


def install_glibc():
    build = stdlib.build.current_build()

    # TODO FIXME Temporary fix to avoid a harmless failure while installing glibc
    stdlib.cmd("sed '/test-installation/s@$(PERL)@echo not running@' -i ../Makefile")

    # Install glibc
    make('install')

    # Install locales
    make('localedata/install-locales')

    # Compile all timezone data
    with stdlib.pushd(build.install_cache):
        tzdata = f'{build.build_cache}/tzdata/'
        zic = f'{build.install_cache}/usr/sbin/zic'

        os.makedirs('usr/share/zoneinfo/posix', exist_ok=True)
        os.makedirs('usr/share/zoneinfo/right', exist_ok=True)

        for tz in ['etcetera', 'southamerica', 'northamerica', 'europe', 'africa', 'antarctica',  'asia', 'australasia', 'backward', 'pacificnew', 'systemv']:
            stdlib.cmd(f'{zic} -L /dev/null -d usr/share/zoneinfo {tzdata}/{tz}')
            stdlib.cmd(f'{zic} -L /dev/null -d usr/share/zoneinfo/posix {tzdata}/{tz}')
            stdlib.cmd(f'{zic} -L {tzdata}/leapseconds -d usr/share/zoneinfo/right {tzdata}/{tz}')

        stdlib.cmd(f'{zic} -d usr/share/zoneinfo -p America/New_York')

        shutil.copy(f'{tzdata}/zone.tab', 'usr/share/zoneinfo/')
        shutil.copy(f'{tzdata}/zone1970.tab', 'usr/share/zoneinfo/')
        shutil.copy(f'{tzdata}/iso3166.tab', 'usr/share/zoneinfo/')

    # Setup default configuration files
    with stdlib.pushd(build.install_cache):
        # /etc/nsswitch.conf
        with open('etc/nsswitch.conf', 'w+') as conf:
            conf.write(dedent('''\
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
            '''))

        # /etc/ld.so.conf
        with open('etc/ld.so.conf', 'w+') as ld_conf:
            ld_conf.write(dedent('''
            #
            # Raven-OS - /etc/ld.so.conf
            #

            include /etc/ld.so.conf.d/*.conf

            /usr/local/lib
            /opt/lib
            '''))


def split_glibc():
    packages = stdlib.split.system.system()

    # The following drains are done early to ensure the deplinker
    # will link everything properly

    # Move all libxxx-2.YY.so files to glibc, or simlink will be broken
    packages['sys-libs/glibc'].drain_package(
        packages['sys-libs/glibc-dev'],
        'usr/lib64/*-{1,2}.*.so',
    )

    # Move some libraries that aren't named the same way than others and are therefore
    # wrongly picked up by the system splitter
    packages['sys-libs/glibc'].drain_package(
        packages['sys-libs/glibc-dev'],
        'usr/lib64/libpcprofile.so',
        'usr/lib64/libthread_db-*.so',
        'usr/lib64/libSegFault.so',
        'usr/lib64/libmemusage.so',
    )

    # Drain the `audit` folder that contains the `sotruss` library.
    packages['sys-libs/glibc'].drain('usr/lib64/audit/')

    return packages


@manifest(
    name='glibc',
    category='sys-libs',
    description='''
    The GNU C library.
    ''',
    tags=['gnu', 'c'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.LGPL],
    upstream_url='https://www.gnu.org/software/libc/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.29.0',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/glibc/glibc-2.29.tar.xz',
                    'sha256': 'f3eeb8d57e25ca9fc13c2af3dae97754f9f643bc69229546828e3a240e2af04b',
                }, {
                    'url': 'https://data.iana.org/time-zones/releases/tzdata2019a.tar.gz',
                    'sha256': '90366ddf4aa03e37a16cd49255af77f801822310b213f195e2206ead48c59772',
                }, {
                    'file': './fhs.patch',
                }
            ],
        },
    ],
)
def build(build):

    # TODO FIXME The following will be removed in a futur pass of glibc
    os.environ['GCC_INCDIR'] = '/usr/lib/gcc/x86_64-pc-linux-gnu/8.2.0/include'
    os.environ['CC'] = 'gcc -isystem /usr/lib/gcc/x86_64-pc-linux-gnu/8.2.0/include -isystem /usr/include '

    packages = autotools.build(
        build_folder='build',
        extract=extract_glibc,
        configure=lambda: configure(
            '--enable-kernel=3.2',
            '--enable-stack-protector=strong',
            '--infodir="/usr/share/info/glibc/"',
            binary='../configure',
        ),
        split=split_glibc,
        install=install_glibc,
    )

    # Drain pre-installed configuration
    packages['sys-libs/glibc'].drain_build_cache('nscd/nscd.conf', 'etc/nscd.conf')
    packages['sys-libs/glibc'].drain_build_cache('nscd/nscd.conf.tmpfiles', 'usr/lib/tmpfiles.d/nscd.conf')
    packages['sys-libs/glibc'].drain_build_cache('nscd/nscd.service', 'usr/lib/systemd/system/nscd.service')

    # Drain files that weren't picked-up by the splitter
    packages['sys-libs/glibc'].drain(
        'usr/share/i18n/{charmaps,locales}/',
        'usr/share/zoneinfo/',
        'usr/lib64/gconv/',
        'usr/lib64/locale/',
    )

    # Drain development files that weren't picked-up by the splitter
    packages['sys-libs/glibc-dev'].drain(
        'usr/lib64/*.o',
    )

    # Ensure `/etc/ld.so.conf.d` will be created when installing `sys-libs/glibc`
    packages['sys-libs/glibc'].make_keepers('etc/ld.so.conf.d')

    # Remove `/etc/ld.so.cache`, it will be generated by the package manager
    packages['sys-libs/glibc'].remove('etc/ld.so.cache')

    # Packages member of `raven-os/essentials` should explicitely state all
    # of their dependencies, including indirect ones.
    packages['sys-libs/glibc'].rdepends_on('raven-os/corefs', '*')

    # Glibc depends on the Linux Kernel headers to compile a software properly.
    packages['sys-libs/glibc-dev'].rdepends_on('sys-kernel/linux-dev', '>=3.2')

    return packages

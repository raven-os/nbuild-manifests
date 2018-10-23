import os
from textwrap import dedent
from nbuild.cmd import cmd
from nbuild.pushd import pushd
from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_urls
from nbuild.stdenv.install import install_file, make_keeper
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
    id="stable::sys-lib/libc#2.28.0",
    run_dependencies={
        "stable::kernel/linux-headers": "=4.18.12",
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
                'sha256': "b1900051afad76f7a4f73e71413df4826dce085ef8ddb785a945b66d7d513082",
            },
            # Fixes some FHS compliency-issues.
            {
                'url': "http://www.linuxfromscratch.org/patches/lfs/development/glibc-2.28-fhs-1.patch",
                'sha256': "643552db030e2f2d7ffde4f558e0f5f83d3fabf34a2e0e56ebdb49750ac27b0d",
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

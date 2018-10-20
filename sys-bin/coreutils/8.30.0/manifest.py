from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_urls
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.pushd import pushd
import os


def configure():
    with pushd('..'):
        cmd("sed -i '/test.lock/s/^/#/' gnulib-tests/gnulib.mk")
        cmd('autoreconf -fiv')
    os.environ['FORCE_UNSAFE_CONFIGURE'] = '1'
    do_configure(
            extra_configure_flags=[
                '--enable-no-install-program=kill,uptime',
            ],
        )


def compile():
    os.environ['FORCE_UNSAFE_CONFIGURE'] = '1'
    do_make()


def check():
    do_make(target='check-root', extra_args=['NON_ROOT_USERNAME=nobody'])
    cmd('echo "dummy:x:1000:nobody" >> /etc/group')
    cmd('chown -R nobody .')
    cmd('su nobody -s /bin/bash \
          -c "PATH=$PATH make RUN_EXPENSIVE_TESTS=yes check"')
    cmd("sed -i '/dummy/d' /etc/group")


def install():
    pk = get_package()
    do_make(target='install')

    bindir = f'{pk.install_dir}/bin'
    os.makedirs(bindir)

    usrsbindir = f'{pk.install_dir}/usr/sbin'
    os.makedirs(usrsbindir)

    mandir = f'{pk.install_dir}/usr/share/man/man8/'
    os.makedirs(mandir)

    cmd(f'mv -v {pk.install_dir}/usr/bin/{{cat,chgrp,chmod,chown,cp,date,dd,df,echo}} {bindir}')
    cmd(f'mv -v {pk.install_dir}/usr/bin/{{false,ln,ls,mkdir,mknod,mv,pwd,rm}} {bindir}')
    cmd(f'mv -v {pk.install_dir}/usr/bin/{{rmdir,stty,sync,true,uname}} {bindir}')
    cmd(f'mv -v {pk.install_dir}/usr/bin/chroot {usrsbindir}')
    cmd(f'mv -v {pk.install_dir}/usr/share/man/man1/chroot.1 {mandir}/chroot.8')
    cmd(f'sed -i s/\"1\"/\"8\"/1 {mandir}/chroot.8')


@package(
    id="stable::sys-bin/coreutils#8.30.0",
    run_dependencies={
        "stable::sys-lib/libc": "=2.28.0",
        "stable::sys-lib/attr": "=2.4.48",
        "stable::sys-lib/acl": "=2.2.53",
        "stable::sys-lib/libcap": "=2.25.0",
        "stable::sys-lib/GMP": "=6.1.2",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_urls([
            {
                'url': "http://ftp.gnu.org/gnu/coreutils/coreutils-8.30.tar.xz",
                'sha256': "e831b3a86091496cdba720411f9748de81507798f6130adeaef872d206e1b057",
            },
            {
                'url': "http://www.linuxfromscratch.org/patches/lfs/development/coreutils-8.30-i18n-1.patch",
                'sha256': "ebfc88e1b1a204dd55259f9967927f6525ffa113db935f8e0c60b49c2a11d8f0",
            }
        ]),
        configure=configure,
        compile=compile,
        check=check,
    )

from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.cmd import cmd
from nbuild.pushd import pushd


def configure():
    with pushd('..'):
        cmd('cp configfsf.guess config.guess')
        cmd('cp configfsf.sub config.sub')


def compile():
    do_make()
    do_make(target='html')


def check():
    cmd('make check 2>&1 | tee gmp-check-log')
    cmd("awk '/# PASS:/{total+=$3} ; END{print total}' gmp-check-log")


def install():
    do_make(target='install')
    do_make(target='install-html')


@package(
    id="stable::sys-lib/GMP#6.1.2",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/gmp/gmp-6.1.2.tar.xz",
            sha256="87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--enable-cxx',
                '--disable-static',
                '--docdir=/usr/share/doc/gmp-6.1.2',
            ],
        ),
        compile=compile,
        check=check,
        install=install
    )

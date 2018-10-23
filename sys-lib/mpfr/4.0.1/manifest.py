from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.pushd import pushd
import os


def compile():
    do_make()
    do_make(target='html')


def install():
    do_make(target="install")
    do_make(target="install-html")


@package(
    id="stable::sys-lib/mpfr#4.0.1",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://www.mpfr.org/mpfr-4.0.1/mpfr-4.0.1.tar.xz",
            sha256="67874a60826303ee2fb6affc6dc0ddd3e749e9bfcb4c8655e3953d0458a6e16e",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--disable-static',
                '--enable-thread-safe',
                '--docdir=/usr/share/doc/mpfr-4.0.1',
            ]
        ),
        compile=compile,
        install=install,
    )

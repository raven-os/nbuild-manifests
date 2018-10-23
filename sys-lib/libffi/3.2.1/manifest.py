from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.pushd import pushd
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make


def configure():
    with pushd('../'):
        cmd("sed -e '/^includesdir/ s/$(libdir).*$/$(includedir)/' -i include/Makefile.in")
        cmd("sed -e '/^includedir/ s/=.*$/=@includedir@/' -e 's/^Cflags: -I${includedir}/Cflags:/' -i libffi.pc.in")
    do_configure(extra_configure_flags=['--disable-static'])


@package(
    id="stable::sys-lib/libffi#3.2.1",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://sourceware.org/ftp/libffi/libffi-3.2.1.tar.gz",
            sha256="d06ebb8e1d9a22d19e38d63fdb83954253f39bedc5d46232a05645685722ca37",
        ),
        configure=configure,
    )

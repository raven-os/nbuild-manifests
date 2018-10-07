from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure


@package(
    id="stable::sys-dev/bison#3.0.5",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/bison/bison-3.0.5.tar.xz",
            sha256="075cef2e814642e30e10e8155e93022e4a91ca38a65aa1d5467d4e969f97f338",
        ),
        configure=lambda: do_configure(extra_configure_flags=['--docdir=/usr/share/doc/bison-3.0.5'])
    )

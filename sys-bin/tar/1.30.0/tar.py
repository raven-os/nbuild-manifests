from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure


@package(
    id="stable::sys-bin/tar#1.30.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/tar/tar-1.30.tar.xz",
            sha256="f1bf92dbb1e1ab27911a861ea8dde8208ee774866c46c0bb6ead41f4d1f4d2d3",
        ),
        configure=lambda: do_configure(extra_configure_flags=[f"--bindir=/bin",
                                                              "FORCE_UNSAFE_CONFIGURE=1"])
    )

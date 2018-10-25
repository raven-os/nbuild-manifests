from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure


@package(
    id="stable::sys-lib/gdbm#1.18.0",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/gdbm/gdbm-1.18.tar.gz",
            sha256="b8822cb4769e2d759c828c06f196614936c88c141c3132b18252fe25c2b635ce",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--disable-static',
            ]
        )
    )

from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make


@package(
    id="stable::sys-bin/grep#3.1.0",
    run_dependencies={
        'stable::sys-lib/PCRE': '=8.41.0',
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/grep/grep-3.1.tar.xz",
            sha256="db625c7ab3bb3ee757b3926a5cfa8d9e1c3991ad24707a83dde8a5ef2bf7a07e",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[f"--bindir=/bin"]
        ),
        check=lambda: do_make(target="check", extra_args="-k", fail_ok=True)
    )

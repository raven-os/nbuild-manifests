from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure


def configure():
    do_configure(
            extra_configure_flags=[
                '--disable-static',
                f'--docdir=/usr/share/doc/libunistring-0.9.10',
            ]
        )


@package(
    id="stable::sys-lib/libunistring#0.9.10",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://ftp.gnu.org/gnu/libunistring/libunistring-0.9.10.tar.xz",
            sha256="eb8fb2c3e4b6e2d336608377050892b54c3c983b646c561836550863003c05d7",
        ),
        configure=configure,
    )

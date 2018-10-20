from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make


@package(
    id="stable::sys-bin/binutils#2.31.1",
    run_dependencies={
        "stable::sys-lib/libc": "=2.28.0",
        "stable::sys-lib/zlib": "=1.2.11",
        "stable::sys-dev/flex": "=2.6.4",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/binutils/binutils-2.31.1.tar.xz",
            sha256="5d20086ecf5752cc7d9134246e9588fa201740d540f7eb84d795b1f7a93bca86",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                 '--enable-gold',
                 '--enable-ld=default',
                 '--enable-plugins',
                 '--enable-shared',
                 '--disable-werror',
                 '--enable-64-bit-bfd',
                 '--with-system-zlib',
             ]
        ),
        compile=lambda: do_make(extra_args=['tooldir=/usr']),
        install=lambda: do_make(target='install', extra_args=['tooldir=/usr']),
    )

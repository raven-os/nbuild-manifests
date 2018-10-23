from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-lib/libtool#2.4.6",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::shell/bash": "4.4.18",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/libtool/libtool-2.4.6.tar.xz",
            sha256="7c87a8c2c8c0fc9cd5019e402bed4292462d00a718a7cd5f11218153bf28b26f",
        ),
    )

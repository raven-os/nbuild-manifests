from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-bin/diffutils#3.6.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/diffutils/diffutils-3.6.tar.xz",
            sha256="d621e8bdd4b573918c8145f7ae61817d1be9deb4c8d2328a65cea8e11d783bd6",
        ),
    )

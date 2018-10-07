from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-bin/which#2.21.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/which/which-2.21.tar.gz",
            sha256="f4a245b94124b377d8b49646bf421f9155d36aa7614b6ebf83705d3ffc76eaad",
        ),
    )

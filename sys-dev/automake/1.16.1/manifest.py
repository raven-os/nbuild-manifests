from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package

@package(
    id="stable::sys-dev/automake#1.16.1",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/automake/automake-1.16.1.tar.xz",
            sha256="5d05bb38a23fd3312b10aea93840feec685bdf4a41146e78882848165d3ae921",
        ),
    )

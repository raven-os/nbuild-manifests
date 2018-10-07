from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-lib/sed#4.5.0",
)
def build_helloworld():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/sed/sed-4.5.tar.xz",
            sha256="7aad73c8839c2bdadca9476f884d2953cdace9567ecd0d90f9959f229d146b40",
        ),
    )

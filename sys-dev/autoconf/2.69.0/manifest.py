from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package

@package(
    id="stable::sys-dev/autoconf#2.69.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz",
            sha256="64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684",
        ),
    )


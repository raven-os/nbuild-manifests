from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package

@package(
    id="stable::sys-dev/autoconf#2.69.0",
    run_dependencies={
        "stable::sys-bin/perl": "=5.28.0",
        "stable::shell/bash": "=4.4.18",
        "stable::sys-bin/sed": "=4.5.0",
        "stable::sys-lib/acl": "=4.4.18",
        "stable::sys-bin/coreutils": "=8.30.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.xz",
            sha256="64ebcec9f8ac5b2487125a86a7760d2591ac9e1d3dbd59489633f9de62a57684",
        ),
    )


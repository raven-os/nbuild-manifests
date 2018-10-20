from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-lib/libseccomp#2.3.3",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://github.com/seccomp/libseccomp/releases/download/v2.3.3/libseccomp-2.3.3.tar.gz",
            sha256="7fc28f4294cc72e61c529bedf97e705c3acf9c479a8f1a3028d4cd2ca9f3b155",
        ),
    )

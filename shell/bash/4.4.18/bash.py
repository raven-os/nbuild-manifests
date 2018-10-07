from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package


@package(
    id="stable::shell/bash#4.4.18",
)
def build():
    package = get_package()
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/bash/bash-4.4.18.tar.gz",
            sha256="604d9eec5e4ed5fd2180ee44dd756ddca92e0b6aa4217bbab2b6227380317f23",
        ),
        configure=lambda: do_configure(prefix=package.install_dir),
    )

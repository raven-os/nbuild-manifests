from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package


@package(
    id="stable::sys-bin/util-linux#2.32.1",
    run_dependencies={
        "stable::sys-lib/libc": "=2.28.0",
        "stable::sys-lib/ncurses": "=6.1.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.kernel.org/pub/linux/utils/util-linux/v2.32/util-linux-2.32.1.tar.xz",
            sha256="86e6707a379c7ff5489c218cfaf1e3464b0b95acf7817db0bc5f179e356a67b2",
        ),
    )

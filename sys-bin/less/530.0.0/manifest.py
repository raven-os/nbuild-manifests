from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package


@package(
    id="stable::sys-bin/less#530.0.0",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.27.0",
        "stable::sys-lib/ncurses": ">=6.1.0",
    }
)
def build():
    package = get_package()
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://www.greenwoodsoftware.com/less/less-530.tar.gz",
            sha256="736ae133c01824915a5e74c6482c74e88071fb7084e070e7aac3c701d4406b74",
        ),
        configure=lambda: do_configure(prefix=f'{package.install_dir}/usr')
    )

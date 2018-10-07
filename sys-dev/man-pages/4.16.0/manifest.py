from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.package import get_package
from nbuild.cmd import cmd


@package(
    id="stable::sys-dev/man-pages#4.16.0",
)
def build():
    package = get_package()
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.kernel.org/pub/linux/docs/man-pages/man-pages-4.16.tar.xz",
            sha256="47ffcc0d27d50e497e290b27e8d76dbed4550db14c881f25b771bcaf28354db4",
        ),
        configure=lambda: None,
        compile=lambda: None,
        check=lambda: None,
        install=lambda: do_make(target='install', folder='..', extra_args=[f'DESTDIR={package.install_dir}'])
    )

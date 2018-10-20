from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.stdenv.package import get_package


def install_python3():
    package = get_package()
    do_make(target="install")
    cmd(f"chmod 755 /{package.install_dir}/usr/lib/libpython3.7m.so")
    cmd(f"chmod 755 /{package.install_dir}/usr/lib/libpython3.so")

    cmd(f"install -dm755 /{package.install_dir}/usr/share/doc/python-3.7.0/html")
    cmd("tar --strip-components=1 "
        "--no-same-owner "
        "--no-same-permissions "
        f"-C /{package.install_dir}/usr/share/doc/python-3.7.0/html "
        f"-xf /{package.download_dir}/python-3.7.0-docs-html.tar.bz2")


@package(
    id="stable::python/python#2.7.15",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url= "https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tar.xz",
            sha256= "22d9b1ac5b26135ad2b8c2901a9413537e08749a753356ee913c84dbd2df5574",
        ),
    )

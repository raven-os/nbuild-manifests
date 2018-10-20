from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_urls
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
    id="stable::python/python#3.7.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_urls([
            {
                'url': "https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz",
                'sha256': "0382996d1ee6aafe59763426cf0139ffebe36984474d0ec4126dd1c40a8b3549",
            },
            {
                'url': "https://docs.python.org/ftp/python/doc/3.7.0/python-3.7.0-docs-html.tar.bz2",
                'sha256': "de2be9d07f6940aadac18e92ac76ce53556df9e5b28d5f1ba040def5cb3d5837",
            }
        ]),
        configure=lambda: do_configure(
            binary="../Python-3.7.0/configure",
            extra_configure_flags=[
                "--enable-shared",
                "--with-system-expat",
                "--with-system-ffi",
                "--with-ensurepip=yes"
            ]
        ),
        install=install_python3,
    )

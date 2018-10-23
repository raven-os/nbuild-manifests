from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.stdenv.package import get_package


def install():
    pk = get_package()
    do_make(target="install")
    cmd(f'chmod -v 755 {pk.install_dir}/usr/lib/libpython2.7.so.1.0')


@package(
    id="stable::python/python#2.7.15",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tar.xz",
            sha256="22d9b1ac5b26135ad2b8c2901a9413537e08749a753356ee913c84dbd2df5574",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                ' --enable-shared',
                '--with-system-expat',
                '--with-system-ffi',
                '--with-ensurepip=yes',
                '--enable-unicode=ucs4',
            ]
        ),
        install=install,
    )

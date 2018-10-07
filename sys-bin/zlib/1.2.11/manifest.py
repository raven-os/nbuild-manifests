from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.package import get_package
from nbuild.cmd import cmd
from nbuild.pushd import pushd


def install():
    do_make(target='install')
    with pushd('..'):
        package = get_package()
        cmd(f'mkdir /{package.install_dir}/lib -p')
        cmd(f'mv -v /{package.install_dir}/usr/lib/libz.so.* /{package.install_dir}/lib')
        cmd(f'ln -sfv ../../lib/$(readlink /{package.install_dir}/usr/lib/libz.so) /{package.install_dir}/usr/lib/libz.so')


@package(
    id="stable::sys-bin/zlib#1.2.11",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://zlib.net/zlib-1.2.11.tar.xz",
            sha256="4ff941449631ace0d4d203e3483be9dbc9da454084111f97ea0a2114e19bf066",
        ),
        configure=lambda: cmd('../configure --prefix=/usr'),
        install=install,
    )

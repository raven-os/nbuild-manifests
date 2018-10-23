from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.pushd import pushd
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
import os


def install():
    package = get_package()
    do_make(target="install")
    with pushd('../'):
        os.mkdir(f'{package.install_dir}/bin')
        cmd(f'mv -v  /{package.install_dir}/usr/bin/{{lzma,unlzma,lzcat,xz,unxz,xzcat}} {package.install_dir}/bin')
        os.mkdir(f'{package.install_dir}/lib')
        cmd(f'mv -v /{package.install_dir}/usr/lib/liblzma.so.* {package.install_dir}/lib')
        cmd(f'ln -svf ../../lib/$(readlink /{package.install_dir}/usr/lib/liblzma.so) /{package.install_dir}/usr/lib/liblzma.so')


@package(
    id="stable::sys-bin/xz#5.2.4",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::shell/bash": "4.4.18",
        "stable::sys-bin/less": "530.0.0",
        "stable::sys-bin/util-linux": "2.32.1",
        "stable::sys-bin/grep": "3.1.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://tukaani.org/xz/xz-5.2.4.tar.xz",
            sha256="9717ae363760dedf573dad241420c5fea86256b65bc21d2cf71b2b12f0544f4b",
        ),
        install=install,
    )

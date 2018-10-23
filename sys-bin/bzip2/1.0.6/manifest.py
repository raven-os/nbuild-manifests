from nbuild.stdenv.package import package
from nbuild.pushd import pushd
from nbuild.stdenv.fetch import fetch_urls
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.stdenv.patch import apply_patches
from nbuild.stdenv.package import get_package
import os


def patch():
    apply_patches()
    pk = get_package()
    cmd(f"sed -i 's@\\(ln -s -f \\){pk.install_dir}/usr/bin/@\1@' Makefile")
    cmd(f'sed -i "s@(PREFIX)/man@{pk.install_dir}/usr/share/man@g" Makefile')
    cmd("make -f Makefile-libbz2_so")
    cmd("make clean")


def install():
    pk = get_package()
    do_make(target="install", folder="..",
            extra_args=[f"PREFIX={pk.install_dir}/usr"]),
    with pushd(".."):
        bin_dir = f'{pk.install_dir}/bin'
        lib_dir = f'{pk.install_dir}/lib'
        usrlib_dir = f'{pk.install_dir}/usr/lib/'

        os.makedirs(bin_dir)
        os.makedirs(lib_dir)

        cmd(f"cp bzip2-shared {bin_dir}/bzip2")
        cmd(f"cp -a libbz2.so* {lib_dir}")

        cmd(f"mkdir -p {usrlib_dir}")
        cmd(f"ln -s libbz2.so.1.0 {usrlib_dir}/libbz2.so")
        cmd(f'rm -v {pk.install_dir}/usr/bin/{{bunzip2,bzcat,bzip2}}')
        cmd(f"ln -fs bzip2 {bin_dir}/bunzip2")
        cmd(f"ln -fs bzip2 {bin_dir}/bzcat")


@package(
    id="stable::sys-bin/bzip2#1.0.6",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_urls([
            {
                'url': "http://anduin.linuxfromscratch.org/LFS/bzip2-1.0.6.tar.gz",
                'sha256': "a2848f34fcd5d6cf47def00461fcb528a0484d8edef8208d6d2e2909dc61d9cd",
            },
            {
                'url': "http://www.linuxfromscratch.org/patches/lfs/8.3/bzip2-1.0.6-install_docs-1.patch",
                'sha256': "35e3bbd9642af51fef2a8a83afba040d272da42d7e3a251d8e43255a7b496702",
            }
        ]),
        patch=patch,
        configure=lambda: None,
        compile=lambda: do_make(folder=".."),
        check=lambda: None,
        install=install,
    )

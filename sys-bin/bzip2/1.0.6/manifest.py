from nbuild.stdenv.package import package
from nbuild.pushd import pushd
from nbuild.stdenv.fetch import fetch_urls
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.stdenv.package import get_package


def configure():
    with pushd(".."):
        # cmd("sed -i 's@\(ln -s -f \)$(PREFIX)/bin/@\1@' Makefile")
        # sed -i "s@(PREFIX)/man@(PREFIX)/share/man@g" Makefile
        cmd("make -f Makefile-libbz2_so")
        cmd("make clean")


def install():
    package = get_package()
    do_make(target="install", folder="..",
            extra_args=["PREFIX={}".format(package.install_dir)]),
    with pushd(".."):
        cmd(f"cp bzip2-shared /{package.install_dir}/bin/bzip2")
        cmd(f"cp -a libbz2.so* /{package.install_dir}/lib")
        cmd(f"mkdir -p /{package.install_dir}/usr/lib/libbz2.so")
        cmd(f"ln -s libbz2.so.1.0 /{package.install_dir}/usr/lib/libbz2.so")
        cmd(f"ln -fs bzip2 /{package.install_dir}/bin/bunzip2")
        cmd(f"ln -fs bzip2 /{package.install_dir}/bin/bzcat")


@package(
    id="stable::sys-bin/bzip2#1.0.6",
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
        configure=configure,
        compile=lambda: do_make(folder=".."),
        install=install
    )

from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.pushd import pushd
from nbuild.cmd import cmd
import os


def configure():
    with pushd('../vim81'):
        cmd("echo '#define SYS_VIMRC_FILE \"/etc/vimrc\"' >> src/feature.h")
        do_configure(binary='./configure')


def check():
    cmd("LANG=en_US.UTF-8 make -C ../vim81 -j1 test &> vim-test.log")


def install():
    package = get_package()
    with pushd('../vim81'):
        do_make(target='install')
        docdir = f"/{package.install_dir}/usr/share/doc/"
        cmd(f'mkdir -p {docdir}')
        cmd(f'ln -sv ../vim/vim81/doc {docdir}/vim-8.1')

@package(
    id="stable::editor/vim#8.1.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="ftp://ftp.vim.org/pub/vim/unix/vim-8.1.tar.bz2",
            sha256="8b69fbd01c877dd8ecbbeca1dc66e5e927228d631ac4c2174b9307eb5c827c86",
        ),
        configure=configure,
        compile=lambda: do_make(target='../vim81'),
        check=check,
        install=install,
    )

from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.cmd import cmd
import os


def configure():
    package = get_package()
    cmd("sed -i '/MV.*old/d' ../Makefile.in")
    cmd("sed -i '/{OLDSUFF}/c:' ../support/shlib-install")
    cmd("sed -i 's|-Wl,-rpath,$(libdir) ||g' ../support/shobj-conf")
    do_configure(
            prefix=f'/{package.install_dir}/usr',
            extra_configure_flags=[
                "--docdir=/{package.install_dir}/share/doc/readline-7.0"
            ]
        )


def compile():
    do_make(extra_args=['SHLIB_LIBS=-lncursesw'])


def install():
    do_make(target='install')
    package = get_package()
    dir_lib = f'{package.install_dir}/lib'
    dir_usrlib = f'{package.install_dir}/usr/lib'
    if not os.path.exists(dir_lib):
        os.makedirs(dir_lib)
    if not os.path.exists(dir_usrlib):
        os.makedirs(dir_usrlib)
    cmd(f'mv -v {package.install_dir}/usr/lib/lib{{readline,history}}.so.* {dir_lib}')
    cmd(f'chmod -v u+w {dir_lib}/lib{{readline,history}}.so.*')
    cmd(f'ln -sfv ../../lib/$(readlink {dir_usrlib}/libreadline.so) {dir_usrlib}/libreadline.so')
    cmd(f'ln -sfv ../../lib/$(readlink {dir_usrlib}/libhistory.so ) {dir_usrlib}/libhistory.so')


@package(
    id="stable::sys-lib/readline#7.0.0",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::sys-lib/ncurses": "6.1.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/readline/readline-7.0.tar.gz",
            sha256="750d437185286f40a369e1e4f4764eda932b9459b5ec9a731628393dd3d32334",
        ),
        configure=configure,
        compile=compile,
        check=lambda: None,
        install=install,
    )

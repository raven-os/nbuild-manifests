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
    cmd('sed -i s/mawk// ../configure')
    do_configure(
            prefix=f'{package.install_dir}/usr',
            extra_configure_flags=[
                f"--mandir={package.install_dir}/usr/share/man",
                "--with-shared",
                "--without-debug",
                "--without-ada",
                "--enable-overwrite",
                "--enable-widec",
            ]
        )


def install():
    do_make(target='install')
    package = get_package()
    os.mkdir(f'/{package.install_dir}/lib')
    cmd(f'mv {package.install_dir}/usr/lib/libncursesw.so.6* /{package.install_dir}/lib')
    cmd(f'ln -sf ../../lib/$(readlink {package.install_dir}/usr/lib/libncursesw.so) {package.install_dir}/usr/lib/libncursesw.so')

    os.mkdir(f'{package.install_dir}/usr/lib/pkgconfig')

    cmd('for lib in ncurses form panel menu;'
        f' do rm -f {package.install_dir}/usr/lib/lib${{lib}}.so; '
        f' echo "INPUT(-l${{lib}}w)" > {package.install_dir}/usr/lib/lib${{lib}}.so;'
        f' ln -sf ${{lib}}w.pc {package.install_dir}/usr/lib/pkgconfig/${{lib}}.pc;'
        ' done')

    cmd(f'rm -f {package.install_dir}/usr/lib/libcursesw.so')
    cmd(f'echo "INPUT(-lncursesw)" > {package.install_dir}/usr/lib/libcursesw.so')
    cmd(f'ln -sf libncurses.so {package.install_dir}/usr/lib/libcurses.so')

    os.makedirs(f'{package.install_dir}/usr/share/doc/ncurses-6.1')
    cmd(f'cp -R ../doc/* {package.install_dir}/usr/share/doc/ncurses-6.1')


@package(
    id="stable::sys-lib/ncurses#6.1.0",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/ncurses/ncurses-6.1.tar.gz",
            sha256="aa057eeeb4a14d470101eff4597d5833dcef5965331be3528c08d99cebaa0d17",
        ),
        configure=configure,
        install=install,
    )

from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.make import do_make
import os


def install():
    pk = get_package()
    do_make(target='install')
    cmd(f'ln -s /usr/bin/bash {pk.install_dir}/usr/bin/sh')


@package(
    id="stable::shell/bash#4.4.18",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.28.0",
        "stable::sys-lib/ncurses": ">=6.1.0",
        "stable::sys-lib/readline": ">=7.0.0",
    }
)
def build():
    package = get_package()
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/bash/bash-4.4.18.tar.gz",
            sha256="604d9eec5e4ed5fd2180ee44dd756ddca92e0b6aa4217bbab2b6227380317f23",
        ),
        configure=lambda: do_configure(prefix=f'{package.install_dir}/usr'),
        check=lambda: None,
        install=install,
    )

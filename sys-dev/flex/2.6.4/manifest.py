from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.cmd import cmd
from nbuild.pushd import pushd
from nbuild.stdenv.autotools.make import do_make
import os


def configure():
    cmd('sed -i "/math.h/a #include <malloc.h>" ../src/flexdef.h')
    os.environ["HELP2MAN"] = '/bin/true'
    do_configure(extra_configure_flags=['--docdir=/usr/share/doc/flex-2.6.4'])


def install():
    with pushd('../'):
        do_make(binary='build/Makefile', target='install')
        cmd('ln -sv flex /usr/bin/lex')


@package(
    id="stable::sys-dev/flex#2.6.4",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.27.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://github.com/westes/flex/releases/download/v2.6.4/flex-2.6.4.tar.gz",
            sha256="e87aae032bf07c26f85ac0ed3250998c37621d95f8bd748b31f15b33c45ee995",
        ),
        configure=configure,
    )

from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.autoconf import do_configure


def configure():
    cmd("sed -i '5481,5485 s/({/(\\{/' ../tp/Texinfo/Parser.pm")
    do_configure()


@package(
    id="stable::sys-bin/texinfo#6.5.0",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.28.0",
        "stable::sys-lib/ncurses": ">=6.1.0",
        "stable::sys-bin/perl": "=5.28.0",
        "stable::shell/bash": "=4.4.18",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/texinfo/texinfo-6.5.tar.xz",
            sha256="77774b3f4a06c20705cc2ef1c804864422e3cf95235e965b1f00a46df7da5f62",
        ),
        configure=configure,
    )

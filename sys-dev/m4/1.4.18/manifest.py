from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.cmd import cmd


def configure():
    cmd("sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' ../lib/*.c")
    cmd('echo "#define _IO_IN_BACKUP 0x100" >> ../lib/stdio-impl.h')
    do_configure()

@package(
    id="stable::sys-dev/m4#1.4.18",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.27.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/m4/m4-1.4.18.tar.xz",
            sha256="f2c1e86ca0a404ff281631bdc8377638992744b175afb806e25871a24a934e07",
        ),
        configure=configure,
    )

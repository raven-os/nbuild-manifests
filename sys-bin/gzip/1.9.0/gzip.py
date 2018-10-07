from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.pushd import pushd
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.autoconf import do_configure


def configure():
    with pushd('../'):
        cmd('sed -i "s/IO_ftrylockfile/IO_EOF_SEEN/" lib/*.c')
        cmd('echo "#define _IO_IN_BACKUP 0x100" >> lib/stdio-impl.h')
    do_configure()


@package(
    id="stable::sys-bin/gzip#1.9.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/gzip/gzip-1.9.tar.xz",
            sha256="ae506144fc198bd8f81f1f4ad19ce63d5a2d65e42333255977cf1dcf1479089a",
        ),
        configure=configure,
    )

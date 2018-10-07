from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.pushd import pushd


def configure():
    package = get_package()
    with pushd("../"):
        cmd("sed -i 's/test-lock..EXEEXT.//' tests/Makefile.in")
        cmd("sed -i 's/IO_ftrylockfile/IO_EOF_SEEN/' gl/lib/*.c")
        cmd("sed -i '/unistd/a #include <sys/sysmacros.h>' gl/lib/mountlist.c")
        cmd("echo '#define _IO_IN_BACKUP 0x100' >> gl/lib/stdio-impl.h")
    do_configure(
                 extra_configure_flags=[
                     f"localstatedir={package.install_dir}/var/lib/locate",
                 ])


@package(
    id="stable::sys-bin/findutils#4.6.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/findutils/findutils-4.6.0.tar.gz",
            sha256="ded4c9f73731cd48fec3b6bdaccce896473b6d8e337e9612e16cf1431bb1169d",
        ),
        configure=configure,
    )

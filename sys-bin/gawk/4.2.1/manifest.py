from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.pushd import pushd
import os


def configure():
    package = get_package()
    # os.environ.pop('LD')
    cmd("sed -i 's/extras//' ../Makefile.in")
    do_configure()


def install():
    package = get_package()
    do_make(target="install")
    # doc_dir = f"/{package.install_dir}/usr/share/doc/tar-1.30"
    # cmd(f"mkdir -p {doc_dir}")
    # cmd(f"make -C doc install-html docdir={doc_dir}")


@package(
    id="stable::sys-bin/gawk#4.2.1",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::sys-lib/mpfr": "4.0.1",
        "stable::sys-lib/readline": "4.0.1",
        "stable::sys-lib/GMP": "6.1.2",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/gawk/gawk-4.2.1.tar.xz",
            sha256="d1119785e746d46a8209d28b2de404a57f983aa48670f4e225531d3bdc175551",
        ),
        configure=configure,
        install=install,
    )

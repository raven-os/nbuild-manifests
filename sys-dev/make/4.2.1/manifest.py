from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.cmd import cmd
from nbuild.pushd import pushd
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make


def configure():
    with pushd("../"):
        cmd("sed -i '211,217 d; 219,229 d; 232 d' glob/glob.c")
    do_configure()


@package(
    id="stable::sys-dev/make#4.2.1",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/make/make-4.2.1.tar.bz2",
            sha256="d6e262bf3601b42d2b1e4ef8310029e1dcf20083c5446b4b7aa67081fdffc589",
        ),
        configure=configure,
        check=lambda: do_make(target="check", extra_args=["PERL5LIB=$PWD/tests/"]),
    )

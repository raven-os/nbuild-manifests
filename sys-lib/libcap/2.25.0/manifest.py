from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd


def compile():
    cmd("sed -i '/install.*STALIBNAME/d' ../libcap/Makefile")
    do_make(folder='..')


def install():
    pk = get_package()
    do_make(target='install', folder='..', extra_args=['RAISE_SETFCAP=no', 'lib=lib'])
    cmd(f'chmod -v 755 {pk.install_dir}/lib/libcap.so')


@package(
    id="stable::sys-lib/libcap#2.25.0",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-2.25.tar.xz",
            sha256="693c8ac51e983ee678205571ef272439d83afe62dd8e424ea14ad9790bc35162",
        ),
        configure=lambda: None,
        compile=compile,
        check=lambda: None,
        install=install,
    )

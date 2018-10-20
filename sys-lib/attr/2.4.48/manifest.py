from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
import os


def install():
    do_make(target='install')
    package = get_package()
    os.makedirs(f'{package.install_dir}/lib')
    cmd(f'mv {package.install_dir}/usr/lib/libattr.so.* {package.install_dir}/lib')
    cmd(f'ln -sfv ../../lib/$(readlink {package.install_dir}/usr/lib/libattr.so) {package.install_dir}/usr/lib/libattr.so')


@package(
    id='stable::sys-lib/attr#2.4.48',
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://download.savannah.gnu.org/releases/attr/attr-2.4.48.tar.gz",
            sha256="5ead72b358ec709ed00bbf7a9eaef1654baad937c001c044fe8b74c57f5324e7",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--bindir=/bin',
                '--disable-static',
                '--sysconfdir=/etc',
                '--docdir=/usr/share/doc/attr-2.4.48',
            ]
        ),
        install=install,
    )

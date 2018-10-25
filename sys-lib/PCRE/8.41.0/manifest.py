from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
import os


def install():
    pk = get_package()
    do_make(target='install')
    dirlib = f'{pk.install_dir}/lib'
    os.makedirs(dirlib)
    cmd(f'mv /usr/lib/libpcre.so.* {dirlib}')
    cmd(f'ln -sf ../../lib/$(readlink {pk.install_dir}/usr/lib/libpcre.so) {pk.install_dir}/usr/lib/libpcre.so')


@package(
    id="stable::sys-lib/PCRE#8.41.0",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://downloads.sourceforge.net/pcre/pcre-8.41.tar.bz2",
            sha256="e62c7eac5ae7c0e7286db61ff82912e1c0b7a0c13706616e94a7dd729321b530",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--docdir=/usr/share/doc/pcre-8.41',
                '--enable-unicode-properties',
                '--enable-pcre16',
                '--enable-pcre32',
                '--enable-pcregrep-libz',
                '--enable-pcregrep-libbz2',
                '--enable-pcretest-libreadline',
                '--disable-static',
            ]
        )
    )


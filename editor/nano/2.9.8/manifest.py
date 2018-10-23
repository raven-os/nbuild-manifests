from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.package import get_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd


def install():
    package = get_package()
    do_make(target="install")
    docdir = f"/{package.install_dir}/usr/share/doc/nano-2.9.8"
    cmd(f"mkdir -p {docdir}")
    cmd(f"install -v -m644 ../doc/{{nano.html,sample.nanorc.in}} {docdir}")


@package(
    id="stable::editor/nano#2.9.8",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::sys-lib/ncurses": ">=6.1.0",
        "stable::sys-bin/file": ">=5.34.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.nano-editor.org/dist/v2.9/nano-2.9.8.tar.xz",
            sha256="c2deac31ba4d3fd27a42fafcc47ccf499296cc69a422bbecab63f2933ea85488",
        ),
        configure=lambda: do_configure(
                               extra_configure_flags=[
                                   "--enable-utf8",
                                   f"--docdir=/usr/share/doc/nano-2.9.8"
                               ]),
        check=lambda: None,
        install=install,
    )

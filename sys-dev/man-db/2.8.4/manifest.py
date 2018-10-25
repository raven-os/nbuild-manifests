from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure


@package(
    id="stable::sys-dev/man-db#2.8.4",
    run_dependencies={
        "stable::sys-lib/libc": "2.28.0",
        "stable::sys-lib/zlib": "2.28.0",
        "stable::sys-lib/libseccomp": "2.28.0",
        "stable::sys-lib/libpipeline": "1.5.0",
        "stable::sys-lib/gdbm": "1.18.0",
        "stable::sys-bin/coreutils": "8.30.0",
        "stable::sys-bin/groff": "1.22.3",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://download.savannah.gnu.org/releases/man-db/man-db-2.8.4.tar.xz",
            sha256="103c185f9d8269b9ee3b8a4cb27912b3aa393e952731ef96fedc880723472bc3",
        ),
        configure=lambda: do_configure(
            extra_configure_flags=[
                '--docdir=/usr/share/doc/man-db-2.8.4',
                '--sysconfdir=/etc',
                '--disable-setuid',
                '--enable-cache-owner=bin',
                '--with-browser=/usr/bin/lynx',
                '--with-vgrind=/usr/bin/vgrind',
                '--with-grap=/usr/bin/grap',
                '--with-systemdtmpfilesdir=',
            ]
        )
    )

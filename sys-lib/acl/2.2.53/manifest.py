from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.pushd import pushd
import os


def configure():
    # cmd("sed -i -e 's|/@pkg_name@|&-@pkg_version@|' ../include/builddefs.in")
    os.environ['INSTALL_USER'] = 'root'
    os.environ['INSTALL_GROUP'] = 'root'

    do_configure(extra_configure_flags=[
        '--libexecdir=/usr/lib',
        '--disable-static'
    ])


def install():
    package = get_package()
    do_make(target='install')
    cmd(f'chmod 755 {package.install_dir}/usr/lib/libacl.so')
    libdir = f'{package.install_dir}/lib'
    os.makedirs(libdir)
    cmd(f'mv {package.install_dir}/usr/lib/libacl.so.* {libdir}')
    cmd(f'ln -sf ../../../lib/libacl.so.1 {package.install_dir}/usr/lib/libacl.so')
    docdir = f'{package.install_dir}/usr/share/doc/acl-2.2.52'
    os.makedirs(docdir)
    cmd(f'install -v -m644 ../doc/*.txt {docdir}')


@package(
    id="stable::sys-lib/acl#2.2.53",
    run_dependencies={
        'stable::sys-lib/attr': '2.4.48',
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://download.savannah.gnu.org/releases/acl/acl-2.2.53.tar.gz",
            sha256="06be9865c6f418d851ff4494e12406568353b891ffe1f596b34693c387af26c7",
        ),
        configure=configure,
        install=install,
    )

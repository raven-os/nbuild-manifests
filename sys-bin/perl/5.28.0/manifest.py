from nbuild.stdenv.package import package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.stdenv.autotools.make import do_make
from nbuild.cmd import cmd
from nbuild.pushd import pushd
import os


def configure():
    cmd("sed -i 's|BEGIN {|BEGIN { plan(skip_all => \"fatal test unsupported with gdbm 1.15\");|' ../ext/GDBM_File/t/fatal.t")
    os.environ['BUILD_ZLIB'] = 'False'
    os.environ['BUILD_BZIP2'] = '0'

    with pushd('../'):
        arch_opts = "-Dcccdlflags='-fPIC'"
        os.environ['CFLAGS'] += ' -fno-plt'
        os.environ['LDFLAGS'] = "-Wl,--as-needed,-z,now"
        cmd(f'./Configure -des -Dusethreads -Duseshrplib -Doptimize=\"{os.environ["CFLAGS"]}\" \
    -Dprefix=/usr -Dvendorprefix=/usr \
    -Dprivlib=/usr/share/perl5/core_perl \
    -Darchlib=/usr/lib/perl5/$_baseversion/core_perl \
    -Dsitelib=/usr/share/perl5/site_perl \
    -Dsitearch=/usr/lib/perl5/$_baseversion/site_perl \
    -Dvendorlib=/usr/share/perl5/vendor_perl \
    -Dvendorarch=/usr/lib/perl5/$_baseversion/vendor_perl \
    -Dscriptdir=/usr/bin/core_perl \
    -Dsitescript=/usr/bin/site_perl \
    -Dvendorscript=/usr/bin/vendor_perl \
    -Dinc_version_list=none \
    -Dman1ext=1perl -Dman3ext=3perl {arch_opts} \
    -Dlddlflags=\"-shared {os.environ["LDFLAGS"]}\"  -Dldflags=\"{os.environ["LDFLAGS"]}\"')


def compile():
    os.environ['CFLAGS'] += ' -fPIC'
    do_make(folder='..')


@package(
    id="stable::sys-bin/perl#5.28.0",
    run_dependencies={
        "stable::sys-lib/libc": ">=2.27.0",
    }
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="https://www.cpan.org/src/5.0/perl-5.28.0.tar.xz",
            sha256="059b3cb69970d8c8c5964caced0335b4af34ac990c8e61f7e3f90cd1c2d11e49",
        ),
        configure=configure,
        compile=compile,
        check=lambda: do_make(target='check', folder='..', extra_args=['-k']),
        install=lambda: do_make(target='install', folder='..')
    )

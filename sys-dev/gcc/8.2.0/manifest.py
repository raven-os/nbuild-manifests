from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.autotools import build_autotools_package
from nbuild.stdenv.autotools.make import do_make
from nbuild.stdenv.autotools.autoconf import do_configure
from nbuild.cmd import cmd
from nbuild.pushd import pushd
import os


def configure():
    os.environ.pop('CC')
    os.environ.pop('HOSTCC')
    os.environ.pop('CFLAGS')
    os.environ.pop('CXX')
    os.environ.pop('HOSTCXX')
    os.environ.pop('CXXFLAGS')
    os.environ.pop('AS')
    os.environ.pop('HOSTAS')
    os.environ.pop('ASFLAGS')
    os.environ['PATH'] = f'/usr/lib/ccache/bin/:{os.environ["PATH"]}'
    with pushd('../'):
        cmd("case $(uname -m) in \
                x86_64) \
                sed -e '/m64=/s/lib64/lib/' \
                -i.orig gcc/config/i386/t-linux64 \
                ;; \
                esac")
    os.environ['SED'] = 'sed'
    cmd('../configure --prefix=/usr '
        '--enable-languages=c,c++ '
        '--disable-multilib '
        '--disable-bootstrap '
        '--disable-libmpx '
        '--with-system-zlib ')
    # do_configure(
    #     extra_configure_flags=[
    #          '--enable-languages=c,c++',
    #          '--disable-multilib',
    #          '--disable-bootstrap',
    #          '--disable-libmpx',
    #          '--with-system-zlib',
    #     ]
    # )


def compile():
    do_make()

    """CC=x86_64-pc-linux-gnu-gcc
    HOSTCC=x86_64-pc-linux-gnu-gcc
    CFLAGS=-O2 -s -m64 -mtune=generic
    CXX=x86_64-pc-linux-gnu-g++
    HOSTCXX=x86_64-pc-linux-gnu-g++
    CXXFLAGS=-O2 -s -m64 -mtune=generic
    AS=x86_64-pc-linux-gnu-as
    HOSTAS=x86_64-pc-linux-gnu-as
    ASFLAGS=-O2 -s -m64 -mtune=generic
    TERM=xterm
    PATH=/bin:/sbin/:/usr/bin:/usr/sbin:/tools/bin
    MAKEFLAGS=-j5
    SED=sed"""


def check():
    cmd('ulimit -s 32768')
    cmd('rm ../gcc/testsuite/g++.dg/pr83239.C')
    cmd('chown -Rv nobody .')
    cmd('su nobody -s /bin/bash -c "PATH=$PATH make -k check"')
    cmd('../contrib/test_summary')


def install():
    pk = get_package()
    do_make(target='install')

    # Create a symlink required by the FHS for "historical" reasons
    cmd(f'ln -sv ../usr/bin/cpp {pk.install_dir}/lib')

    # Many packages use the name cc to call the C compiler
    cmd(f'ln -sv gcc {pk.install_dir}/usr/bin/cc')

    # Add a compatibility symlink to enable building programs with Link Time Optimization (LTO)
    cmd('install -v -dm755 /usr/lib/bfd-plugins')
    cmd(f'ln -sfv ../../libexec/gcc/$(gcc -dumpmachine)/8.2.0/liblto_plugin.so {pk.install_dir}/usr/lib/bfd-plugins/')

    # Sanity checks
    cmd("echo 'int main(){}' > dummy.c")
    cmd("cc dummy.c -v -Wl,--verbose &> dummy.log")
    cmd("readelf -l a.out | grep ': /lib'")
    cmd("grep -o '/usr/lib.*/crt[1in].*succeeded' dummy.log")



    cmd(f'mkdir -p {pk.install_dir}/usr/share/gdb/auto-load/usr/lib')
    cmd(f'mv {pk.install_dir}/usr/lib/*gdb.py {pk.install_dir}/usr/share/gdb/auto-load/usr/lib')


@package(
    id="stable::sys-dev/gcc#8.2.0",
)
def build():
    build_autotools_package(
        fetch=lambda: fetch_url(
            url="http://ftp.gnu.org/gnu/gcc/gcc-8.2.0/gcc-8.2.0.tar.xz",
            sha256="196c3c04ba2613f893283977e6011b2345d1cd1af9abeac58e916b1aab3e0080",
        ),
        configure=configure,
        compile=compile,
        check=check,
    )

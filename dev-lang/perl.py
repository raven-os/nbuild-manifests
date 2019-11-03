#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
from stdlib.split.system import system
from stdlib.template import autotools
from stdlib.template.make import make
from stdlib.manifest import manifest


def split_perl():
    build = stdlib.build.current_build()
    packages = stdlib.split.system.system()

    # Drain the perl5 folder which contains most of the language's necessary files.
    packages['dev-lang/perl'].drain('usr/lib/perl5')

    # Make a couple of symlinks to put libperl.so into a more standard location
    with stdlib.pushd(f"{packages['dev-lang/perl'].wrap_cache}/usr/"):
        libperl = glob.glob(f'lib/perl{build.major}/{build.semver}/*/CORE/libperl.so')[0]

        packages['dev-lang/perl'].make_symlink(f'../{libperl}', 'usr/lib64/libperl.so')
        packages['dev-lang/perl'].make_symlink(f'../{libperl}', f'usr/lib64/libperl.so.{build.major}.{build.minor}')
        packages['dev-lang/perl'].make_symlink(f'../{libperl}', f'usr/lib64/libperl.so.{build.major}.{build.minor}.{build.patch}')

    return packages


@manifest(
    name='perl',
    category='dev-lang',
    description='''
    Practical Extraction and Report Language.
    ''',
    tags=['perl', 'language', 'util', 'script'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.PERL_ARTISTIC],
    upstream_url='https://www.perl.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '5.30.0',
            'fetch': [{
                    'url': 'https://www.cpan.org/src/5.0/perl-5.30.0.tar.gz',
                    'sha256': '851213c754d98ccff042caa40ba7a796b2cee88c5325f121be5cbb61bbf975f2',
                },
            ],
        },
    ],
)
def build(build):
    # Ensures Perl uses the system's zlib and bzip2 libraries.
    os.environ['BUILD_ZLIB'] = 'False'
    os.environ['BUILD_BZIP2'] = '0'

    packages = autotools.build(
        configure=lambda: stdlib.cmd(f'''sh Configure \
            -des                            \
            -Dprefix=/usr                   \
            -Dvendorprefix=/usr             \
            -Dman1dir=/usr/share/man/man1   \
            -Dman3dir=/usr/share/man/man3   \
            -Dman1ext=1perl                 \
            -Dman3ext=3perl                 \
            -Dpager="/usr/bin/less -isR"    \
            -Duseshrplib                    \
            -Dusethreads                    \
        '''),
        split=split_perl,
        check=lambda: make('-k', 'check', fail_ok=True)
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-lang/perl'].requires('raven-os/corefs')

    return packages

#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
import textwrap
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


def patch_bc():
    # TODO FIXME Replace all uses of `ed` by `sed`
    with open('bc/fix-libmath_h', 'w') as f:
        f.write(textwrap.dedent("""\
            #! /bin/bash
            sed -e '1   s/^/{"/' \\
                -e     's/$/",/' \\
                -e '2,$ s/^/"/'  \\
                -e   '$ d'       \\
                -i libmath.h

            sed -e '$ s/$/0}/' \\
                -i libmath.h
        """))

    # TODO FIXME Fix an issue in configure due to missing files in the early stages of Raven-OS
    stdlib.cmd("sed -i -e '/flex/s/as_fn_error/: ;; # &/' configure")


def check_bc():
    stdlib.cmd('echo "quit" | ./bc/bc -l Test/checklib.b', fail_ok=True)


@manifest(
    name='bc',
    category='sys-dev',
    description='''
    An arbitrary precision numeric processing language.
    ''',
    tags=['gnu', 'calculator', 'maths'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V3],
    upstream_url='https://www.gnu.org/software/bc/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.7.1',
            'fetch': [{
                    'url': 'https://ftp.gnu.org/gnu/bc/bc-1.07.1.tar.gz',
                    'sha256': '62adfca89b0a1c0164c2cdca59ca210c1d44c3ffc46daf9931cf4942664cb02a',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--with-readline',
        ),
        patch=patch_bc,
        check=check_bc,
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['sys-dev/bc'].rdepends_on('raven-os/corefs', '*')

    return packages

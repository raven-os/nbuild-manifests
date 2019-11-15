#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import glob
import stdlib
import stdlib.patch
from stdlib.split.drain_all import drain_all_with_doc
from stdlib.template import autotools
from stdlib.manifest import manifest


def patch_vim():
    stdlib.patch.patch_all()

    # Change the default location of the vimrc configuration file to /etc/vimrc
    with open('src/feature.h', 'a') as feature:
        feature.write('#define SYS_VIMRC_FILE "/etc/vimrc"')


def check_vim():
    # Prepare the tests
    stdlib.cmd('chown -Rv nobody .')

    # Run the tests as the nobody user, through 'cat -e' to avoid messing with the building terminal
    stdlib.cmd('su nobody -s /bin/bash -c "LANG=en_US.UTF-8 make -j1 test" | cat -e')


@manifest(
    name='vim',
    category='editor',
    description='''
    Vi IMproved, a powerful text editor.
    ''',
    tags=['vi', 'text', 'editor'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://www.vim.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '8.1.1846',
            'fetch': [{
                    'url': 'https://github.com/vim/vim/archive/v8.1.1846/vim-8.1.1846.tar.gz',
                    'sha256': '68de2854199a396aee19fe34c32c02db5784c76c0334d58b510266436c7529bb',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        patch=patch_vim,
        check=check_vim,
        split=drain_all_with_doc,
    )

    # Make a symlink from vi to vim, both for the binaries and man pages
    packages['editor/vim'].make_symlink('vim', 'usr/bin/vi')
    packages['editor/vim'].make_symlink('vim.1', 'usr/share/man/man1/vi.1')

    with stdlib.pushd(packages['editor/vim'].wrap_cache):
        for path in glob.glob('usr/share/man/*/man1/vim.1'):
            packages['editor/vim'].make_symlink('vim.1', f'{os.path.dirname(path)}/vi.1')

    # Symlink the documentation to a more standard place.
    packages['editor/vim-doc'].make_symlink(f'../vim/vim{build.major}{build.minor}/doc/', 'usr/share/doc/vim')
    packages['editor/vim-doc'].requires('editor/vim')

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['editor/vim'].requires('raven-os/corefs')

    return packages

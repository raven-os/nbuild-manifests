import os

import stdlib
import stdlib.build
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all


def rename_correctly(pkg):
    usr = os.path.join(pkg.wrap_cache, 'usr')
    f1 = os.path.join(usr, 'bin', os.environ['TARGET'] + '-htop')
    f2 = os.path.join(usr, 'share', 'man', 'man1', os.environ['TARGET'] + '-htop.1')
    remove_target_prefix(f1)
    remove_target_prefix(f2)


def remove_target_prefix(path):
    dirname = os.path.dirname(path)
    base = os.path.basename(path)
    new_name = base.replace(os.environ['TARGET'] + '-', '')
    os.rename(path, os.path.join(dirname, new_name))


@manifest(
    name='htop',
    category='sys-apps',
    description='''
    An interactive process viewer.
    ''',
    tags=["ncurses", "process"],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.GPL],
    upstream_url='https://hisham.hm/htop/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.2.0',
            'fetch': [{
                    'url': 'https://hisham.hm/htop/releases/2.2.0/htop-2.2.0.tar.gz',
                    'sha256': 'd9d6826f10ce3887950d709b53ee1d8c1849a70fa38e91d5896ad8cbc6ba3c57',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/ncurses-dev'
    ]
)
def build(build):
    packages = autotools.build(
        split=drain_all
    )

    # remove TARGET prefix on some files (i.e. x86_64-raven-linux-gnu-htop)
    rename_correctly(packages['sys-apps/htop'])

    return packages

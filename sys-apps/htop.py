import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all


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
    return packages

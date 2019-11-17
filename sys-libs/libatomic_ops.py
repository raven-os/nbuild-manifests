import stdlib
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest


@manifest(
    name='libatomic-ops',
    category='dev-libs',
    description='''
    A semi-portable access to hardware-provided atomic memory update operations on a number of architectures.
    ''',
    tags=['atomic', 'hardware', 'memory'],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.MIT, stdlib.license.License.GPL],
    upstream_url='https://github.com/ivmai/libatomic_ops',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '7.6.10',
            'fetch': [{
                'url': 'https://github.com/ivmai/libatomic_ops/releases/download/v7.6.10/libatomic_ops-7.6.10.tar.gz',
                'sha256': '587edf60817f56daf1e1ab38a4b3c729b8e846ff67b4f62a6157183708f099af',
            }],
        },
    ],
)
def build(build):
    packages = autotools.build()
    return packages

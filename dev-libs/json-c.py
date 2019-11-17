import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='json-c',
    category='dev-libs',
    description='''
    A JSON implementation in C.
    ''',
    tags=['json', 'c', 'parser'],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/json-c/json-c',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.13.1',
            'fetch': [{
                    'url': 'https://github.com/json-c/json-c/archive/json-c-0.13.1-20180305.tar.gz',
                    'sha256': '5d867baeb7f540abe8f3265ac18ed7a24f91fe3c5f4fd99ac3caba0708511b90',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()
    return packages

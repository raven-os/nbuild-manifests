import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='json-c',
    category='dev-libs',
    description='''
    JSON-C implements a reference counting object model that allows you to easily construct JSON objects in C, output them as JSON formatted strings and parse JSON formatted strings back into the C representation of JSON objects. It aims to conform to RFC 7159.
    ''',
    tags=['dev', 'json', 'c', 'libs'],
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

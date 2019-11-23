import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='c-ares',
    category='dev-libs',
    description='''
    A C library for asynchronous DNS requests.
    ''',
    tags=['dns', 'c', 'asynchronous'],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://github.com/c-ares/c-ares/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.15.0',
            'fetch': [{
                    'url': 'https://c-ares.haxx.se/download/c-ares-1.15.0.tar.gz',
                    'sha256': '6cdb97871f2930530c97deb7cf5c8fa4be5a0b02c7cea6e7c7667672a39d6852',
                },
            ],
        },
    ],
)
def build(build):
    return autotools.build()

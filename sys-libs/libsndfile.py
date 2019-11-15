import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libsndfile',
    category='sys-libs',
    description='''
    Libsndfile is a C library for reading and writing files containing sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format) through one standard library interface.
    ''',
    tags=['sound', 'library'],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.LGPL_V3],
    upstream_url='http://www.mega-nerd.com/libsndfile/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.0.28',
            'fetch': [{
                    'url': 'http://www.mega-nerd.com/libsndfile/files/libsndfile-1.0.28.tar.gz',
                    'sha256': '1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()
    return packages

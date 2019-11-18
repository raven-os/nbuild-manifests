import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='libspeexdsp',
    category='sys-libs',
    description='''
    Speex is an Open Source/Free Software patent-free audio compression format designed for speech.
    ''',
    tags=['sound', 'speech', 'audio', 'media', 'gnu'],
    maintainer='matteo.melis@epiteh.eu',
    licenses=[stdlib.license.License.BSD],
    upstream_url='https://www.speex.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.2.0',
            'fetch': [{
                    'url': 'https://downloads.us.xiph.org/releases/speex/speexdsp-1.2.0.tar.gz',
                    'sha256': '682042fc6f9bee6294ec453f470dadc26c6ff29b9c9e9ad2ffc1f4312fd64771'
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build()
    return packages

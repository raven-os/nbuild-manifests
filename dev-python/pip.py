#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import stdlib
import textwrap
from stdlib.template import distutils
from stdlib.manifest import manifest

PYTHON_MAJOR = '3'
PYTHON_MINOR = '7'


@manifest(
    name='pip',
    category='dev-python',
    description='''
    The Python Package Installer.
    ''',
    tags=['python', 'python3', 'package', 'manager'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.MIT],
    upstream_url='https://www.python.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '19.2.3',
            'fetch': [{
                    'url': 'https://github.com/pypa/pip/archive/19.2.3.tar.gz',
                    'sha256': 'f9b21137bea9ca1b8f5324bb9af023d69fd352d4b40f64d2867898711902ad26',
                },
            ],
        },
    ],
    build_dependencies=[
        f'dev-lang/python#~{PYTHON_MAJOR}.{PYTHON_MINOR}',
    ],
)
def build(build):
    packages = distutils.build()

    with stdlib.pushd(packages['dev-python/pip'].wrap_cache):
        # Remove the default binaries
        os.remove('usr/bin/pip')
        os.remove(f'usr/bin/pip{PYTHON_MAJOR}')
        os.remove(f'usr/bin/pip{PYTHON_MAJOR}.{PYTHON_MINOR}')

        # Make the pip binary
        with open(f'usr/bin/pip{PYTHON_MAJOR}.{PYTHON_MINOR}', 'w+') as resolv:
            resolv.write(textwrap.dedent(f'''\
                #!/usr/bin/env python{PYTHON_MAJOR}.{PYTHON_MINOR}
                # -*- coding: utf-8 -*-

                import re
                import sys

                from pip._internal import main

                if __name__ == '__main__':
                    sys.argv[0] = re.sub(r'(-script\\.pyw?|\\.exe)?$', '', sys.argv[0])
                    sys.exit(main())
            '''))

        os.chmod(f'usr/bin/pip{PYTHON_MAJOR}.{PYTHON_MINOR}', 0o755)

        # Make the python -> python3 symlink
        packages['dev-python/pip'].make_symlink(f'pip{PYTHON_MAJOR}', 'usr/bin/pip')
        packages['dev-python/pip'].make_symlink(f'pip{PYTHON_MAJOR}.{PYTHON_MINOR}', f'usr/bin/pip{PYTHON_MAJOR}')

    packages['dev-python/pip'].requires('dev-lang/python#~3.7')
    packages['dev-python/pip'].requires('dev-python/setuptools')

    return packages

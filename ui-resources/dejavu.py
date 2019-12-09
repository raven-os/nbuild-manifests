#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import basic
from stdlib.manifest import manifest


@manifest(
    name='dejavu',
    category='ui-resources',
    description='''
    A font family based on the Vera Fonts.
    ''',
    tags=['font', 'vera', 'unicode', 'ttf', 'otf'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.CUSTOM],
    upstream_url='https://dejavu-fonts.github.io/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.37.0',
            'fetch': [{
                'url': 'https://sourceforge.net/projects/dejavu/files/dejavu/2.37/dejavu-fonts-ttf-2.37.tar.bz2',
                'sha256': 'fa9ca4d13871dd122f61258a80d01751d603b4d3ee14095d65453b4e846e17d7',
            }],
        },
    ],
)
def build(build):
    packages = basic.build()

    packages['ui-resources/dejavu'].drain_build_cache('ttf/*.ttf', 'usr/share/fonts/dejavu/')

    return packages

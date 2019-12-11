#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools


@manifest(
    name='hicolor-icon-theme',
    category='ui-resources',
    description='''
    Default fallback theme for implementations of the icon theme specification.
    ''',
    tags=['icon', 'theme'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='https://www.freedesktop.org/wiki/Software/icon-theme/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '0.17.0',
            'fetch': [{
                'url': 'https://icon-theme.freedesktop.org/releases/hicolor-icon-theme-0.17.tar.xz',
                'sha256': '317484352271d18cbbcfac3868eab798d67fff1b8402e740baa6ff41d588a9d8',
            }],
        },
    ]
)
def build(build):
    packages = autotools.build()

    packages['ui-resources/hicolor-icon-theme'].drain('usr/share/icons/hicolor/')

    return packages

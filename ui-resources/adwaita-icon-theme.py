#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.manifest import manifest
from stdlib.template import autotools


@manifest(
    name='adwaita-icon-theme',
    category='ui-resources',
    description='''
    GNOME standard icons.
    ''',
    tags=['icon', 'theme'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL_V3, stdlib.license.License.CUSTOM],
    upstream_url='https://gitlab.gnome.org/GNOME/adwaita-icon-theme',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '3.32.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/adwaita-icon-theme/3.32/adwaita-icon-theme-3.32.0.tar.xz',
                'sha256': '698db6e407bb987baec736c6a30216dfc0317e3ca2403c7adf3a5aa46c193286',
            }],
        },
    ]
)
def build(build):
    packages = autotools.build()

    packages['ui-resources/adwaita-icon-theme'].drain(
        'usr/share/icons/Adwaita/',
        'usr/share/pkgconfig/adwaita-icon-theme.pc'
    )

    return packages

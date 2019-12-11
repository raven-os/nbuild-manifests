#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='glibmm',
    category='dev-libs',
    description='''
    C++ bindings for GLib.
    ''',
    tags=['glib', 'c++', 'bindings'],
    maintainer='doom@raven-os.org',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.gtkmm.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.60.0',
            'fetch': [{
                'url': 'http://ftp.gnome.org/pub/gnome/sources/glibmm/2.60/glibmm-2.60.0.tar.xz',
                'sha256': 'a3a1b1c9805479a16c0018acd84b3bfff23a122aee9e3c5013bb81231aeef2bc',
            }],
        },
    ],
    build_dependencies=[
        'dev-libs/libsigc++-dev',
        'dev-libs/glib-dev',
        'dev-libs/gobject-introspection-dev'
    ]
)
def build(build):
    packages = autotools.build()

    packages['dev-libs/glibmm-dev'].drain(
        'usr/lib64/glibmm-2.4/include/glibmmconfig.h',
        'usr/lib64/glibmm-2.4/proc/',
        'usr/lib64/giomm-2.4/include/giommconfig.h',
    )

    return packages

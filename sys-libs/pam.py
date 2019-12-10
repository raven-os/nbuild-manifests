#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import os
import textwrap
import stdlib
from stdlib.template.configure import configure
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='pam',
    category='sys-libs',
    description='''
    Pluggable Authentication Modules used to enable the local system administrator to choose how applications authenticate users.
    ''',
    tags=['authentication', 'password', 'modules'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL_V2],
    upstream_url='http://linux-pam.org/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '1.3.1',
            'fetch': [{
                    'url': 'https://github.com/linux-pam/linux-pam/releases/download/v1.3.1/Linux-PAM-1.3.1.tar.xz',
                    'sha256': 'eff47a4ecd833fbf18de9686632a70ee8d0794b79aecb217ebd0ce11db4cd0db',
                },
            ],
        },
    ],
)
def build(build):
    packages = autotools.build(
        configure=lambda: configure(
            '--includedir=/usr/include/security/',
            '--enable-securedir=/usr/lib64/security',
        ),
    )

    packages['sys-libs/pam'].drain_package(
        packages['sys-libs/pam-dev'],
        'usr/lib64/security/*.so',
    )

    packages['sys-libs/pam'].drain(
        'usr/lib64/security/pam_filter/'
    )

    # Write a bunch of configuration file
    with stdlib.pushd(packages['sys-libs/pam'].wrap_cache):
        os.makedirs('etc/pam.d/', exist_ok=True)

        with open('etc/pam.d/other', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/other
            #

            auth        required        pam_warn.so
            auth        required        pam_deny.so
            account     required        pam_warn.so
            account     required        pam_deny.so
            password    required        pam_warn.so
            password    required        pam_deny.so
            session     required        pam_warn.so
            session     required        pam_deny.so
            '''))

        with open('etc/pam.d/system-account', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/system-account
            #

            account   required    pam_unix.so
            '''))

        with open('etc/pam.d/system-auth', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/system-auth
            #

            auth      required    pam_unix.so
            '''))

        with open('etc/pam.d/system-session', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/system-session
            #

            session   required    pam_unix.so
            '''))

        with open('etc/pam.d/system-password', 'w+') as other:
            other.write(textwrap.dedent('''\
            #
            # Raven-OS - /etc/pam.d/system-password
            #

            password  required    pam_unix.so       sha512 shadow try_first_pass
            '''))

    return packages

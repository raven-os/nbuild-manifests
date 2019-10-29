#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import stdlib
from stdlib.template.make import make
from stdlib.template import autotools
from stdlib.manifest import manifest


@manifest(
    name='xml-parser',
    category='dev-perl',
    description='''
    An Expat-based XML module.
    ''',
    tags=['perl', 'xml', 'parser', 'expat'],
    maintainer='grange_c@raven-os.org',
    licenses=[stdlib.license.License.GPL, stdlib.license.License.PERL_ARTISTIC],
    upstream_url='https://metacpan.org/release/XML-Parser',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '2.44.0',
            'fetch': [{
                    'url': 'https://cpan.metacpan.org/authors/id/T/TO/TODDR/XML-Parser-2.44.tar.gz',
                    'sha256': '1ae9d07ee9c35326b3d9aad56eae71a6730a73a116b9fe9e8a4758b7cc033216',
                },
            ],
        },
    ],
)
def build(build):

    # TODO FIXME We should create a Perl template when a sufficient amount of
    # packets will be built this way (providing enough information to make a solid
    # perl template)
    #
    # We're doing it manually in the meantime
    #   - Septembre 2019

    packages = autotools.build(
        configure=lambda: stdlib.cmd('perl Makefile.PL'),
        check=lambda: make('test', fail_ok=True),
    )

    packages['dev-perl/xml-parser'].drain('usr/lib/perl5/')

    # We don't want -dev alternatives if they add nothing but mans for perl modules.
    packages['dev-perl/xml-parser'].drain_package(
        packages['dev-perl/xml-parser-dev'],
        '*',
    )

    # Packages member of `raven-os/essentials` should explicitly state all
    # of their dependencies, including indirect ones.
    packages['dev-perl/xml-parser'].rdepends_on('raven-os/corefs', '*')

    return packages

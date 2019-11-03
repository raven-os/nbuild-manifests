#!/usr/bin/env sh

before_install() {
    :
}

after_install() {

    # TODO FIXME: This is a quick, dirty and unflexible solution to generate the
    # certificate configuration file.

    pushd /usr/share/ca-certificates/
        find -name "*.crt" | sed 's#^\./##' > /etc/ca-certificates.conf
    popd

    update-ca-certificates
}

before_remove() {
    :
}

after_remove() {
    :
}

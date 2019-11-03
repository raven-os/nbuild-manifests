#!/usr/bin/env sh

before_install() {
    :
}

after_install() {
    # Generate machine-id
    systemd-machine-id-setup

    # Generate systemd users
    useradd -M -s /usr/bin/nologin systemd-journal
    useradd -M -s /usr/bin/nologin systemd-bus-proxy
    useradd -M -s /usr/bin/nologin systemd-coredump
    useradd -M -s /usr/bin/nologin systemd-journal-gateway
    useradd -M -s /usr/bin/nologin systemd-journal-remote
    useradd -M -s /usr/bin/nologin systemd-journal-upload
    useradd -M -s /usr/bin/nologin systemd-network
    useradd -M -s /usr/bin/nologin systemd-resolve
    useradd -M -s /usr/bin/nologin systemd-timesync
}

before_remove() {
    :
}

after_remove() {
    :
}

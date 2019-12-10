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

    # Make the modifications required to make systemd-logind work
    echo "session   required    pam_loginuid.so" >> /etc/pam.d/system-session
    echo "session   optional    pam_systemd.so" >> /etc/pam.d/system-session
}

before_remove() {
    # Remove the above modifications
    sed '/session   required    pam_loginuid.so/d' -i /etc/pam.d/system-session
    sed '/session   optional    pam_systemd.so/d' -i /etc/pam.d/system-session
}

after_remove() {
    :
}

#!/usr/bin/env sh

before_install() {
    :
}

after_install() {
    systemctl enable dhcpcd

    if [[ $(pidof "systemd") ]]; then
        systemctl daemon-reload
        systemctl start dhcpcd
    fi
}

before_remove() {
    :
}

after_remove() {
    :
}

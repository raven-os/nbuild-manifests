#!/usr/bin/env sh

after_install() {
    groupadd -f polkitd
    useradd -c 'PolicyKit Daemon Owner' -d /etc/polkit-1 -g polkitd -s /bin/false polkitd
}
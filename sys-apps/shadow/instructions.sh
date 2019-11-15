#!/usr/bin/env sh

before_install() {
    :
}

after_install() {
    # Shadow user passwords
    pwconv

    # Shadow group passwords
    grpconv

    # Change permissions of /etc/shadow to give write access to root.
    chmod 640 /etc/shadow
}

before_remove() {
    :
}

after_remove() {
    :
}

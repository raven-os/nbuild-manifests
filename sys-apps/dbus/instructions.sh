#!/usr/bin/env sh

before_install() {
    :
}

after_install() {
    # Generate dbus users
    useradd -M -s /usr/bin/nologin messagebus

    chown -v root:messagebus /usr/lib64/dbus-daemon-launch-helper
    chmod -v 4750 /usr/lib64/dbus-daemon-launch-helper
}

before_remove() {
    :
}

after_remove() {
    :
}

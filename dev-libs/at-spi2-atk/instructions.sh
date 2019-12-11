#!/usr/bin/env sh

after_install() {
    glib-compile-schemas /usr/share/glib-2.0/schemas
}

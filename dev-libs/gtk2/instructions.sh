#!/usr/bin/env sh

after_install() {
    gtk-query-immodules-2.0 --update-cache
}

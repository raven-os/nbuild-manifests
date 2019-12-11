#!/usr/bin/env sh

after_install() {
    gdk-pixbuf-query-loaders --update-cache
}

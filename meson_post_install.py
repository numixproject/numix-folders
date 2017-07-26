#!/usr/bin/env python3
from os import environ, path
from subprocess import call

PREFIX = environ.get('MESON_INSTALL_PREFIX', '/usr/local')
DATA_DIR = path.join(PREFIX, 'share')
ICONS_DIR = path.join(DATA_DIR, 'icons')

if not environ.get('DESTDIR'):
    print('Updating icon cache...')
    call(['gtk-update-icon-cache', '-qtf', path.join(ICONS_DIR, 'hicolor')])
    call(['gtk-update-icon-cache', '-qtf', path.join(ICONS_DIR, 'HighContrast')])
    print("Installing new Schemas")
    call(['glib-compile-schemas', path.join(DATA_DIR, 'glib-2.0/schemas')])

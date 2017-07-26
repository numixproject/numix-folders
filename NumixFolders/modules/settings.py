from gi.repository import Gio, GLib
from .log import Logger


class Schema:
    WINDOW_POSITION = "window-position"
    CURRENT_COLORS = "colors"


class Settings(Gio.Settings):
    KEY = "org.Numix.Folders"
    _instance = None

    def __init__(self):
        Gio.Settings.__init__(self)

    def new():
        gsettings = Gio.Settings.new(Settings.KEY)
        gsettings.__class__ = Settings
        return gsettings

    @staticmethod
    def get_default():
        if Settings._instance is None:
            Settings._instance = Settings.new()
        return Settings._instance

    @property
    def window_position(self):
        x, y = tuple(self.get_value(Schema.WINDOW_POSITION))
        Logger.info('Settings: Window position ({}, {})'.format(x, y))
        return x, y

    @window_position.setter
    def window_position(self, position):
        x, y = position
        Logger.info('Settings: Window position set to ({},{})'.format(x, y))
        position = GLib.Variant('ai', list(position))
        self.set_value(Schema.WINDOW_POSITION, position)

    @property
    def colors(self):
        primary, secondary, symbol = tuple(
            self.get_value(Schema.CURRENT_COLORS))
        print(primary, secondary, symbol)
        Logger.info('Current primary color: '.format(primary))
        Logger.info('Current secondary color: '.format(secondary))
        Logger.info('Current symbol color: '.format(symbol))
        return primary, secondary, symbol

    @colors.setter
    def colors(self, colors):
        primary, secondary, symbol = colors
        Logger.info('Current primary color is set to '.format(primary))
        Logger.info('Current secondary color is set to'.format(secondary))
        Logger.info('Current symbol color is set to '.format(symbol))
        self.set_value(Schema.CURRENT_COLORS, GLib.Variant('as', list(colors)))

from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

from .widgets.window import Window


class Application(Gtk.Application):
    instance = None

    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="org.Numix.Folders",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        window = Window.get_default()
        window.set_application(self)
        self.add_window(window)
        window.show_all()

    @staticmethod
    def get_default():
        if Application.instance is None:
            Application.instance = Application()
        return Application.instance

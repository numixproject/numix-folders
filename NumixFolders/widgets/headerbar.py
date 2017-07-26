from gettext import gettext as _

from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject


class HeaderBar(Gtk.HeaderBar, GObject.GObject):
    instance = None
    __gsignals__ = {
        'apply': (GObject.SignalFlags.RUN_LAST, None, ())
    }

    def __init__(self):
        GObject.GObject.__init__(self)
        Gtk.HeaderBar.__init__(self)
        self.set_show_close_button(True)
        self.set_title(_("Numix Folders"))
        self._build_widget()

    @staticmethod
    def get_default():
        if HeaderBar.instance is None:
            HeaderBar.instance = HeaderBar()
        return HeaderBar.instance

    def _build_widget(self):
        """Create HeaderBar Widget."""
        apply_btn = Gtk.Button()
        apply_btn.set_label(_("Apply"))
        apply_btn.get_style_context().add_class("suggested-action")
        apply_btn.connect("clicked", self._send_apply_signal)
        self.pack_start(apply_btn)

    def _send_apply_signal(self, *args):
        self.emit("apply")

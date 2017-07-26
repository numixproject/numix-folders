import re


from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GObject


class ColorSelector(Gtk.Box, GObject.GObject):

    __gsignals__ = {
        'changed': (GObject.SignalFlags.RUN_LAST, None, (str,))
    }

    def __init__(self, label, default_color):
        GObject.GObject.__init__(self)
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self._build_widget(label, default_color)

    def _build_widget(self, label, default_color):
        """Create the ColorSelector widget."""
        # Color selector label
        self._label = Gtk.Label()
        self._label.set_halign(Gtk.Align.END)
        self._label.set_text(label)
        self.pack_start(self._label, True, True, 6)

        # Color selector entry (shows the hex value of the color)
        self._entry = Gtk.Entry()
        self._entry.set_width_chars(7)
        self._entry.set_max_width_chars(7)
        self._entry.connect("changed", self._do_color_modified)
        self.pack_end(self._entry, False, False, 6)

        # Color selector button
        self._button = Gtk.ColorButton()
        self._button.connect("color-set", self._do_color_set)
        self.pack_end(self._button, False, False, 6)

        self.set_color(default_color)

    def get_color(self):
        return self._entry.get_text()

    def set_color(self, color):
        gdk_color = Gdk.Color.parse(color)
        is_valid = gdk_color[0] == True
        self._entry.set_sensitive(is_valid)
        self._entry.set_text(color)
        if is_valid:
            self._button.set_color(gdk_color[1])

    def _do_color_set(self, color_button):
        color = color_button.get_color().to_string()[0:7]
        self._entry.set_text(color)

    def _do_color_modified(self, entry):
        color = entry.get_text()
        if re.search(r'#[a-fA-F0-9]{6}$', color):
            self.emit("changed", color)
            parsed_color = ColorSelector.parse_color(color)
            # TODO: set the button color !
            entry.get_style_context().remove_class("error")
        else:
            entry.get_style_context().add_class("error")

    @staticmethod
    def parse_color(color):
        color = Gdk.Color.parse(color)
        if color[0]:
            return color[1]
        return None

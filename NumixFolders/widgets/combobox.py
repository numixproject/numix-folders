from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject


class ComboBox(Gtk.Box, GObject.GObject):
    __gsignals__ = {
        'changed': (GObject.SignalFlags.RUN_LAST, None, ())
    }

    def __init__(self):
        GObject.GObject.__init__(self)
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self._build_widget()

    def _build_widget(self):
        """Create the ComboBox with a preview widget."""
        # ComboBox widget
        self._combox = Gtk.ComboBox()
        self._combox.connect("changed", lambda x: self.emit("changed"))
        renderer_text = Gtk.CellRendererText()
        self._combox.pack_start(renderer_text, True)
        self._combox.add_attribute(renderer_text, "text", 0)

        self.pack_start(self._combox, False, False, 6)

    def set_data(self, data):
        # Do it!
        # Color name, primary color, secondary color, symbol color
        liststore = Gtk.ListStore(str, str, str, str)
        for color_name, color in data.items():
            liststore.append([color_name, color[0], color[1], color[2]])
        self._combox.set_model(liststore)

    def get_selected_data(self):
        active_iter = self._combox.get_active_iter()
        if active_iter:
            model = self._combox.get_model()
            return model[active_iter]
        return None

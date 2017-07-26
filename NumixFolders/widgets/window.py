from gettext import gettext as _
import json

from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


from .preview import Preview
from .headerbar import HeaderBar
from .combobox import ComboBox
from .color_selector import ColorSelector
from ..modules.settings import Settings
from ..utils import load_from_resource

class Window(Gtk.ApplicationWindow):
    instance = None

    def __init__(self):
        """Intiate the Gtk Window."""
        Gtk.ApplicationWindow.__init__(self, Gtk.WindowType.TOPLEVEL)
        self.set_resizable(False)
        self.set_border_width(18)
        self.set_default_size(300, 450)
        self.set_size_request(300, 450)
        self.set_title(_("Numix Folders"))
        self.set_icon_name("org.Numix.Folders")
        self.connect("delete-event", self._close)

        self._build_widgets()
        self._fill_content()

        self._restore_state()

    @staticmethod
    def get_default():
        """Return the default instance of Window."""
        if Window.instance is None:
            Window.instance = Window()
        return Window.instance

    def _build_widgets(self):
        """Create the main widgets."""
        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        # Preview Image
        self.preview = Preview.get_default()
        container.pack_start(self.preview, False, False, 6)

        # Styles & Colors comobobox
        hz_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        hz_container.set_halign(Gtk.Align.CENTER)

        self.styles_combobox = ComboBox()
        self.colors_combobox = ComboBox()
        self.colors_combobox.connect("changed", self._do_change_color)

        hz_container.pack_start(self.styles_combobox, False, False, 6)
        hz_container.pack_end(self.colors_combobox, False, False, 6)
        container.pack_start(hz_container, False, False, 6)

        # Primary Color
        colors_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        colors_container.set_valign(Gtk.Align.CENTER)
        colors_container.set_halign(Gtk.Align.CENTER)

        self.primary_color = ColorSelector("Primary", "#66bb6a")
        colors_container.pack_start(self.primary_color, False, False, 6)
        self.secondary_color = ColorSelector("Secondary", "#388e3c")
        colors_container.pack_start(self.secondary_color, False, False, 6)
        self.symbol_color = ColorSelector("Symbol", "#fff8e1")
        colors_container.pack_start(self.symbol_color, False, False, 6)

        container.pack_start(colors_container, False, False, 6)

        # Use a HeaderBar only on support platforms
        if Gtk.MAJOR_VERSION >= 3 and Gtk.MINOR_VERSION >= 14:
            headerbar = HeaderBar.get_default()
            headerbar.connect("apply", self._do_apply)
            self.set_titlebar(headerbar)
        else:
            # Add an apply button on old Gtk versions
            apply_btn = Gtk.Button()
            apply_btn.set_label(_("Apply"))
            apply_btn.get_style_context().add_class("suggested-action")
            apply_btn.connect("clicked", self._do_apply)
            apply_btn.set_halign(Gtk.Align.END)
            container.pack_end(apply_btn, False, False, 0)

        self.add(container)

    def _do_change_color(self, colors_combobox):
        primary, secondary, symbol = colors_combobox.get_selected_data()[1:]
        self.primary_color.set_color(primary)
        self.secondary_color.set_color(secondary)
        self.symbol_color.set_color(symbol)

    def _do_apply(self, *args):
        settings = Settings.get_default()
        primary = self.primary_color.get_color()
        secondary = self.secondary_color.get_color()
        symbol = self.symbol_color.get_color()
        settings.colors = (primary, secondary, symbol)

    def _fill_content(self):
        primary, secondary, symbol = Settings.get_default().colors
        self.primary_color.set_color(primary)
        self.secondary_color.set_color(secondary)
        self.symbol_color.set_color(symbol)

        colors = json.loads(load_from_resource('colors.json'))
        self.colors_combobox.set_data(colors)

    def _restore_state(self):
        x, y = Settings.get_default().window_position
        if x and y:
            self.move(x, y)
        else:
            self.set_position(Gtk.WindowPosition.CENTER)

    def _close(self, *args):
        Settings.get_default().window_position = self.get_position()
        self.destroy()

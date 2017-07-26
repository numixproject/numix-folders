from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk


class Preview(Gtk.Image):
    instance = None

    def __init__(self, preview_icon="folder"):
        """
        Intiate the Preview Image.
        Args:
            @preview_icon (string): The preview icon name/path.
        """
        Gtk.Image.__init__(self)

        self.set_preview(preview_icon)
        self.set_valign(Gtk.Align.CENTER)
        self.set_halign(Gtk.Align.CENTER)

    @staticmethod
    def get_default():
        if Preview.instance is None:
            Preview.instance = Preview()
        return Preview.instance

    def set_preview(self, icon):
        if len(icon.split("/")) > 1:
            print("hey")
        else:
            self.set_from_icon_name(icon, Gtk.IconSize.DIALOG)

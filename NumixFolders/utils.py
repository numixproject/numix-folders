from os import path
from gi.repository import Gio

def load_from_resource(resource_name):
    filename = path.join("resource:///org/Numix/Folders", resource_name)
    obj = Gio.File.new_for_uri(filename)
    content = str(obj.load_contents(None)[1].decode("utf-8"))
    return content

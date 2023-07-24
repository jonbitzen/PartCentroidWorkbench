import os
from .version import __version__
import FreeCADGui

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

FreeCADGui.addIconPath(ICONPATH)
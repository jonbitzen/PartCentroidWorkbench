import os
import FreeCADGui as Gui
import FreeCAD as App
import Draft
from freecad.part_centroid import ICONPATH


class PartCentroidWorkbench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "PartCentroid Workbench"
    ToolTip = "A toolbench to change the centroid of imported models"
    Icon = os.path.join(ICONPATH, "icons8-crosshair-40.png")
    toolbox = ['CursorToCenter', 'CentroidToCursor']

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        from . import commands

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

        Gui.addCommand('CursorToCenter', commands.cursor_to_center.CursorToCenterCommand())
        Gui.addCommand('CentroidToCursor', commands.centroid_to_cursor.CentroidToCursorCommand())
        Gui.addDocumentObserver(self)

    def Activated(self):
        cursor = self.createCursor()
        if cursor is not None:
            cursor.recompute(True)

    def Deactivated(self):
        if App.ActiveDocument is None:
            return
        
        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is not None:
            App.ActiveDocument.removeObject("centroid_cursor")

    def createCursor(self):

        if App.ActiveDocument is None:
            return None

        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is None:
            cursor = Draft.makePoint(
                App.Vector(0,0,0), 
                color=(235/255,164/255,52/255), 
                point_size=10, 
                name="centroid_cursor"
            )
        return cursor

    def slotActivateDocument(self, vobj):
        cursor = self.createCursor()
        if cursor is not None:    
            cursor.ViewObject.Visibility = True
            cursor.recompute(True)
            


Gui.addWorkbench(PartCentroidWorkbench())

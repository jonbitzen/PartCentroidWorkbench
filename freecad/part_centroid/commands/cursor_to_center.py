import FreeCAD
import FreeCADGui


class CursorToCenterCommand(object):

    def __init__(self) -> None:
        pass

    def GetResources(self):
        return {
            'Pixmap':   'icons8-square-border-50.png',
            'MenuText': 'Move cursor to center',
            'ToolTip':  'Move the cursor to the center of the current selection',
        }
    
    def IsActive(self):
        if (FreeCAD.ActiveDocument is not None):
            return True
        return False
    
    def Activated(self):
        print("Do something nice here")
        # OK so we want to:
        #   - get the selection, and create a list of objects and subobjects that we're going
        #     to add to a compound that we will use to get a box centroid
        #     - if the selected object has valid selected subobjects, add those to the compound,
        #       otherwise, just add the whole object
        #     - once we're done adding objects / subobjects, get the compound bbox, get its
        #   - move the cursor to the computed center
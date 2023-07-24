import FreeCAD as App
import FreeCADGui as Gui


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
        if (App.ActiveDocument is not None):
            return True
        return False
    
    def Activated(self):

        selected_objects = Gui.Selection.getSelectionEx()

        # remove the cursor, we dont use it to find a center point        
        selected_objects = \
            [sel_obj for sel_obj in selected_objects if sel_obj.ObjectName != "centroid_cursor" ]

        count = 0
        centroid = App.Vector(0,0,0)

        for selected_object in selected_objects:
            # if we have one or more sub objects selected, iterate over it and
            # add it to the 
            if len(selected_object.SubObjects) > 0:
                for sub_obj in selected_object.SubObjects:
                    count += 1
                    centroid = centroid + sub_obj.BoundBox.Center
            else:
                count += 1
                centroid = centroid + selected_object.Object.BoundBox.Center

        centroid = centroid/count

        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is None:
            return
        
        cursor.Placement.Base = centroid
        
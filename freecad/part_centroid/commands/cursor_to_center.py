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
    
    def GetSelectionObjects(self):
        selected_objects = Gui.Selection.getSelectionEx()

        # remove the cursor, we dont use it to find a center point        
        selected_objects = \
            [sel_obj for sel_obj in selected_objects if sel_obj.ObjectName != "centroid_cursor" ]
        
        return selected_objects

    def IsActive(self):

        if App.ActiveDocument is None:
            return False
        
        if len(self.GetSelectionObjects()) < 1:
            print("CursorToCenterCommand::IsActive - no objects selected")
            return False
        
        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is None:
            print("CursorToCenterCommand::IsActive - no cursor found")
            return False
        return True

    def Activated(self):

        count = 0
        centroid = App.Vector(0,0,0)
        selected_objects = self.GetSelectionObjects()
        for selected_object in selected_objects:
            # if we have one or more sub objects selected, iterate over it and
            # add it to the centroid
            if len(selected_object.SubObjects) > 0:
                for sub_obj in selected_object.SubObjects:
                    count += 1
                    centroid = centroid + sub_obj.BoundBox.Center
            # if we only have an object but no subobjects, then get the center of
            # the object
            else:
                count += 1
                centroid = centroid + selected_object.Object.Shape.BoundBox.Center
        centroid = centroid/count

        cursor = App.ActiveDocument.getObject("centroid_cursor")        
        cursor.Placement.Base = centroid
        cursor.recompute(True)
        
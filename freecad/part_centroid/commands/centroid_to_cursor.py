import FreeCAD as App
import FreeCADGui as Gui


class CentroidToCursorCommand(object):

    def __init__(self) -> None:
        pass

    def GetResources(self):
        return {
            'Pixmap':   'icons8-arrows-to-center-64.png',
            'MenuText': 'Move selection centroid to cursor',
            'ToolTip':  'Moves the selection centroid to the location of the 3D cursor'
        }
    
    def IsActive(self):
        if (App.ActiveDocument is not None):
            return True
        return False
    
    def Activated(self):

        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is None:
            return
        
        selected_objects = Gui.Selection.getSelectionEx()
        # remove the cursor, we dont use it to find a center point        
        selected_objects = \
            [sel_obj.Object for sel_obj in selected_objects if sel_obj.ObjectName != "centroid_cursor" ]
        
        if len(selected_objects) < 1:
            print("No object selected")
            return

        if len(selected_objects) > 1:
            print("Please select only one object to move its centroid")
            return
        
        selected_object = selected_objects[0]

        new_ctr = cursor.Placement.Base

        transform_mat = App.Matrix()
        transform_mat.move(-new_ctr)
        new_shape = selected_object.Shape.transformGeometry(transform_mat)
        selected_object.Shape = new_shape
        selected_object.recompute(True)

        cursor.Placement.Base = App.Vector(0,0,0)
        cursor.recompute(True)

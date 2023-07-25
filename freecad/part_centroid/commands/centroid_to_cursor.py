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
    
    def GetSelectedObjects(self):
        selected_objects = Gui.Selection.getSelectionEx()

        # remove the cursor, we dont use it to find a center point        
        selected_objects = \
            [sel_obj.Object for sel_obj in selected_objects if sel_obj.ObjectName != "centroid_cursor" ]
        
        return selected_objects

    def IsActive(self):
        if App.ActiveDocument is None:
            return False
        
        cursor = App.ActiveDocument.getObject("centroid_cursor")
        if cursor is None:
            return False

        selected_objects = self.GetSelectedObjects()

        if len(selected_objects) < 1:
            print("CentroidToCursorCommand::IsActive - No object selected")
            return False

        if len(selected_objects) > 1:
            print("CentroidToCursorCommand::IsActive - Please select only one object to move its centroid")
            return False

        selected_object = selected_objects[0]

        if selected_object.TypeId != "Part::Feature":
            print("CentroidToCursorCommand::IsActive - PartCentroid only works with Part::Feature objects")
            return False

        return True

    def Activated(self):

        selected_objects = self.GetSelectedObjects()

        selected_object = selected_objects[0]

        cursor = App.ActiveDocument.getObject("centroid_cursor")
        new_ctr = cursor.Placement.Base

        transform_mat = App.Matrix()
        transform_mat.move(-new_ctr)
        new_shape = selected_object.Shape.transformGeometry(transform_mat)
        selected_object.Shape = new_shape
        selected_object.recompute(True)

        cursor.Placement.Base = App.Vector(0,0,0)
        cursor.recompute(True)

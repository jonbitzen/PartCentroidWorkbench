import os
import FreeCADGui as Gui
import FreeCAD as App
from freecad.part_centroid import ICONPATH


class PartCentroidWorkbench(Gui.Workbench):
    """
    class which gets initiated at startup of the gui
    """

    MenuText = "PartCentroid Workbench"
    ToolTip = "A toolbench to change the centroid of imported models"
    Icon = os.path.join(ICONPATH, "icons8-crosshair-40.png")
    toolbox = []

    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        """
        This function is called at the first activation of the workbench.
        here is the place to import all the commands
        """
        # from freecad.part_centroid import my_numpy_function
        # App.Console.PrintMessage("switching to PartCentroid workbench\n")
        # App.Console.PrintMessage("run a numpy function: sqrt(100) = {}\n".format(my_numpy_function.my_foo(100)))

        self.appendToolbar("Tools", self.toolbox)
        self.appendMenu("Tools", self.toolbox)

    def Activated(self):
        '''
        code which should be computed when a user switch to this workbench
        '''
        pass

    def Deactivated(self):
        '''
        code which should be computed when this workbench is deactivated
        '''
        pass


Gui.addWorkbench(PartCentroidWorkbench())

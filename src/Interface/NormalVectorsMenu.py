"""
# Module: NormalVectorsMenu.py
# Description: This module contains the Normal Vectors side widget menu UI for
               manipulation of the normal vectors of model's surfaces.
# Author: Rodrigo de Oliveira Neto.
"""

# Numpy imports:
import numpy

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QLineEdit, QMessageBox, QSpacerItem, QMessageBox

# OpenCASCADE imports:
from OCC.Geom import Geom_Point
from OCC.gp import gp_Ax2, gp_Pnt, gp_Vec, gp_Dir, gp_Pnt2d, gp_Trsf
from OCC.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeOneAxis, BRepPrimAPI_MakeCylinder
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add
from OCC.TopExp import TopExp_Explorer
from OCC.Quantity import Quantity_Color, Quantity_Color_Name
from OCC.AIS import AIS_PointCloud, AIS_Line, AIS_Shape, AIS_ColoredShape

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings
from Discretization.DiscretizeModel import *

class normalVectorsMenu(QWidget):
    """
    # Class: normalVectorsMenu.
    # Description: This class implements functions associated with the normalVectors panel
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        """
        # Method: initUI.
        # Description: This method initializes the User Interface Elements of the Log Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.normalVectorsDescription, self)
        grid.addWidget(label1, 0, 0, 1, 2)

        verticalSpacer = QSpacerItem(20,15)
        grid.addItem(verticalSpacer, 1, 0)

        btn1 = QToolButton()
        btn1.setText(MyStrings.normalVectorsShow)
        grid.addWidget(btn1, 2, 0, 1, 2)
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(120)
        btn1.clicked.connect(lambda: self.create3DNormalVectors(parent))

        btn2 = QToolButton()
        btn2.setText(MyStrings.normalVectorsHide)
        grid.addWidget(btn2, 2, 1, 1, 2)
        btn2.setMinimumHeight(30)
        btn2.setMinimumWidth(120)
        btn2.clicked.connect(lambda: self.hide3DNormalVectors(parent))

        verticalSpacer = QSpacerItem(20,30)
        grid.addItem(verticalSpacer, 3, 0)

        btn1 = QToolButton()
        btn1.setText(MyStrings.selectionModeSolids)
        btn1.clicked.connect(lambda: self.selectSolids(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(130)
        btn1.setEnabled(False)
        grid.addWidget(btn1, 4, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.selectionModeSurfaces)
        btn2.clicked.connect(lambda: self.selectSurfaces(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 4, 1)

        label4 = QLabel(MyStrings.normalVectorsEntitySel, self)
        grid.addWidget(label4, 5, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText(MyStrings.entityPlaceholder)
        grid.addWidget(self.selectedObject, 6, 0, 1, 2)

        btn5 = QToolButton()
        btn5.setText(MyStrings.addEntityOption)
        btn5.clicked.connect(lambda: self.addSelection(parent))
        btn5.setMinimumHeight(30)
        btn5.setMinimumWidth(266)
        grid.addWidget(btn5, 7, 0, 1, 2)

        verticalSpacer = QSpacerItem(20,30)
        grid.addItem(verticalSpacer, 8, 0)

        btn6 = QToolButton()
        btn6.setText(MyStrings.normalVectorsReverse)
        btn6.clicked.connect(lambda: self.reverse3DNormalVectors(parent))
        btn6.setMinimumHeight(50)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 9, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(10, 1)

    def show3DNormalVectors(self, parent):
        """
        # Method: show3DNormalVectors.
        # Description: This complementary method shows the 3D normal vectors of model's surfaces.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        if(parent.normalArrowsShapeList):
            localContext = parent.canvas._display.GetContext().GetObject()
            for i in parent.normalArrowsShapeList:
                localContext.Display(i.GetHandle())

    def hide3DNormalVectors(self, parent):
        """
        # Method: hide3DNormalVectors.
        # Description: This complementary method hides the 3D normal vectors.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeNeutral()
        if(parent.normalArrowsShapeList):
            for i in parent.normalArrowsShapeList:
                parent.canvas._display.Context.Remove(i.GetHandle())
        else:
            return

        if(parent.pointCloudObject):
            restoreCloud(parent)

    def delete3DNormalVectors(self, parent):
        """
        # Method: delete3DNormalVectors.
        # Description: This method deletes the 3D normal vectors of model's surfaces.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        if(parent.normalArrowsShapeList):
            # Deleting every 3D normal vectors
            self.hide3DNormalVectors(parent)
            parent.normalArrowsShapeList = []


    def create3DNormalVectors(self, parent):
        """
        # Method: create3DNormalVectors.
        # Description: This method creates the 3D normal vectors of model's surfaces.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        # Checking if there are 3D arrows in the tupple. If so, they get removed, and then they can get refreshed
        if(parent.normalArrowsShapeList):
            self.delete3DNormalVectors(parent)

        # Defining color properties of the 3D structures
        green = Quantity_Color_Name(0, 1, 0)
        colGreen = Quantity_Color(green)

        # Creating a boundary box with the whole 3D structure to get the order of magnitude of the workpiece
        boundaryBox = Bnd_Box()
        for i in parent.shapeList:
            brepbndlib_Add(i, boundaryBox)
        xMin, yMin, zMin, xMax, yMax, zMax = boundaryBox.Get()
        deltaX = xMax - xMin
        deltaY = yMax - yMin
        deltaZ = zMax - zMin

        # Getting the order of magnitude based on the smaller cartesian dimension of the workpiece
        if(deltaX <= deltaY and deltaX <= deltaZ):
            ref = deltaX
        elif(deltaY <= deltaX and deltaY <= deltaZ):
            ref = deltaY
        else:
            ref = deltaZ

        # Initializing the auxiliar tupples used to create the 3d face-normal arrows
        vecList = []
        pntList = []
        pnts = []
        nmls = []

        # (Auxiliary) discretizating every face of the model with points only in the center regions.
        # These points will be the reference for creation of the 3D Vectors.
        sequence, normals, points = discretizeModel(parent, parent.entitiesObject, 2, 10, 2, 4, True, True, True)

        # Attributing points and vectors references to tupples that will be used to create the 3D Vectors.
        for i in range (len(points)):
            index = 0
            inverseVector = False
            for j in range (len(points[i])):
                pnts.append(points[i][j])
                while index < len(parent.faceSequenceNumbers):
                    if(sequence[i] == parent.faceSequenceNumbers[index]):
                        # Checking in a auxiliary tupple if the normal vector of the correspondent surface has been reversed yet.
                        if(not parent.normVectorsToggle[index]):
                            inverseVector = True
                    index += 1
                # If it wasn't reversed, the reference considered for normal vector will be product of the latest auxiliary discretization
                if(not inverseVector):
                    nmls.append(normals[i][j])
                # If it was reversed, the reference considered for normal vector will be product of the latest auxiliary discretization, but negative
                else:
                    newNormalVec = [numpy.negative(x) for x in normals[i][j]]
                    nmls.append(newNormalVec)

        # Calling the methods to create 3D Vectors in the workspace
        for i in range (len(pnts)):
            p1 = gp_Pnt(pnts[i][0], pnts[i][1], pnts[i][2])
            pntList.append(p1)
            dir = gp_Dir(nmls[i][0], nmls[i][1], nmls[i][2])
            vec = gp_Vec(dir)
            vecList.append(vec)
            ax1 = gp_Ax2(p1, dir)
            # Creating the cylindrical base for the 3D normal vector
            cyl = BRepPrimAPI_MakeCylinder(ax1, ref*0.015, vec.Magnitude()).Shape()

            tnsf = gp_Trsf()
            tnsf.SetTranslation(vec)
            ax1.Transform(tnsf)
            # Creating the conical head of the 3D normal vector
            cone = BRepPrimAPI_MakeCone(ax1, ref*0.03, 0, 4*ref*0.03).Shape()
            AISCyl = AIS_Shape(cyl)
            AIScone = AIS_Shape(cone)
            AISCyl.SetColor(colGreen)
            AIScone.SetColor(colGreen)
            parent.normalArrowsShapeList.append(AISCyl)
            parent.normalArrowsShapeList.append(AIScone)
        self.show3DNormalVectors(parent)

    def toggle(self, a):
        """
        # Method: toggle.
        # Description: This method makes a toggle operation over a bool variable.
        # Parameters: * Bool a = Generic bool variable to be toggled.
        """
        return not a

    def reverse3DNormalVectors(self, parent):
        """
        # Method: reverse3DNormalVectors.
        # Description: This method reverses the 3D normal vectors of model's surfaces.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        try:
            for i in range(len(parent.selectedSequenceNumber)):
                index = 0
                seqNumber = None
                while index < len(parent.faceSequenceNumbers):
                    seqNumber = parent.faceSequenceNumbers[index]
                    if(seqNumber == parent.selectedSequenceNumber[i]):
                        break
                    index += 1
                # Getting the negative values of the selected discretized surface that will have its normal vectors reversed
                aux = [numpy.negative(x) for x in parent.faceNormalVectors[index]]
                newNormalVec = [p for p in [(l[0], l[1], l[2]) for l in aux]]
                # Reversing its normal vectors
                parent.faceNormalVectors[index] = newNormalVec
                # Applying the toggle operation over the appropriate index of normVectorsToggle, to save the occurrence of reversing operation
                parent.normVectorsToggle[index] = self.toggle(parent.normVectorsToggle[index])
            self.delete3DNormalVectors(parent)
            self.create3DNormalVectors(parent)
        # Handling the error of trying to reverse non-discretized surfaces
        except IndexError:
            QMessageBox.information(parent, MyStrings.popupReverseNonDiscNormSurf, MyStrings.popupReverseNonDiscNormSurfDescription, QMessageBox.Ok, QMessageBox.Ok)
            return
        except TypeError:
            QMessageBox.information(parent, MyStrings.popupReverseNonDiscNormSurf, MyStrings.popupReverseNonDiscNormSurfDescription, QMessageBox.Ok, QMessageBox.Ok)
            return

    def selectSurfaces(self, parent):
        """
        # Method: selectSurfaces.
        # Description: Method for activating the Face Selection Mode in the PythonOCC lib.
        The Face Selection Mode allows the selection of each separated face of the CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        # Setting the mode and restoring the point cloud:
        parent.canvas._display.SetSelectionModeFace()
        if(parent.pointCloudObject):
            restoreCloud(parent)

    def addSelection(self, parent):
        """
        # Method: addSelection.
        # Description: Method for adding the current selected shape in the selectedObject
        parameter of the main window. The current selected shape is retrieved by a specific
        function of the PythonOCC lib and is used for comparing with a list of loaded shapes
        of the CAD Model. With this association, it is possible to check the Sequence Number
        associated in the IGES file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        if parent.canvas._display.GetSelectedShapes():
            parent.shapeParameter1 = parent.canvas._display.GetSelectedShapes()
        else:
            return
        parent.selectedShape = []
        parent.selectedSequenceNumber = []
        selectedObjectText = ''
        for shape in parent.shapeParameter1:
            i = 0
            while i < len(parent.shapeList):
                if(shape.IsPartner(parent.shapeList[i])):
                    break
                i += 1
            parent.selectedShape.append(parent.shapeList[i])
            parent.selectedSequenceNumber.append(2*i+1)
            selectedObjectText += str(i+1) + ' '
        self.selectedObject.setText(selectedObjectText)

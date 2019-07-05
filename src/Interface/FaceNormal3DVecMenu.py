
import numpy

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QLineEdit, QMessageBox, QSpacerItem

# OpenCASCADE imports:
from OCC.Geom import Geom_Point
from OCC.gp import gp_Ax2, gp_Pnt, gp_Vec, gp_Dir, gp_Pnt2d
from OCC.BRepPrimAPI import BRepPrimAPI_MakeCone, BRepPrimAPI_MakeOneAxis, BRepPrimAPI_MakeCylinder
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add
from OCC.TopExp import TopExp_Explorer
from OCC.Quantity import Quantity_Color, Quantity_Color_Name
from OCC.AIS import AIS_PointCloud, AIS_Line, AIS_Shape, AIS_ColoredShape

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings

class faceNormal3DVecMenu(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel("Show and manipulate the normal vectors of\n the 3D model.\n", self)
        grid.addWidget(label1, 0, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText("Show 3D vectors")
        grid.addWidget(btn1, 1, 0, 1, 2)
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(100)
        btn1.clicked.connect(lambda: self.create3DNormalVectors(parent))

        btn2 = QToolButton()
        btn2.setText("Hide 3D vectors")
        grid.addWidget(btn2, 1, 1, 1, 2)
        btn2.setMinimumHeight(30)
        btn2.setMinimumWidth(100)
        #btn2.setEnabled(False)
        btn2.clicked.connect(lambda: self.hide3DNormalVectors(parent))

        verticalSpacer = QSpacerItem(20,30)
        grid.addItem(verticalSpacer, 2, 0)

        label4 = QLabel("Select an entity to manipulate its normal vectors:", self)
        grid.addWidget(label4, 3, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText(MyStrings.entityPlaceholder)
        grid.addWidget(self.selectedObject, 4, 0, 1, 2)

        btn3 = QToolButton()
        btn3.setText(MyStrings.selectionModeSurfaces)
        btn3.clicked.connect(lambda: self.selectSurfaces(parent))
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(115)
        grid.addWidget(btn3, 5, 0, 1, 2)

        btn5 = QToolButton()
        btn5.setText(MyStrings.addEntityOption)
        btn5.clicked.connect(lambda: self.addSelection(parent))
        btn5.setMinimumHeight(50)
        btn5.setMinimumWidth(115)
        grid.addWidget(btn5, 5, 1, 1, 2)

        verticalSpacer = QSpacerItem(20,30)
        grid.addItem(verticalSpacer, 6, 0)

        btn6 = QToolButton()
        btn6.setText("Reverse Normal Vectors")
        btn6.clicked.connect(lambda: self.reverse3DNormalVectors(parent))
        btn6.setMinimumHeight(30)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 7, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(8, 1)

    def show3DNormalVectors(self, parent):
        if(parent.normalArrowsShapeList):
            localContext = parent.canvas._display.GetContext().GetObject()
            for i in parent.normalArrowsShapeList:
                # localContext.Display(shapeListCil[i].GetHandle())
                localContext.Display(i.GetHandle())

    def hide3DNormalVectors(self, parent):
        parent.canvas._display.SetSelectionModeNeutral()
        if(parent.normalArrowsShapeList):
            for i in parent.normalArrowsShapeList:
                parent.canvas._display.Context.Remove(i.GetHandle())
        else:
            return

        if(parent.pointCloudObject):
            restoreCloud(parent)

    def delete3DNormalVectors(self, parent):
        if(parent.normalArrowsShapeList):
            # Deleting every face-normal 3D vectors
            self.hide3DNormalVectors(parent)
            parent.normalArrowsShapeList = []


    def create3DNormalVectors(self, parent):
        # Checking if there are 3D arrows in the tupple. If so, they get removed, and then they can get refreshed
        if(parent.normalArrowsShapeList):
            self.delete3DNormalVectors(parent)

        # Defining color properties of the 3D structures
        blue = Quantity_Color_Name(0, 1, 0)
        colBlue = Quantity_Color(blue)

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

        for index in range(len(parent.faceSequenceNumbers)):
            totPoints = len(parent.cloudPointsList[index])
            if(totPoints > 0):
                if(totPoints <5):
                    div = 4
                else:
                    div = 4
                for i in range(div+1):
                    print(i)
                    # xyz = parent.cloudPointsList[index][int((totPoints-1)/i)]
                    xyz = parent.cloudPointsList[index][int((i/4)*(totPoints-1))]
                    normal = parent.faceNormalVectors[index][int((i/4)*(totPoints-1))]
                    p1 = gp_Pnt(xyz[0], xyz[1], xyz[2])
                    pntList.append(p1)
                    dir = gp_Dir(normal[0], normal[1], normal[2])
                    vec = gp_Vec(dir)
                    vecList.append(vec)
                    ax1 = gp_Ax2(p1, dir)
                    cone = BRepPrimAPI_MakeCone(ax1, ref*0.03, 0, 4*ref*0.03).Shape()
                    AIScone = AIS_Shape(cone)
                    AIScone.SetColor(colBlue)
                    parent.normalArrowsShapeList.append(AIScone)
        self.show3DNormalVectors(parent)

    def reverse3DNormalVectors(self, parent):
        for i in range(len(parent.selectedSequenceNumber)):
            index = 0
            seqNumber = None
            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == parent.selectedSequenceNumber[i]):
                    break
                index += 1

            aux = [numpy.negative(x) for x in parent.faceNormalVectors[index]]
            newNormalVec = [p for p in [(l[0], l[1], l[2]) for l in aux]]
            parent.faceNormalVectors[index] = newNormalVec

        self.delete3DNormalVectors(parent)
        self.create3DNormalVectors(parent)


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

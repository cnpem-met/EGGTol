"""
# Module: RotationalnDefectsMenu.py
# Description: This module contains the Translation Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

# Numpy Imports:
from numpy import array, dot

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QLineEdit

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings

# System Imports:
import math

class rotationalDefectsMenu(QWidget):
    """
    # Class: rotationalDefectsMenu
    # Description: This class provides a side menu with some options for rotating some
    group of points in an specific direction that can be defined relative to some basis
    axis, usually located at the face's center of mass.
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
        # Description: This method initializes the User Interface Elements of the Rotational
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.rotationalDefectsDescription)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel(MyStrings.selectionModeHeader, self)
        grid.addWidget(label2, 1, 0, 1, 2)

        label3 = QLabel(MyStrings.askingForSelectionMethod, self)
        grid.addWidget(label3, 2, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText(MyStrings.selectionModeSolids)
        btn1.clicked.connect(lambda: self.selectSolids(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(130)
        btn1.setEnabled(False)
        grid.addWidget(btn1, 3, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.selectionModeSurfaces)
        btn2.clicked.connect(lambda: self.selectSurfaces(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 3, 1)

        label4 = QLabel(MyStrings.askingForEntity, self)
        grid.addWidget(label4, 4, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText(MyStrings.entityPlaceholder)
        grid.addWidget(self.selectedObject, 5, 0, 1, 2)

        btn5 = QToolButton()
        btn5.setText(MyStrings.addEntityOption)
        btn5.clicked.connect(lambda: self.addSelection(parent))
        btn5.setMinimumHeight(30)
        btn5.setMinimumWidth(266)
        grid.addWidget(btn5, 6, 0, 1, 2)

        label5 = QLabel(MyStrings.askingForAngles, self)
        grid.addWidget(label5, 7, 0, 1, 2)

        label6 = QLabel(MyStrings.askingForXValue, self)
        grid.addWidget(label6, 8, 0, 1, 1)

        self.xAngle = QLineEdit()
        grid.addWidget(self.xAngle, 9, 0, 1, 2)

        label7 = QLabel(MyStrings.askingForYValue, self)
        grid.addWidget(label7, 10, 0, 1, 1)

        self.yAngle = QLineEdit()
        grid.addWidget(self.yAngle, 11, 0, 1, 2)

        label8 = QLabel(MyStrings.askingForZValue, self)
        grid.addWidget(label8, 12, 0, 1, 1)

        self.zAngle = QLineEdit()
        grid.addWidget(self.zAngle, 13, 0, 1, 2)

        btn6 = QToolButton()
        btn6.setText(MyStrings.rotationalDefectsApply)
        btn6.clicked.connect(lambda: self.rotatePoints(parent))
        btn6.setMinimumHeight(30)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 14, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(15, 1)

    def rotatePoints(self, parent):
        """
        # Method: rotatePoints.
        # Description: This method applies a rotational defect in the selected
        entity. The parameters of the defect is defined by the configuration done
        at the Rotational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Getting information about the selected surface:
        index = 0
        seqNumber = None
        while index < len(parent.faceSequenceNumbers):
            seqNumber = parent.faceSequenceNumbers[index]
            if(seqNumber == parent.selectedSequenceNumber):
                break
            index += 1

        # Getting the rotation parameters:
        angleX = (float(self.xAngle.displayText())/180) * math.pi
        angleY = (float(self.yAngle.displayText())/180) * math.pi
        angleZ = (float(self.zAngle.displayText())/180) * math.pi

        # Defining the rotation matrix along the three axis:
        matrixX = array([[1, 0, 0],
                         [0, math.cos(angleX), -math.sin(angleX)],
                         [0, math.sin(angleX), math.cos(angleX)]])
        matrixY = array([[math.cos(angleY), 0, math.sin(angleY)],
                         [0, 1, 0],
                         [-math.sin(angleY), 0, math.cos(angleY)]])
        matrixZ = array([[math.cos(angleZ), -math.sin(angleZ), 0],
                         [math.sin(angleZ), math.cos(angleZ), 0],
                         [0, 0, 1]])

        # Apply the boundary box functions to define the center point of a face:
        boundaryBox = Bnd_Box()
        brepbndlib_Add(parent.selectedShape, boundaryBox)
        xMin, yMin, zMin, xMax, yMax, zMax = boundaryBox.Get()
        deltaX = xMax - xMin
        deltaY = yMax - yMin
        deltaZ = zMax - zMin
        centerX = xMin + deltaX/2
        centerY = yMin + deltaY/2
        centerZ = zMin + deltaZ/2

        # Translating the points near to the default basis vector:
        newPointsList = []
        for i in range(len(parent.cloudPointsList[index])):
            point = (parent.cloudPointsList[index][i][0] - centerX,
                     parent.cloudPointsList[index][i][1] - centerY,
                     parent.cloudPointsList[index][i][2] - centerZ)
            newPointsList.append(point)
        parent.cloudPointsList[index] = newPointsList

        # Rotating all the points on the selected surface based on given parameters:
        newPointsList = []
        for i in range(len(parent.cloudPointsList[index])):
            point = array([[parent.cloudPointsList[index][i][0]],
                           [parent.cloudPointsList[index][i][1]],
                           [parent.cloudPointsList[index][i][2]]])
            point = dot(matrixX, point)
            point = dot(matrixY, point)
            point = dot(matrixZ, point)
            newPointsList.append((point[0][0], point[1][0], point[2][0]))
        parent.cloudPointsList[index] = newPointsList

        # Translating the points back to the origianl basis vector:
        newPointsList = []
        for i in range(len(parent.cloudPointsList[index])):
            point = (parent.cloudPointsList[index][i][0] + centerX,
                     parent.cloudPointsList[index][i][1] + centerY,
                     parent.cloudPointsList[index][i][2] + centerZ)
            newPointsList.append(point)
        parent.cloudPointsList[index] = newPointsList

        # Rebuilding the point cloud object in the local context:
        rebuildCloud(parent)

    def selectSolids(self, parent):
        """
        # Method: selectSolids.
        # Description: Method for activating the Neutral Selection Mode in PythonOCC lib.
        The Neutral Selection Mode allows the selection of whole solid CAD models.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        # Setting the mode and restoring the point cloud:
        parent.canvas._display.SetSelectionModeNeutral()
        if(parent.pointCloudObject):
            restoreCloud(parent)

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
            parent.shapeParameter1 = parent.canvas._display.GetSelectedShapes()[-1]
        else:
            return
        i = 0
        while i < len(parent.shapeList):
            if(parent.shapeParameter1.IsPartner(parent.shapeList[i])):
                break
            i += 1
        self.selectedObject.setText(parent.entitiesList[i][0])
        parent.selectedShape = parent.shapeList[i]
        parent.selectedSequenceNumber = 2*i + 1

    def getCenterOfMass(self, parent):
        """
        # Method: getCenterOfMass.
        # Description: This method gets the center of mass of a shape as a tuple of
        coordinates x, y, z of a shape.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

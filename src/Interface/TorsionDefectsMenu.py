"""
# Module: RandomDefectsMenu.py
# Description: This module contains the Random Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Rodrigo de Oliveira Neto.
"""

# System Imports:
import math

# Numpy Imports:
from numpy import array, dot

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QLineEdit

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Interface.SenoidalPatternDefectsMenu import senPattDefectsMenu
from Actions.Functions import *
from Resources.Strings import MyStrings


class torsionDefectsMenu(QWidget):
    """
    # Class: randomDefectsMenu
    # Description: This class provides a side menu with some options for moving some
    group of points in a random direction with a displacement provided.
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
        # Description: This method initializes the User Interface Elements of the Random
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel("Oval deffects menu", self)
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

        btn3 = QToolButton()
        btn3.setText(MyStrings.addEntityOption)
        btn3.clicked.connect(lambda: self.addSelection(parent))
        btn3.setMinimumHeight(30)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 6, 0, 1, 2)

        label5 = QLabel("Enter the Torque:", self)
        grid.addWidget(label5, 7, 0, 1, 2)

        self.pico = QLineEdit()
        grid.addWidget(self.pico, 8, 0, 1, 2)

        label6 = QLabel("Select the longest axis (x, y or z):", self)
        grid.addWidget(label6, 9, 0, 1, 2)

        self.longAxis = QLineEdit()
        grid.addWidget(self.longAxis, 10, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText("Apply torsional defect")
        btn4.clicked.connect(lambda: self.torsionPoints(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 12, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(13, 1)

    def torsionPoints(self, parent):
        """
        # Method: flexionPoints.
        # Description: This method applies flexion manufacturing errors in the selected
        entity. The flexion errors has some rules to follow, defined by the configuration
        done at the flexion Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Getting information about the selected surfaces:
        for i in range(len(parent.selectedSequenceNumber)):
            index = 0
            seqNumber = None
            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == parent.selectedSequenceNumber[i]):
                    break
                index += 1

            # Apply the boundary box functions to define the center point of a face:
            boundaryBox = Bnd_Box()
            brepbndlib_Add(parent.selectedShape[i], boundaryBox)
            xMin, yMin, zMin, xMax, yMax, zMax = boundaryBox.Get()
            deltaX = xMax - xMin
            deltaY = yMax - yMin
            deltaZ = zMax - zMin
            self.centerX = xMin + deltaX/2
            self.centerY = yMin + deltaY/2
            self.centerZ = zMin + deltaZ/2

            # Getting flexion parameters
            long_axis = self.longAxis.displayText()
            #perp_axis = self.perpAxis.displayText()
            T = float(self.pico.displayText().replace(',','.'))
            G = 77.2*10**9
            #EI = 204.8 # Young's module times the Inertia moment of an arbitrary solid

            # Identifying the longitudional axis and verifying if it is a circular beam or not
            if(long_axis == 'z' or long_axis == 'Z'):
                long_axis == 'z'
                if(round(deltaX,4) == round(deltaY, 4)):
                    circBeam = True
                    c = (deltaX/2)*10**(-3)
                else:
                    circBeam = False
            elif(long_axis == 'x' or long_axis == 'X'):
                long_axis = 'x'
                if(round(deltaZ, 4) == round(deltaY, 4)):
                    circBeam = True
                    c = (deltaZ/2)*10**(-3)
                else:
                    circBeam = False
            elif(long_axis == 'y' or long_axis == 'Y'):
                long_axis = 'y'
                if(round(deltaX, 4) == round(deltaZ, 4)):
                    circBeam = True
                    c = (deltaX/2)*10**(-3)
                else:
                    circBeam = False
            else:
                print("Enter the longitudional axis.")
                return

            # Flexioning all the points on the selected surface based on given parameters:
            for i in range(len(parent.cloudPointsList[index])):
                x0 = parent.cloudPointsList[index][i][0]
                y0 = parent.cloudPointsList[index][i][1]
                z0 = parent.cloudPointsList[index][i][2]
                if(long_axis == "x"):
                    L = (x0 - self.centerX)*10**(-3)
                    if(deltaY != 0):
                        a = deltaY
                    else:
                        a = deltaZ
                elif(long_axis == "y"):
                    L = (y0 - self.centerY)*10**(-3)
                    if(deltaX != 0):
                        a = deltaX
                    else:
                        a = deltaZ
                elif(long_axis == "z"):
                    L = (z0 - self.centerZ)*10**(-3)
                    if(deltaX != 0):
                        a = deltaX
                    else:
                        a = deltaY
                if(circBeam):
                    J = (1/2)*math.pi*c**4
                else:
                    c2 = 0.1406
                    a = a*10**(-3)
                    b = a
                    J = c2*a*b**3
                    torsionAngle = T*L/(J*G)
                torsionAngle = 180*torsionAngle/math.pi
                print(torsionAngle)
                self.rotatePoints(parent, torsionAngle, index, i, long_axis)

        # Rebuilding the point cloud object in the local context:
        rebuildCloud(parent)


    def selectSolids(self, parent):
        """
        # Method: selectSolids.
        # Description: Method for activating the Neutral Selection Mode in PythonOCC lib.
        The Neutral Selection Mode allows the selection of whole solid CAD models.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
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

    def rotatePoints(self, parent, torsionAngle, index, i, long_axis):
        if(long_axis == 'x'):
            # Defining the rotation matrix along the three axis:
            rotMatrixX = array([[1, 0, 0],
                             [0, math.cos(torsionAngle), -math.sin(torsionAngle)],
                             [0, math.sin(torsionAngle), math.cos(torsionAngle)]])
            rotMatrixY = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            rotMatrixZ = rotMatrixY
        elif(long_axis == 'y'):
            rotMatrixY = array([[math.cos(torsionAngle), 0, math.sin(torsionAngle)],
                             [0, 1, 0],
                             [-math.sin(torsionAngle), 0, math.cos(torsionAngle)]])
            rotMatrixX = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            rotMatrixZ = rotMatrixX
        elif(long_axis == 'z'):
            rotMatrixZ = array([[math.cos(torsionAngle), -math.sin(torsionAngle), 0],
                             [math.sin(torsionAngle), math.cos(torsionAngle), 0],
                             [0, 0, 1]])
            rotMatrixX = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            rotMatrixY = rotMatrixX

        # Translating the points near to the default basis vector:
        newPointsList = []
        point = (parent.cloudPointsList[index][i][0] - self.centerX,
                 parent.cloudPointsList[index][i][1] - self.centerY,
                 parent.cloudPointsList[index][i][2] - self.centerZ)
        #newPointsList.append(point)
        parent.cloudPointsList[index][i] = point # newPointsList

        # Rotating all the points on the selected surface based on given parameters:
        newPointsList = []
        point = array([[parent.cloudPointsList[index][i][0]],
                       [parent.cloudPointsList[index][i][1]],
                       [parent.cloudPointsList[index][i][2]]])
        point = dot(rotMatrixX, point)
        point = dot(rotMatrixY, point)
        point = dot(rotMatrixZ, point)
        #newPointsList.append((point[0][0], point[1][0], point[2][0]))
        parent.cloudPointsList[index][i] = (point[0][0], point[1][0], point[2][0]) # newPointsList

        # Translating the points back to the origianl basis vector:
        newPointsList = []
        point = (parent.cloudPointsList[index][i][0] + self.centerX,
                 parent.cloudPointsList[index][i][1] + self.centerY,
                 parent.cloudPointsList[index][i][2] + self.centerZ)
        # newPointsList.append(point)
        parent.cloudPointsList[index][i] = point # newPointsList

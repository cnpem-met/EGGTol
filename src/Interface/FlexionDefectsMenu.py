"""
# Module: flexionDefectsMenu.py
# Description: This module contains the flexion Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

from numpy import linspace
import math

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QLineEdit, QComboBox, QMessageBox, QCheckBox, QFrame

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings

class flexionDefectsMenu(QWidget):
    """
    # Class: flexionDefectsMenu
    # Description: This class provides a side menu with some options for moving some
    group of points in a flexion direction with a displacement provided.
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
        # Description: This method initializes the User Interface Elements of the flexion
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.flexionDefectsDescription, self)
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

        frame = QFrame()
        grid.addWidget(frame, 7, 0)

        label5 = QLabel("Longitudional axis:", self)
        grid.addWidget(label5, 8, 0, 1, 1)

        self.longAxisBox = QComboBox()
        grid.addWidget(self.longAxisBox, 8, 1, 1, 2)

        label6 = QLabel("Normal axis:", self)
        grid.addWidget(label6, 9, 0, 1, 1)

        self.perpAxisBox = QComboBox()
        grid.addWidget(self.perpAxisBox, 9, 1, 1, 2)

        axis = ["x", "y", "z"]
        for i in range (3):
            self.longAxisBox.addItem(axis[i])
            self.perpAxisBox.addItem(axis[i])

        self.perpAxisBox.setCurrentIndex(1)

        label7 = QLabel("Maximum deflection (mm):", self)
        grid.addWidget(label7, 10, 0, 1, 1)

        self.maxDef = QLineEdit()
        grid.addWidget(self.maxDef, 11, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText(MyStrings.flexionDefectsApply)
        btn4.clicked.connect(lambda: self.flexionPoints(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 12, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(13, 1)

    def flexionPoints(self, parent):
        """
        # Method: flexionPoints.
        # Description: This method applies flexion manufacturing errors in the selected
        entity. The flexion errors has some rules to follow, defined by the configuration
        done at the flexion Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Declaring the list of index of deviated surface(s)
        selectedEntityList = []

        # Getting information about the selected surfaces:
        for i in range(len(parent.selectedSequenceNumber)):
            index = 0
            seqNumber = None

            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == parent.selectedSequenceNumber[i]):
                    break
                index += 1

            selectedEntityList.append(int(seqNumber/2+0.5))

            # Apply the boundary box functions to define the center point of a face:
            boundaryBox = Bnd_Box()
            brepbndlib_Add(parent.selectedShape[i], boundaryBox)
            xMin, yMin, zMin, xMax, yMax, zMax = boundaryBox.Get()
            deltaX = xMax - xMin
            deltaY = yMax - yMin
            deltaZ = zMax - zMin
            centerX = xMin + deltaX/2
            centerY = yMin + deltaY/2
            centerZ = zMin + deltaZ/2

            # Getting flexion parameters
            long_axis = self.longAxisBox.currentText()
            perp_axis = self.perpAxisBox.currentText()

            # Handling input errors
            try:
                max_def = float(self.maxDef.displayText().replace(',','.'))
            except ValueError:
                QMessageBox.information(parent, "Invalid deflection value",
                                        "Invalid deflection value. Please, try again by inputting a number.", QMessageBox.Ok, QMessageBox.Ok)
                return
            if(long_axis == perp_axis):
                QMessageBox.information(parent, "Invalid Axis combination",
                                        "Invalid axis combination. Please, try again with another combination.", QMessageBox.Ok, QMessageBox.Ok)
                return

            try:
                # Flexioning all the points on the selected surface based on given parameters:
                newPointsList = []
                for i in range(len(parent.cloudPointsList[index])):
                    x0 = parent.cloudPointsList[index][i][0]
                    y0 = parent.cloudPointsList[index][i][1]
                    z0 = parent.cloudPointsList[index][i][2]

                    if(long_axis == "x"):
                        # associating the parameter maximum deformation to the homogeneos load applied
                        q = -(384*max_def)/(5*deltaX**4)
                        # applying deflection formula to the points of selected face
                        v = -(q/24)*(x0-xMin)**4 + (q/12)*deltaX*(x0-xMin)**3 -0.0417*(deltaX**3)*q*(x0-xMin)
                        if(perp_axis == "y"):
                                point = (x0,
                                y0 + v,
                                z0)
                        elif(perp_axis == "z"):
                                point = (x0,
                                y0,
                                z0 + v)
                    elif(long_axis == "y"):
                        q = -(384*max_def)/(5*deltaY**4)
                        v = -(q/24)*(y0-yMin)**4 + (q/12)*deltaY*(y0-yMin)**3 -0.0417*(deltaY**3)*q*(y0-yMin)
                        if(perp_axis == "x"):
                                point = (x0 + v,
                                y0,
                                z0)
                        elif(perp_axis == "z"):
                                point = (x0,
                                y0,
                                z0 + v)
                    elif(long_axis == "z"):
                        q = -(384*max_def)/(5*deltaZ**4)
                        v = -(q/24)*(z0-zMin)**4 + (q/12)*deltaZ*(z0-zMin)**3 -0.0417*(deltaZ**3)*q*(z0-zMin)
                        if(perp_axis == "x"):
                                point = (x0 + v,
                                y0,
                                z0)
                        elif(perp_axis == "y"):
                                point = (x0,
                                y0 + v,
                                z0)

                    newPointsList.append(point)
                parent.cloudPointsList[index] = newPointsList
            # Non-discretized surface error handling
            except IndexError:
                QMessageBox.information(parent, "Invalid selected surface",
                                        "Invalid selected surface. Please, select a discretized one to apply a deviation.", QMessageBox.Ok, QMessageBox.Ok)
                return

        # Building the logbook tupple
        logText = '> [Deviation] Flexion:\n\tEntity List: '+str(selectedEntityList)+'\n\tLong. axis: '+long_axis+'\n\tNorm. axis: '+perp_axis+'\n\tMax. deflection: '+str(max_def)+' mm\n\n'
        parent.logbookList.append(logText)

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
            print("i: "+str(i))
            print(shape.ShapeType())
            parent.selectedShape.append(parent.shapeList[i])
            parent.selectedSequenceNumber.append(2*i+1)
            selectedObjectText += str(i+1) + ' '
        self.selectedObject.setText(selectedObjectText)

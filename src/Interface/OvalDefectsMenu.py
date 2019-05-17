"""
# Module: RandomDefectsMenu.py
# Description: This module contains the Random Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Rodrigo de Oliveira Neto.
"""

# System Imports:
import math
import numpy as np

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QLineEdit, QMessageBox

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Interface.WaveDefectsMenu import waveDefectsMenu
from Actions.Functions import *
from Resources.Strings import MyStrings


class ovalDefectsMenu(QWidget):
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

        label15 = QLabel("Maximum deviation [mm]:", self)
        grid.addWidget(label15, 7, 0, 1, 2)

        self.maxDev = QLineEdit()
        grid.addWidget(self.maxDev, 8, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText("Apply oval defects")
        btn4.clicked.connect(lambda: self.ovalPoints(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 9, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(10, 1)

    def ovalPoints(self, parent):
        """
        # Method: randomPoints.
        # Description: This method applies random manufacturing errors in the selected
        entity. The random errors has some rules to follow, defined by the configuration
        done at the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        try:
            maxDev = float(self.maxDev.displayText().replace(',','.'))
        # Handling input errors
        except ValueError:
            QMessageBox.information(parent, "Invalid input","Invalid input value. Please, enter a valid number.", QMessageBox.Ok, QMessageBox.Ok)
            return

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

            try:
                # calculating parameters to properly generate a sine wave that flattens the rounded surface
                freq = int((len(parent.cloudPointsList[index])/(parent.UVproperty[0] - 1))/2)
                numPointsMainAxis = parent.UVproperty[0] -1

                newPointsList = []
                for i in range(len(parent.cloudPointsList[index])):
                    x0 = parent.cloudPointsList[index][i][0]
                    y0 = parent.cloudPointsList[index][i][1]
                    z0 = parent.cloudPointsList[index][i][2]

                    # applying the sine function to generate a offset to the points
                    offset = maxDev * math.sin(int(i/numPointsMainAxis)/freq*2*math.pi)
                    # shifting points
                    point = (x0 + parent.faceNormalVectors[index][i][0] * offset,
                             y0 + parent.faceNormalVectors[index][i][1] * offset,
                             z0 + parent.faceNormalVectors[index][i][2] * offset)
                    newPointsList.append(point)
                parent.cloudPointsList[index] = newPointsList
            # Handling non-rounded surface error
            except AttributeError:
                QMessageBox.information(parent, "Error","Error: the selected surface isn't parametric (rounded).", QMessageBox.Ok, QMessageBox.Ok)
                return
            # Handling non-discretized surface error
            except IndexError:
                QMessageBox.information(parent, "Invalid selected surface",
                                        "Invalid selected surface. Please, select a discretized one to apply a deviation.", QMessageBox.Ok, QMessageBox.Ok)
                return

        # Building the logbook tupple
        logText = '> [Deviation] Ovalization:\n\tEntity list: '+str(selectedEntityList)+'\n\tMax. Offset: '+str(maxDev)+' mm\n\n'
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
            parent.selectedShape.append(parent.shapeList[i])
            parent.selectedSequenceNumber.append(2*i+1)
            selectedObjectText += str(i+1) + ' '
        self.selectedObject.setText(selectedObjectText)

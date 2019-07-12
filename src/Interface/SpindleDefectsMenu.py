"""
# Module: SpindleDefectsMenu.py
# Description: This module contains the Spindle Defects Side Widget Menu UI, based
               on a Artificial Neural Network Model of diameters deviation in a
               real turning operation.
# Author: Rodrigo de Oliveira Neto.
"""

import neurolab as nl

import numpy
import math

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QLineEdit, QComboBox, QMessageBox, QCheckBox, QFrame, QDoubleSpinBox, QSpacerItem
from PyQt5.QtCore import QRect

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings
from Discretization.DiscretizeModel import *

class spindleDefectsMenu(QWidget):
    """
    # Class: spindlenDefectsMenu
    # Description: This class provides a side menu with some options for simualting
                   a spindle deflection to a curved profile.
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

        label1 = QLabel(MyStrings.spindleDefectsDescription, self)
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
        btn3.setMinimumWidth(350)
        grid.addWidget(btn3, 6, 0, 1, 2)

        frame = QFrame()
        grid.addWidget(frame, 7, 0)

        label5 = QLabel(MyStrings.askingForToolCond, self)
        grid.addWidget(label5, 8, 0, 1, 1)

        self.toolCondBox = QComboBox()
        grid.addWidget(self.toolCondBox, 8, 1, 1, 2)

        axis = ["New", "Worn"]
        for i in range(len(axis)):
            self.toolCondBox.addItem(axis[i])

        self.toolCondBox.setCurrentIndex(1)

        label6 = QLabel(MyStrings.askingForDepth, self)
        grid.addWidget(label6, 9, 0, 1, 1)

        self.depth = QDoubleSpinBox()
        grid.addWidget(self.depth, 9, 1, 1, 2)
        self.depth.setRange(0.5, 2)
        self.depth.setSingleStep(0.1)
        self.depth.setValue(1)

        label7 = QLabel(MyStrings.askingForFeed, self)
        grid.addWidget(label7, 10, 0, 1, 1)

        self.feed = QDoubleSpinBox()
        grid.addWidget(self.feed, 10, 1, 1, 2)
        self.feed.setRange(0.1, 0.2)
        self.feed.setSingleStep(0.01)
        self.feed.setValue(0.15)

        label8 = QLabel(MyStrings.askingForRPM, self)
        grid.addWidget(label8, 11, 0, 1, 1)

        self.spindle = QDoubleSpinBox()
        grid.addWidget(self.spindle, 11, 1, 1, 2)
        self.spindle.setRange(800, 1400)
        self.spindle.setSingleStep(10)
        self.spindle.setValue(1000)

        label9 = QLabel(MyStrings.askingForFixtureName, self)
        grid.addWidget(label9, 12, 0, 1, 2)

        self.fixFaceEdit = QLineEdit()
        self.fixFaceEdit.setReadOnly(True)
        self.fixFaceEdit.setPlaceholderText(MyStrings.askingForFixtureText)
        grid.addWidget(self.fixFaceEdit, 13, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText(MyStrings.FixtureApplyText)
        btn4.clicked.connect(lambda: self.addSelectedFixFace(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(350)
        grid.addWidget(btn4, 14, 0, 1, 2)

        verticalSpacer = QSpacerItem(20,30)
        grid.addItem(verticalSpacer, 15, 0)

        btn5 = QToolButton()
        btn5.setText(MyStrings.spindleDefectsApply)
        btn5.clicked.connect(lambda: self.spindleDefects(parent))
        btn5.setMinimumHeight(30)
        btn5.setMinimumWidth(350)
        grid.addWidget(btn5, 16, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(17, 1)

    def interval_mapping(self, image, from_min, from_max, to_min, to_max):
        """
        # Method: interval_mapping.
        # Description: This method maps a list of numbers from a range to another.
        # Parameters: * List image = input array.
                      * Float from_min, from_max = limits of the range of the input array
                      * Float to_min, to_max = limits of the desired range
        """
        from_range = from_max - from_min
        to_range = to_max - to_min
        scaled = numpy.array((image - from_min) / float(from_range), dtype=float)
        return to_min + (scaled * to_range)

    def spindleDefects(self, parent):
        """
        # Method: spindleDefects.
        # Description: This method applies diameters deviations from a turning operation
                       on a curved discretized surface.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Getting flexion parameters
        tool = self.toolCondBox.currentText()
        depth = self.depth.value()
        feed = self.feed.value()
        spindle = self.spindle.value()

        selectedFacesNumber = parent.selectedSequenceNumber
        selectedShapes = parent.selectedShape

        # Loads the loading window:
        parent.loadingWindow.show()

        # Declaring the list of index of deviated surface(s)
        selectedEntityList = []

        # Getting information about the selected surfaces:
        for i in range(len(selectedFacesNumber)):
            index = 0
            seqNumber = None

            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == selectedFacesNumber[i]):
                    break
                index += 1

            selectedEntityList.append(int(seqNumber/2+0.5))
            U, V = 160, 120
            points1, normals1 = discretizeSurface(parent.entitiesObject[pos(parent.faceSequenceNumbers[i])], parent.entitiesObject, U, V)

            # Calculating the aproximated diameter and length of the curved profile
            numPointsPerim = V-1
            numPointsLength = U-2
            x1,y1,z1 = points1[0]
            x2,y2,z2 = points1[int(numPointsPerim/2)*(numPointsLength+1)]
            x3,y3,z3 = points1[numPointsLength-1]

            diam = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5
            length = ((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)**0.5

            # Extracting the plane equation from the selected referency face

            # First creating a discretized surface with 3 points
            seqFixNumber = self.selectedFixFaceSeqNumber[0]/2+0.5
            points2, normals2 = discretizeFace(parent.entitiesObject[pos(self.selectedFixFaceSeqNumber[0])], parent.entitiesObject, 5, 10, True)
            u = points2[0]
            v = points2[8]
            w = points2[15]
            n = crossProduct(subVec(v,u), subVec(w,u))

            # plane characteristic equation: Ax+By+Cy=D, (A,B,C) = n
            A, B, C = n
            D = A*u[0]+B*u[1]+C*u[2]

            # Acquiring imputed data
            toolCond = self.toolCondBox.currentIndex()
            depth = self.depth.value()
            feed = self.feed.value()
            spindle = self.spindle.value()
            LDratio = length/diam

            # Importing the range from training data, to be used in normalization process of data imputed
            normVec = [(0.0, 1.0), (0.5, 2.0), (0.1, 0.2), (800.0, 1400.0), (2.567, 4.089), (0.07, 0.9), (-0.188, 0.065)]

            # Normalizating imputed data to be inserted on the NN model
            depth = self.interval_mapping(depth, normVec[1][0], normVec[1][1], 0, 1)
            feed = self.interval_mapping(feed, normVec[2][0], normVec[2][1], 0, 1)
            spindle = self.interval_mapping(spindle, normVec[3][0], normVec[3][1], 0, 1)
            LDratio = self.interval_mapping(LDratio, normVec[4][0], normVec[4][1], 0, 1)

            aux = [toolCond, depth, feed, spindle, LDratio]

            # Loading the Trained Neural Network, according to some geometrical specifications
            NN = nl.load("..\\neural networks\\trainedNN_3.net")

            try:
                newPointsList = []
                for i in range(len(parent.cloudPointsList[index])):
                    x0 = parent.cloudPointsList[index][i][0]
                    y0 = parent.cloudPointsList[index][i][1]
                    z0 = parent.cloudPointsList[index][i][2]

                    # Calculating the distance between each point and the plane at the reference face
                    dist = abs(A*x0 + B*y0 + C*z0 - D)/((A**2 + B**2 + C**2)**.5)

                    # Creating LiLratio parameter, and normalizing it
                    LiLratio = dist/length
                    LiLratio = self.interval_mapping(LiLratio, normVec[5][0], normVec[5][1], 0, 1)

                    # Creating the vector with every parameter (normalized) needed to compose the input of the NN model
                    normInput = [[toolCond, depth, feed, spindle, LDratio, LiLratio]]

                    # Obtaining the output (normalized) from the NN model
                    nnOutput = NN.sim(normInput)

                    # Desnormalizing the output
                    nnOutput = self.interval_mapping(nnOutput, 0, 1, normVec[6][0], normVec[6][1])

                    offset = nnOutput[0][0]

                    # Applying the offset for each point
                    point = (x0 + parent.faceNormalVectors[index][i][0] * offset, y0 + parent.faceNormalVectors[index][i][1] * offset, z0 + parent.faceNormalVectors[index][i][2] * offset)

                    newPointsList.append(point)
                parent.cloudPointsList[index] = newPointsList
            # Non-discretized surface error handling
            except IndexError:
                QMessageBox.information(parent, MyStrings.popupInvalidSurf, MyStrings.popupInvalidSurfDescription, QMessageBox.Ok, QMessageBox.Ok)
                return

        # Building the logbook tupple
        logText = '> [Deviation] Spindle:\n\tEntity List: '+str(selectedEntityList)+'\n\tTool condition: '+self.toolCondBox.currentText()+'\n\tDepth of cut: '+str(self.depth.value())+'\n\tFeed rate: '+str(self.feed.value())+'\n\tSpindle speed: '+str(self.spindle.value())+'\n\tFixture entity: '+str(seqFixNumber)+'\n\n'
        parent.logbookList.append(logText)

        # Rebuilding the point cloud object in the local context:
        rebuildCloud(parent)

        # Closes the loading window:
        parent.loadingWindow.close()

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

    def addSelectedFixFace(self, parent):

        if parent.canvas._display.GetSelectedShapes():
            parent.shapeParameter1 = parent.canvas._display.GetSelectedShapes()
        else:
            return
        self.selectedFixFace = []
        self.selectedFixFaceSeqNumber = []
        selectedObjectText = ''
        for shape in parent.shapeParameter1:
            i = 0
            while i < len(parent.shapeList):
                if(shape.IsPartner(parent.shapeList[i])):
                    break
                i += 1
            self.selectedFixFace.append(parent.shapeList[i])
            self.selectedFixFaceSeqNumber.append(2*i+1)
            selectedObjectText += str(i+1) + ' '
        self.fixFaceEdit.setText(selectedObjectText)

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

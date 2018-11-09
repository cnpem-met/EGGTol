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
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QToolButton, QLineEdit

# OpenCASCADE Imports:
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings

class senPattDefectsMenu(QWidget):
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

        label1 = QLabel("", self)
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

        label5 = QLabel(MyStrings.askingForMinimumOffset, self)
        grid.addWidget(label5, 7, 0, 1, 2)

        self.pico = QLineEdit()
        grid.addWidget(self.pico, 8, 0, 1, 2)

        label6 = QLabel("Select the drilling axis:", self)
        grid.addWidget(label6, 9, 0, 1, 2)

        self.drillAxis = QLineEdit()
        grid.addWidget(self.drillAxis, 10, 0, 1, 2)

        label7 = QLabel("Enter the frequency [points/cycle]:", self)
        grid.addWidget(label7, 11, 0, 1, 2)

        self.freq = QLineEdit()
        grid.addWidget(self.freq, 12, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText(MyStrings.randomDefectsApply)
        btn4.clicked.connect(lambda: self.senPattPoints(parent, 0, 0, None, True))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 14, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(15, 1)

    def senPattPoints(self, parent, pico, freq, drillAxis, internalCall):
        """
        # Method: randomPoints.
        # Description: This method applies random manufacturing errors in the selected
        entity. The random errors has some rules to follow, defined by the configuration
        done at the Random Defects Menu side widget.
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
            print(deltaX)
            print(deltaY)
            print(deltaZ)

            # case in which the Senoidal Pattern apply button will call the function, and the Parameters
            # will be imputed at the display boxes and readed at this scope
            if(internalCall):
                if not self.pico.displayText().replace(',','.'):
                    pico = float('0')
                    self.pico.setText('0')
                else:
                    pico = float(self.pico.displayText().replace(',','.'))

                if not self.freq.displayText().replace(',','.'):
                    freq = float('0')
                    self.freq.setText('0')
                else:
                    freq = float(self.freq.displayText().replace(',','.'))

                # Searching for the corresponding drill axis
                if(round(deltaX, 4) == round(deltaY, 4) and round(deltaX, 4) == round(deltaZ, 4)):
                    if(self.drillAxis.displayText() == 'x'):
                        drillAxis = 'x'
                    elif(self.drillAxis.displayText() == 'y'):
                        drillAxis = 'y'
                    elif(self.drillAxis.displayText() == 'z'):
                        drillAxis = 'z'
                    else:
                        print("Eixo de furo não identificado")
                        return
                elif(round(deltaX, 4) == round(deltaY, 4)):
                    drillAxis = 'z'
                elif(round(deltaX, 4) == round(deltaZ, 4)):
                    drillAxis = 'y'
                elif(round(deltaY, 4) == round(deltaZ, 4)):
                    drillAxis = 'x'
                else:
                    print("Face não é circular.")
                    return

            newPointsList = []
            # state of variable z to the first iteration for comparasion. It will be a float type
            # print(parent.cloudPointsList[index])
            drillAxisLength = 0
            z0 = False
            found = False
            z_list = np.array([])
            for i in range(len(parent.cloudPointsList[index])):
                if(drillAxis == 'z'):
                    z = parent.cloudPointsList[index][i][2]
                elif(drillAxis == 'y'):
                    z = parent.cloudPointsList[index][i][1]
                elif(drillAxis == 'x'):
                    z = parent.cloudPointsList[index][i][0]

                if(z != z0):
                    for j in range(len(z_list)):
                        if (round(z, 3) == round(z_list[j], 3)):
                            found = True
                            break
                    if(not found):
                        z_list = np.append(z_list, z)
                        drillAxisLength += 1
                        z0 = z
                    else:
                            break

            if(not internalCall):
                freq = int((len(parent.cloudPointsList[index])/drillAxisLength)/2)
                print("total pontos: "+str(len(parent.cloudPointsList[index])))
                print("drillAxisLength: "+str(drillAxisLength))
                print("freq: "+str(freq))


            for i in range(len(parent.cloudPointsList[index])):
                x0 = parent.cloudPointsList[index][i][0]
                y0 = parent.cloudPointsList[index][i][1]
                z0 = parent.cloudPointsList[index][i][2]

                point = (x0 + parent.faceNormalVectors[index][i][0] * senPattDefectsMenu.getAmplitude(self, i, pico, freq, drillAxisLength),
                         y0 + parent.faceNormalVectors[index][i][1] * senPattDefectsMenu.getAmplitude(self, i, pico, freq, drillAxisLength),
                         z0 + parent.faceNormalVectors[index][i][2] * senPattDefectsMenu.getAmplitude(self, i, pico, freq, drillAxisLength))
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

    def getAmplitude(self, i, Amp, Freq, drillAxisLength):
        """
        # Method: randomOffset.
        # Description: Method for generating a random number between two specified offset values.
        # Parameters: * Float pico = The minimum value for the offset.
                      * Float maxOffset = The maximum value for the offset.
        """
        #value = Amp * math.sin((i/4)*2*math.pi)
        value = Amp * math.sin(int(i/drillAxisLength)/Freq*2*math.pi)
        #value = amp * math.sin(2*math.pi*)
        return value

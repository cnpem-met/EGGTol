"""
# Module: FaceDiscretizeMenu.py
# Description: This module contains the Face Discretization Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

# System Imports:
import sys

# PyQt5 Imports:
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QMessageBox, QLineEdit, \
                            QRadioButton, QSlider

# Local Imports:
from Import.IGESImport import *
from Actions.Functions import *
from Discretization.DiscretizeModel import *
from Resources.Strings import MyStrings

class faceDiscretizeMenu(QWidget):
    """
    # Class: faceDiscretizeMenu.
    # Description: This class provides a side menu with some options to configure
    the Face Discretization process.
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
        # Description: This method initializes the User Interface Elements of the Face
        Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.faceDiscretizeDescription, self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel(MyStrings.selectionModeHeader, self)
        grid.addWidget(label2, 1, 0, 1, 2)

        label3 = QLabel(MyStrings.askingForSelectionMethod)
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

        label4 = QLabel(MyStrings.entitySelectionHeader)
        grid.addWidget(label4, 4, 0, 1, 2)

        label5 = QLabel(MyStrings.askingForEntity, self)
        grid.addWidget(label5, 5, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText(MyStrings.entityPlaceholder)
        grid.addWidget(self.selectedObject, 6, 0, 1, 2)

        btn3 = QToolButton()
        btn3.setText(MyStrings.addEntityOption)
        btn3.clicked.connect(lambda: self.addSelection(parent))
        btn3.setMinimumHeight(30)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 7, 0, 1, 2)

        label4 = QLabel(MyStrings.flatDiscretizationHeader, self)
        grid.addWidget(label4, 8, 0, 1, 2)

        self.gridDiscretization = QRadioButton(MyStrings.gridDiscretization, self)
        self.gridDiscretization.setChecked(True)
        grid.addWidget(self.gridDiscretization, 9, 0, 1, 2)

        self.densityDiscretization = QRadioButton(MyStrings.nonGridDiscretization, self)
        grid.addWidget(self.densityDiscretization, 10, 0, 1, 2)

        label5 = QLabel(MyStrings.askingForNValue, self)
        grid.addWidget(label5, 11, 0, 1, 2)

        self.density = QLineEdit()
        grid.addWidget(self.density, 12, 0, 1, 2)

        label6 = QLabel(MyStrings.askingForPrecision , self)
        grid.addWidget(label6, 13, 0, 1, 2)

        self.precisionSlider = QSlider(Qt.Horizontal, self)
        self.precisionSlider.setMaximum(50)
        self.precisionSlider.setMinimum(10)
        self.precisionSlider.setSingleStep(1)
        self.precisionSlider.valueChanged.connect(self.precisionValueChanged)
        grid.addWidget(self.precisionSlider, 14, 0, 1, 2)

        self.precision = QLineEdit()
        self.precision.setText('10')
        self.precision.textChanged.connect(self.precisionChanged)
        grid.addWidget(self.precision, 15, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText(MyStrings.faceDiscretizeApply)
        btn4.clicked.connect(lambda: self.faceDiscretize(parent, False, None))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 16, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(17, 1)

    def faceDiscretize(self, parent, isInternalCall, paramList):
        """
        # Method: faceDiscretize.
        # Description: Performs the discretization of a selected face in the loaded CAD Model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Check if there is a point cloud present:
        if(parent.pointCloudObject):
            cleanCloud(parent)

        if(isInternalCall):
            selectedFaces = [2*i - 1 for i in paramList[0]]
            if(paramList[1] == "N x N"):
                gridDiscretization = True
            else:
                gridDiscretization = False

            density = paramList[2]
            precision = paramList[3]
        else:
            # Gets all the required parameters from the User Interface:
            gridDiscretization = self.gridDiscretization.isChecked()
            densityDiscretization = self.densityDiscretization.isChecked()

            # Check if the density parameter is OK:
            try:
                density = float(self.density.displayText())
            except:
                QMessageBox.information(parent, MyStrings.popupInvalidNTitle, MyStrings.popupInvalidNDescription,
                                        QMessageBox.Ok, QMessageBox.Ok)
                return

            # Check if the precision parameter is OK:
            try:
                precision = float(self.precision.displayText())
                if(precision > 50 or precision < 10):
                    raise
            except:
                QMessageBox.information(parent, MyStrings.popupInvalidPrecisionTitle,
                                        MyStrings.popupInvalidPrecisionDescription, QMessageBox.Ok, QMessageBox.Ok)
                return

            selectedFaces = parent.selectedSequenceNumber

        # Loads the loading window:
        parent.loadingWindow.show()

        # Checks if at least one surface was selected
        if(selectedFaces):
            # Performs the faceDiscretization using the Discretization package:
            for sequence in selectedFaces:
                points, normals = discretizeFace(parent.entitiesObject[pos(sequence)], parent.entitiesObject,
                                                 density, precision, gridDiscretization)
                parent.faceSequenceNumbers.append(sequence)
                parent.faceNormalVectors.append(normals)
                parent.cloudPointsList.append(points)
                parent.UVproperty.append([None, None])
                parent.normVectorsToggle.append(True)
        else:
            QMessageBox.information(parent, "Surface not selected",
                                    "Surface not selected. Please, select one to generate a point cloud.", QMessageBox.Ok, QMessageBox.Ok)
            return

        # Builds the generated point cloud:
        buildCloud(parent)

        # Updates some properties from the main window:
        parent.activeCloudFile = MyStrings.currentSessionGeneratedPoints

        # Building the logbook tupple
        selectedEntityList = []
        for i in range(len(selectedFaces)):
            index = 0
            seqNumber = None
            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == selectedFaces[i]):
                    break
                index += 1
            selectedEntityList.append(int(seqNumber/2+0.5))

        if(gridDiscretization):
            discrMode = "N x N"
        else:
            discrMode = "N points/mm"
        logText = '> [Discretization] Flat:\n\tEntity list: '+str(selectedEntityList)+'\n\tMode: '+discrMode+'\n\tN Value: '+str(density)+'\n\tPrecision: '+str(precision)+'\n\n'
        parent.logbookList.append(logText)

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

    def precisionValueChanged(self, value):
        self.precision.setText(str(value))

    def precisionChanged(self):
        try:
            if(int(self.precision.displayText()) >= 10 and int(self.precision.displayText()) <= 50):
                self.precisionSlider.setSliderPosition(int(self.precision.displayText()))
        except:
            return

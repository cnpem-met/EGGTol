"""
# Module: TranslationDefectsMenu.py
# Description: This module contains the Translation Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QLineEdit

# Local Imports:
from Actions.Functions import *
from Resources.Strings import MyStrings

class translationDefectsMenu(QWidget):
    """
    # Class: translationDefectsMenu
    # Description: This class provides a side menu with some options for moving some
    group of points in an specific direction, usually, normal to the underlying surface
    which lies the group of points.
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
        # Description: This method initializes the User Interface Elements of the Translational
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.translationDefectsDescription)
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

        label5 = QLabel(MyStrings.askingForDirection, self)
        grid.addWidget(label5, 7, 0, 1, 2)

        btn6 = QToolButton()
        btn6.setText(MyStrings.useNormalDirectionOption)
        btn6.clicked.connect(lambda: self.setNormalDirection(parent))
        btn6.setMinimumHeight(30)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 8, 0, 1, 2)

        label6 = QLabel(MyStrings.askingForXValue, self)
        grid.addWidget(label6, 9, 0, 1, 1)

        self.xDirection = QLineEdit()
        grid.addWidget(self.xDirection, 10, 0, 1, 2)

        label7 = QLabel(MyStrings.askingForYValue, self)
        grid.addWidget(label7, 11, 0, 1, 1)

        self.yDirection = QLineEdit()
        grid.addWidget(self.yDirection, 12, 0, 1, 2)

        label8 = QLabel(MyStrings.askingForZValue, self)
        grid.addWidget(label8, 13, 0, 1, 1)

        self.zDirection = QLineEdit()
        grid.addWidget(self.zDirection, 14, 0, 1, 2)

        label9 = QLabel(MyStrings.askingForOffset, self)
        grid.addWidget(label9, 15, 0, 1, 1)

        self.offset = QLineEdit()
        grid.addWidget(self.offset, 16, 0, 1, 2)

        btn7 = QToolButton()
        btn7.setText(MyStrings.translationDefectsApply)
        btn7.clicked.connect(lambda: self.translatePoints(parent))
        btn7.setMinimumHeight(30)
        btn7.setMinimumWidth(266)
        grid.addWidget(btn7, 17, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(18, 1)

    def normalizePoints(self, parent):
        """
        # Method: normalizePoints
        # Description: This method applies a normalization of the direction
        vector for further use.
        # Parameters: * MainWindow parent = A reference for the main window object
        """

        # Getting information from the interface:
        try:
            x = float(self.xDirection.displayText().replace(',','.'))
            y = float(self.yDirection.displayText().replace(',','.'))
            z = float(self.zDirection.displayText().replace(',','.'))
        except:
            return

        # Evaluating the module value:
        module = (x**2 + y**2 + z**2)**(1/2)
        x, y, z = x/module, y/module, z/module
        self.xDirection.setText(str(x))
        self.yDirection.setText(str(y))
        self.zDirection.setText(str(z))

    def translatePoints(self, parent):
        """
        # Method: translatePoints.
        # Description: This method applies a translational defect in the selected
        entity. The parameters of the defect is defined by the configuration done
        at the Translation Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Normalizing the given direction:
        self.normalizePoints(parent)

        # Getting information about the selected surfaces:
        for sequence in parent.selectedSequenceNumber:
            index = 0
            seqNumber = None
            while index < len(parent.faceSequenceNumbers):
                seqNumber = parent.faceSequenceNumbers[index]
                if(seqNumber == sequence):
                    break
                index += 1

            # Translating all the points on the selected surface based on given parameters:
            newPointsList = []
            offset = float(self.offset.displayText().replace(',','.'))
            if(self.xDirection.displayText() == 'Multiple Values'):
                for i in range(len(parent.cloudPointsList[index])):
                    point = (parent.cloudPointsList[index][i][0] + parent.faceNormalVectors[index][i][0] * offset,
                             parent.cloudPointsList[index][i][1] + parent.faceNormalVectors[index][i][1] * offset,
                             parent.cloudPointsList[index][i][2] + parent.faceNormalVectors[index][i][2] * offset)
                    newPointsList.append(point)
            else:
                for i in range(len(parent.cloudPointsList[index])):
                    #checking for possible imcompabitilities on the displays
                    if not self.xDirection.displayText().replace(',','.'):
                        xDirection = '0'
                        self.xDirection.setText('0')
                    else:
                        xDirection = self.xDirection.displayText().replace(',','.')
                    if not self.yDirection.displayText().replace(',','.'):
                        yDirection = '0'
                        self.yDirection.setText('0')
                    else:
                        yDirection = self.yDirection.displayText().replace(',','.')
                    if not self.zDirection.displayText().replace(',','.'):
                        zDirection = '0'
                        self.zDirection.setText('0')
                    else:
                        zDirection = self.zDirection.displayText().replace(',','.')
                    point = (parent.cloudPointsList[index][i][0] + float(xDirection) * offset,
                             parent.cloudPointsList[index][i][1] + float(yDirection) * offset,
                             parent.cloudPointsList[index][i][2] + float(zDirection) * offset)
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

    def setNormalDirection(self, parent):
        """
        # Method: setNormalDirection.
        # Description: Method for adding the normal direction of a planar face in the Translational
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        self.xDirection.setText('Multiple Values')
        self.yDirection.setText('Multiple Values')
        self.zDirection.setText('Multiple Values')

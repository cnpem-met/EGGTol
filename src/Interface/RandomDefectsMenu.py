"""
# Module: RandomDefectsMenu.py
# Description: This module contains the Random Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

# System Imports:
import sys
import random

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QLineEdit
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import QIcon

# Local Imports:
from Actions.Functions import *

class randomDefectsMenu(QWidget):
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

        label1 = QLabel('Selecione um Modo de Seleção.', self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel('O método de seleção determinará qual tipo de\n' +
                        'entidade será selecionada na tela principal.', self)
        grid.addWidget(label2, 1, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText('Selecionar\nSólidos')
        btn1.clicked.connect(lambda: self.selectSolids(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(130)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Selecionar\nSupefícies')
        btn2.clicked.connect(lambda: self.selectSurfaces(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 2, 1)

        label3 = QLabel('\nSelecione a entidade que deseja aplicar a aleatorização\n' +
                        'do grupo de pontos:', self)
        grid.addWidget(label3, 3, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText('Selecione uma entidade')
        grid.addWidget(self.selectedObject, 4, 0, 1, 2)

        btn3 = QToolButton()
        btn3.setText('Adicionar Entidade Selecionada')
        btn3.clicked.connect(lambda: self.addSelection(parent))
        btn3.setMinimumHeight(30)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 5, 0, 1, 2)

        label4 = QLabel('\nA direção do deslocamento dos pontos será escolhida\n' +
                        'de maneira aleatória.', self)
        grid.addWidget(label4, 6, 0, 1, 2)

        label5 = QLabel('Deslocamento mínimo (em mm):', self)
        grid.addWidget(label5, 7, 0, 1, 2)

        self.minOffset = QLineEdit()
        grid.addWidget(self.minOffset, 8, 0, 1, 2)

        label6 = QLabel('Deslocamento máximo (em mm):', self)
        grid.addWidget(label6, 9, 0, 1, 2)

        self.maxOffset = QLineEdit()
        grid.addWidget(self.maxOffset, 10, 0, 1, 2)

        btn4 = QToolButton()
        btn4.setText('Aplicar Aleatorização aos Pontos')
        btn4.clicked.connect(lambda: self.randomPoints(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 11, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(12, 1)

    def randomPoints(self, parent):
        """
        # Method: randomPoints.
        # Description: This method applies random manufacturing errors in the selected
        entity. The random errors has some rules to follow, defined by the configuration
        done at the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        # Translating all the points based on given random parameters:
        minOffset = float(self.minOffset.displayText())
        maxOffset = float(self.maxOffset.displayText())
        newCloudPointsList = []
        for points in parent.cloudPointsList:
            auxList = []
            for point in points:
                direction = self.randomDirection()
                point = (point[0] + direction[0] * self.randomOffset(minOffset, maxOffset),
                         point[1] + direction[1] * self.randomOffset(minOffset, maxOffset),
                         point[2] + direction[2] * self.randomOffset(minOffset, maxOffset))
                auxList.append(point)
            newCloudPointsList.append(auxList)
        parent.cloudPointsList = newCloudPointsList
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
        restoreCloud(parent)

    def selectSurfaces(self, parent):
        """
        # Method: selectSurfaces.
        # Description: Method for activating the Face Selection Mode in the PythonOCC lib.
        The Face Selection Mode allows the selection of each separated face of the CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeFace()
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

    def randomDirection(self):
        """
        # Method: randomDirection.
        # Description: Method for generating a random and not biased 3D vector.
        """
        direction = [random.gauss(0, 1) for i in range(3)]
        magnitude = sum(x**2 for x in direction)**(0.5)
        normalizedDirection = [x/magnitude for x in direction]
        return normalizedDirection

    def randomOffset(self, minOffset, maxOffset):
        """
        # Method: randomOffset.
        # Description: Method for generating a random number between two specified offset values.
        # Parameters: * Float minOffset = The minimum value for the offset.
                      * Float maxOffset = The maximum value for the offset.
        """
        randomNumber = random.random()
        return minOffset + (maxOffset-minOffset)*randomNumber

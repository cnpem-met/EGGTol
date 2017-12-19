"""
# Module: TranslationDefectsMenu.py
# Description: This module contains the Translation Defects Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QLineEdit
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import QIcon

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

        label3 = QLabel('\nSelecione a entidade que deseja aplicar a translação\n' +
                        'do grupo de pontos:', self)
        grid.addWidget(label3, 3, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText('Selecione uma entidade')
        grid.addWidget(self.selectedObject, 4, 0, 1, 2)

        btn5 = QToolButton()
        btn5.setText('Adicionar Entidade Selecionada')
        btn5.clicked.connect(lambda: self.addSelection(parent))
        btn5.setMinimumHeight(30)
        btn5.setMinimumWidth(266)
        grid.addWidget(btn5, 5, 0, 1, 2)

        label4 = QLabel('\nInforme uma direção (x, y, z) para a translação dos\n' +
                        'pontos na face selecionada', self)
        grid.addWidget(label4, 6, 0, 1, 2)

        btn6 = QToolButton()
        btn6.setText('Utilizar Direção Normal à Superfície')
        btn6.clicked.connect(lambda: self.setNormalDirection(parent))
        btn6.setMinimumHeight(30)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 7, 0, 1, 2)

        label5 = QLabel('Direção X:', self)
        grid.addWidget(label5, 8, 0, 1, 1)

        self.xDirection = QLineEdit()
        grid.addWidget(self.xDirection, 9, 0, 1, 2)

        label6 = QLabel('Direção Y:', self)
        grid.addWidget(label6, 10, 0, 1, 1)

        self.yDirection = QLineEdit()
        grid.addWidget(self.yDirection, 11, 0, 1, 2)

        label6 = QLabel('Direção Z:', self)
        grid.addWidget(label6, 12, 0, 1, 1)

        self.zDirection = QLineEdit()
        grid.addWidget(self.zDirection, 13, 0, 1, 2)

        label7 = QLabel('Deslocamento (em mm):', self)
        grid.addWidget(label7, 14, 0, 1, 1)

        self.offset = QLineEdit()
        grid.addWidget(self.offset, 15, 0, 1, 2)

        btn7 = QToolButton()
        btn7.setText('Aplicar Translação aos Pontos')
        btn7.clicked.connect(lambda: self.translatePoints(parent))
        btn7.setMinimumHeight(30)
        btn7.setMinimumWidth(266)
        grid.addWidget(btn7, 16, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(17, 1)

    def translatePoints(self, parent):
        """
        # Method: translatePoints.
        # Description: This method applies a translational defect in the selected
        entity. The parameters of the defect is defined by the configuration done
        at the Translation Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        pass

    def selectSolids(self, parent):
        """
        # Method: selectSolids.
        # Description: Method for activating the Neutral Selection Mode in PythonOCC lib.
        The Neutral Selection Mode allows the selection of whole solid CAD models.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeNeutral()

    def selectSurfaces(self, parent):
        """
        # Method: selectSurfaces.
        # Description: Method for activating the Face Selection Mode in the PythonOCC lib.
        The Face Selection Mode allows the selection of each separated face of the CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeFace()

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

    def setNormalDirection(self, parent):
        """
        # Method: setNormalDirection.
        # Description: Method for adding the normal direction of a planar face in the Translational
        Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        i = 0
        seqNumber = None
        while i < len(parent.faceSequenceNumbers):
            seqNumber = parent.faceSequenceNumbers[i]
            if(seqNumber == parent.selectedSequenceNumber):
                break
            i += 1

        self.xDirection.setText(str(parent.faceNormalVectors[i][0][0]))
        self.yDirection.setText(str(parent.faceNormalVectors[i][0][1]))
        self.zDirection.setText(str(parent.faceNormalVectors[i][0][2]))

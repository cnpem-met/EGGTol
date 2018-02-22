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
                            QCheckBox, QRadioButton, QSlider

# Local Imports:
from Import.IGESImport import *
from Actions.Functions import *
from Discretization.DiscretizeModel import *

class faceDiscretizeMenu(QWidget):
    """
    # Class: autoDiscretizeMenu.
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

        label1 = QLabel('O método de discretização por faces irá discretizar\n' +
                        'faces individuais conforme uma seleção.\n', self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel('<b>Modo de Seleção</b>', self)
        grid.addWidget(label2, 1, 0, 1, 2)

        label3 = QLabel('O método de seleção deterinará qual tipo de\n' +
                        'entidade será selecionada na tela principal.')
        grid.addWidget(label3, 2, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText('Selecionar\nSólidos')
        btn1.clicked.connect(lambda: self.selectSolids(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(130)
        grid.addWidget(btn1, 3, 0)

        btn2 = QToolButton()
        btn2.setText('Selecionar\nSupefícies')
        btn2.clicked.connect(lambda: self.selectSurfaces(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 3, 1)

        label4 = QLabel('<b><br>Seleção de Entidade</b>')
        grid.addWidget(label4, 4, 0, 1, 2)

        label5 = QLabel('Selecione a entidade que deseja aplicar a translação\n' +
                        'do grupo de pontos:', self)
        grid.addWidget(label5, 5, 0, 1, 2)

        self.selectedObject = QLineEdit()
        self.selectedObject.setReadOnly(True)
        self.selectedObject.setPlaceholderText('Selecione uma entidade')
        grid.addWidget(self.selectedObject, 6, 0, 1, 2)

        btn3 = QToolButton()
        btn3.setText('Adicionar Entidade Selecionada')
        btn3.clicked.connect(lambda: self.addSelection(parent))
        btn3.setMinimumHeight(30)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 7, 0, 1, 2)

        label4 = QLabel('<b><br>Modo de Discretização das Faces Planas:</b>', self)
        grid.addWidget(label4, 8, 0, 1, 2)

        self.gridDiscretization = QRadioButton('Discretização em Grade N x N', self)
        self.gridDiscretization.setChecked(True)
        grid.addWidget(self.gridDiscretization, 9, 0, 1, 2)

        self.densityDiscretization = QRadioButton('Discretização em N pontos/mm', self)
        grid.addWidget(self.densityDiscretization, 10, 0, 1, 2)

        label5 = QLabel('Informe o valor de N para a discretização:', self)
        grid.addWidget(label5, 11, 0, 1, 2)

        self.density = QLineEdit()
        grid.addWidget(self.density, 12, 0, 1, 2)

        label6 = QLabel('Informe a precisão desejada para o enquadramento\n' +
                        'dos pontos em bordas e limites curvos (10 a 50):' , self)
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
        btn4.setText('Aplicar Discretização da Face')
        btn4.clicked.connect(lambda: self.faceDiscretize(parent))
        btn4.setMinimumHeight(30)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 16, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(17, 1)

    def faceDiscretize(self, parent):
        """
        # Method: faceDiscretize.
        # Description: Performs the discretization of a selected face in the loaded CAD Model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        
        # Check if there is a point cloud present:
        if(parent.pointCloudObject):
            cleanCloud(parent)

        # Gets all the required parameters from the User Interface:
        gridDiscretization = self.gridDiscretization.isChecked()
        densityDiscretization = self.densityDiscretization.isChecked()

        # Check if the density parameter is OK:
        try:
            density = float(self.density.displayText())
        except:
            QMessageBox.information(parent, 'Valor inválido para N.',
                                    'O valor escolhido para N não é válido.\n' +
                                    'Utilize um valor numérico positivo que se enquadre ' +
                                    'nas unidades de N pontos/mm ou de uma grade N x N.',
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

        # Check if the precision parameter is OK:
        try:
            precision = float(self.precision.displayText())
            if(precision > 50 or precision < 10):
                raise
        except:
            QMessageBox.information(parent, 'Precisão Inválida.',
                                    'A precisão informada não é válida.\n' +
                                    'Utilize uma precisão positiva que esteja entre ' +
                                    '10 e 50 e tente novamente.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # Loads the loading window:
        parent.loadingWindow.show()

        # Performs the faceDiscretization using the Discretization package:
        sequence = parent.selectedSequenceNumber
        points, normals = discretizeFace(parent.entitiesObject[pos(sequence)], parent.entitiesObject,
                                         density, precision, gridDiscretization)
        parent.faceSequenceNumbers.append(sequence)
        parent.faceNormalVectors.append(normals)
        parent.cloudPointsList.append(points)

        # Builds the generated point cloud:
        buildCloud(parent)

        # Updates some properties from the main window:
        parent.activeCloudFile = 'Pontos Gerados Nesta Sessão'

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

    def precisionValueChanged(self, value):
        self.precision.setText(str(value))

    def precisionChanged(self):
        try:
            if(int(self.precision.displayText()) >= 10 and int(self.precision.displayText()) <= 50):
                self.precisionSlider.setSliderPosition(int(self.precision.displayText()))
        except:
            return

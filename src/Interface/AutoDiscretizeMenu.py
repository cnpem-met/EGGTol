"""
# Module: AutoDiscretizeMenu.py
# Description: This module contains the Auto Discretization Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QLineEdit, \
                            QCheckBox
from PyQt5.QtCore import QCoreApplication, QSize
from OCC.Graphic3d import Graphic3d_ArrayOfPoints
from OCC.AIS import AIS_PointCloud
from Import.IGESImport import *
from Discretization.DiscretizeModel import *

class autoDiscretizeMenu(QWidget):
    """
    # Class: autoDiscretizeMenu.
    # Description: This class provides a side menu with some options to configure
    the Auto Discretization process.
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
        # Description: This method initializes the User Interface Elements of the Auto
        Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel('Discretização Automática.', self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel('O método de discretização automática irá procurar\n' +
                        'pelas faces do modelo e discretizar segundo os\n' +
                        'parâmetros especificados.', self)
        grid.addWidget(label2, 1, 0, 1, 2)

        label3 = QLabel('\nInforme uma densidade de pontos a ser utilizada\n' +
                        'durante o processo (em pontos/cm):', self)
        grid.addWidget(label3, 2, 0, 1, 2)

        self.density = QLineEdit()
        self.density.setPlaceholderText('1')
        grid.addWidget(self.density, 3, 0, 1, 2)

        label3 = QLabel('\nInforme a precisão desejada para o enquadramento\n' +
                        'dos pontos em bordas e limites curvos:' , self)
        grid.addWidget(label3, 4, 0, 1, 2)

        self.precision = QLineEdit()
        self.precision.setPlaceholderText('50')
        grid.addWidget(self.precision, 5, 0, 1, 2)

        self.UVParametric = QCheckBox('Discretizar Superfícies Não-Planas usando\n' +
                                      'Parametrização UV', self)
        grid.addWidget(self.UVParametric, 6, 0, 1, 2)

        label4 = QLabel('Núm. de Parâmetros U:', self)
        grid.addWidget(label4, 7, 0, 1, 2)

        self.UParameter = QLineEdit()
        self.UParameter.setPlaceholderText('10')
        grid.addWidget(self.UParameter, 8, 0, 1, 2)

        label5 = QLabel('Núm. de Parâmetros V:', self)
        grid.addWidget(label5, 9, 0, 1, 2)

        self.VParameter = QLineEdit()
        self.VParameter.setPlaceholderText('10')
        grid.addWidget(self.VParameter, 10, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText('Aplicar Discretização Automática')
        btn1.clicked.connect(lambda: self.autoDiscretize(parent))
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 11, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(12, 1)

    def autoDiscretize(self, parent):
        """
        # Method: autoDiscretize.
        # Description: Performs the discretization process of a loaded CAD Model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Gets the density, precision and U/V parameters from the User Interface:
        density = float(self.density.displayText())/10
        precision = float(self.precision.displayText())
        Uparam = int(self.UParameter.displayText())
        Vparam = int(self.VParameter.displayText())
        useParametric = self.UVParametric.isChecked()

        # Checks if the parameters are valid:
        if(precision > 50 or precision < 1):
            QMessageBox.information(parent, 'Precisão Inválida.',
                                    'A precisão informada não é válida.\n' +
                                    'Utilize uma precisão inteira positiva entre ' +
                                    '1 e 50 e tente novamente.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # Performs the autoDiscretization using the Discretization package:
        file = loadIGESFile(parent.activeCADFile)
        entities = loadEntities(getRawData(file), getRawParameters(file))
        parent.loadingWindow.show()
        sequence, normals, points = discretizeModel(entities, density, precision, Uparam, Vparam, useParametric)
        parent.faceSequenceNumbers = sequence
        parent.faceNormalVectors = normals
        parent.cloudPointsList = points
        generatePcd(parent.cloudPointsList)

        # Displays the generated points over the model using the PythonOCC lib.
        # A CloudData.pcd file is generated inside the tmp/ folder for display purposes.
        pcd_file = open('..\\tmp\\CloudData.pcd', 'r').readlines()[10:]
        pc = Graphic3d_ArrayOfPoints(len(pcd_file))
        for line in pcd_file:
            x, y, z = map(float, line.split())
            pc.AddVertex(x, y, z)
        point_cloud = AIS_PointCloud()
        point_cloud.SetPoints(pc.GetHandle())
        ais_context = parent.canvas._display.GetContext().GetObject()
        ais_context.Display(point_cloud.GetHandle())
        parent.activeCloudFile = '..\\tmp\\CloudData.pcd'
        parent.loadingWindow.close()

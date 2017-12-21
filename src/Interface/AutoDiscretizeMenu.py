"""
# Module: AutoDiscretizeMenu.py
# Description: This module contains the Auto Discretization Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QLineEdit, \
                            QCheckBox, QRadioButton, QSlider
from PyQt5.QtCore import QCoreApplication, QSize, Qt
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

        label1 = QLabel('O método de discretização automática irá procurar\n' +
                        'pelas faces do modelo e discretizar segundo os\n' +
                        'parâmetros especificados.\n', self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel('<b>Modo de Discretização das Faces Planas:</b>', self)
        grid.addWidget(label2, 1, 0, 1, 2)

        self.gridDiscretization = QRadioButton('Discretização em Grade N x N', self)
        self.gridDiscretization.setChecked(True)
        grid.addWidget(self.gridDiscretization, 2, 0, 1, 2)

        self.densityDiscretization = QRadioButton('Discretização em N pontos/mm', self)
        grid.addWidget(self.densityDiscretization, 3, 0, 1, 2)

        label3 = QLabel('Informe o valor de N para a discretização:', self)
        grid.addWidget(label3, 4, 0, 1, 2)

        self.density = QLineEdit()
        grid.addWidget(self.density, 5, 0, 1, 2)

        label4 = QLabel('Informe a precisão desejada para o enquadramento\n' +
                        'dos pontos em bordas e limites curvos (10 a 50):' , self)
        grid.addWidget(label4, 6, 0, 1, 2)

        self.precisionSlider = QSlider(Qt.Horizontal, self)
        self.precisionSlider.setMaximum(50)
        self.precisionSlider.setMinimum(10)
        self.precisionSlider.setSingleStep(1)
        self.precisionSlider.valueChanged.connect(self.precisionValueChanged)
        grid.addWidget(self.precisionSlider, 7, 0, 1, 2)

        self.precision = QLineEdit()
        self.precision.setText('10')
        self.precision.textChanged.connect(self.precisionChanged)
        grid.addWidget(self.precision, 8, 0, 1, 2)

        label5 = QLabel('<b>Modo de Discretização das Faces Não-Planas:</b>', self)
        grid.addWidget(label5, 9, 0, 1, 2)

        self.UVParametric = QCheckBox('Discretizar Superfícies Não-Planas usando\n' +
                                      'Parametrização UV', self)
        self.UVParametric.stateChanged.connect(self.UVParametricChanged)
        grid.addWidget(self.UVParametric, 10, 0, 1, 2)

        label6 = QLabel('Núm. de Parâmetros U:', self)
        grid.addWidget(label6, 11, 0, 1, 2)

        self.UParameter = QLineEdit()
        self.UParameter.setEnabled(False)
        grid.addWidget(self.UParameter, 12, 0, 1, 2)

        label7 = QLabel('Núm. de Parâmetros V:', self)
        grid.addWidget(label7, 13, 0, 1, 2)

        self.VParameter = QLineEdit()
        self.VParameter.setEnabled(False)
        grid.addWidget(self.VParameter, 14, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText('Aplicar Discretização Automática')
        btn1.clicked.connect(lambda: self.autoDiscretize(parent))
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 15, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(16, 1)

    def autoDiscretize(self, parent):
        """
        # Method: autoDiscretize.
        # Description: Performs the discretization process of a loaded CAD Model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Gets all the required parameters from the User Interface:
        gridDiscretization = self.gridDiscretization.isChecked()
        densityDiscretization = self.densityDiscretization.isChecked()
        useParametric = self.UVParametric.isChecked()

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

        # Check if the UParameter and VParameter are OK:
        if(useParametric):
            try:
                Uparam = int(self.UParameter.displayText())
                Vparam = int(self.VParameter.displayText())
            except:
                QMessageBox.information(parent, 'Valores de U e V Inválidos.',
                                        'Os valores U e V para a discretização paramétrica não são válidos.\n' +
                                        'Utilize um valor inteiro positivo e tente novamente.',
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        else:
            Uparam = Vparam = None

        # Performs the autoDiscretization using the Discretization package:
        file = loadIGESFile(parent.activeCADFile)
        entities = loadEntities(getRawData(file), getRawParameters(file))
        parent.loadingWindow.show()
        sequence, normals, points = discretizeModel(entities, density, precision, Uparam, Vparam, useParametric, gridDiscretization)
        parent.faceSequenceNumbers = sequence
        parent.faceNormalVectors = normals
        parent.cloudPointsList = points
        generatePcd(parent.cloudPointsList, '..\\tmp\\CloudData.pcd')

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

    def UVParametricChanged(self):
        self.UParameter.setEnabled(not self.UParameter.isEnabled())
        self.VParameter.setEnabled(not self.VParameter.isEnabled())

    def precisionValueChanged(self, value):
        self.precision.setText(str(value))

    def precisionChanged(self):
        try:
            if(int(self.precision.displayText()) >= 10 and int(self.precision.displayText()) <= 50):
                self.precisionSlider.setSliderPosition(int(self.precision.displayText()))
        except:
            return

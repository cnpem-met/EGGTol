"""
# Module: FaceDiscretizeMenu.py
# Description: This module contains the Face Discretization Side Widget Menu UI
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

        label7 = QLabel('<b><br>Modo de Discretização das Faces Não-Planas:</b>', self)
        grid.addWidget(label7, 16, 0, 1, 2)

        self.UVParametric = QCheckBox('Discretizar Superfícies Não-Planas usando\n' +
                                      'Parametrização UV', self)
        self.UVParametric.stateChanged.connect(self.UVParametricChanged)
        grid.addWidget(self.UVParametric, 17, 0, 1, 2)

        label8 = QLabel('Núm. de Parâmetros U:', self)
        grid.addWidget(label8, 18, 0, 1, 2)

        self.UParameter = QLineEdit()
        self.UParameter.setEnabled(False)
        grid.addWidget(self.UParameter, 19, 0, 1, 2)

        label9 = QLabel('Núm. de Parâmetros V:', self)
        grid.addWidget(label9, 20, 0, 1, 2)

        self.VParameter = QLineEdit()
        self.VParameter.setEnabled(False)
        grid.addWidget(self.VParameter, 21, 0, 1, 2)

        btn3 = QToolButton()
        btn3.setText('Aplicar Discretização Automática')
        btn3.clicked.connect(lambda: self.autoDiscretize(parent))
        btn3.setMinimumHeight(30)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 22, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(23, 1)

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

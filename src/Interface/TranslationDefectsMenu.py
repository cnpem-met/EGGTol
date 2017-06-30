# Module: TranslationDefectsMenu.py
# Description: This module contains the Translation Defects Side Widget Menu UI
# for calling the discretization functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 22, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QLineEdit
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import QIcon

# Class: translationDefectsMenu
# Description: This class provides a side menu with some options for moving some.
# group of points in an specific direction, usually, normal to the underlying
# surface which the group of points are.
class translationDefectsMenu(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
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

    def selectSolids(self, parent):
        parent.canvas._display.SetSelectionModeNeutral()

    def selectSurfaces(self, parent):
        parent.canvas._display.SetSelectionModeFace()
    
    def addSelection(self, parent):
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
            

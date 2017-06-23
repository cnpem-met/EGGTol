# Module: TranslationDefectsMenu.py
# Description: This module contains the Translation Defects Side Widget Menu UI
# for calling the discretization functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 22, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox
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
        btn1.setText('Sólidos')
        btn1.clicked.connect(lambda: self.selectSolids(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(130)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Supefícies')
        btn2.clicked.connect(lambda: self.selectSurfaces(parent))
        btn2.setIconSize(QSize(50, 50))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 2, 1)

        btn3 = QToolButton()
        btn3.setText('Arestas')
        btn3.clicked.connect(lambda: self.selectEdges(parent))
        btn3.setIconSize(QSize(50, 50))
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(130)
        grid.addWidget(btn3, 3, 0)

        btn4 = QToolButton()
        btn4.setText('Vértices')
        btn4.clicked.connect(lambda: self.selectVertices(parent))
        btn4.setIconSize(QSize(50, 50))
        btn4.setMinimumHeight(50)
        btn4.setMinimumWidth(130)
        grid.addWidget(btn4, 3, 1)

        label3 = QLabel('\nSelecione a entidade que deseja aplicar a translação\n' +
                        'do grupo de pontos:', self)
        grid.addWidget(label3, 4, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(5, 1)

    def selectSolids(self, parent):
        parent.canvas._display.SetSelectionModeNeutral()

    def selectSurfaces(self, parent):
        parent.canvas._display.SetSelectionModeFace()

    def selectEdges(self, parent):
        parent.canvas._display.SetSelectionModeEdge()

    def selectVertices(self, parent):
        parent.canvas._display.SetSelectionModeVertex()

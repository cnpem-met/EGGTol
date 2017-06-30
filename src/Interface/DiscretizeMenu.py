# Module: DiscretizeMenu.py
# Description: This module contains the Discretization Side Widget Menu UI
# for calling the discretization functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: May, 04, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox
from PyQt5.QtCore import QCoreApplication, QSize
from PyQt5.QtGui import QIcon
from OCC.Graphic3d import Graphic3d_ArrayOfPoints
from OCC.AIS import AIS_PointCloud
from Actions.ActionList import *

# Class: discretizeMenu
# Description: This class provides a side menu with 6 discretization options.
# Each discretization option calls a function to initiate the discretization process.
class discretizeMenu(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel('Selecione uma opção de discretização.', self)
        grid.addWidget(label1, 0, 0, 1, 2)

        label2 = QLabel('A discretização automática irá trabalhar sobre\n' +
                        'todas as superfícies planas do modelo CAD segundo\n' +
                        'uma determinada precisão.', self)
        grid.addWidget(label2, 1, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText('Discretização\nAutomática')
        btn1.setIcon(QIcon('..\\icons\\cadIcons\\star.png'))
        btn1.setToolButtonStyle(3)
        btn1.clicked.connect(lambda: self.autoDiscretize(parent))
        btn1.setIconSize(QSize(50, 50))
        btn1.setMinimumWidth(130)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Discretização\nde Faces')
        btn2.setIcon(QIcon('..\\icons\\cadIcons\\cube.png'))
        btn2.setToolButtonStyle(3)
        btn2.setIconSize(QSize(50, 50))
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 2, 1)

        btn3 = QToolButton()
        btn3.setText('Discretização\nCilíndrica')
        btn3.setIcon(QIcon('..\\icons\\cadIcons\\cylinder.png'))
        btn3.setToolButtonStyle(3)
        btn3.setIconSize(QSize(50, 50))
        btn3.setMinimumWidth(130)
        grid.addWidget(btn3, 3, 0)

        btn4 = QToolButton()
        btn4.setText('Discretização\nCônica')
        btn4.setIcon(QIcon('..\\icons\\cadIcons\\cone.png'))
        btn4.setToolButtonStyle(3)
        btn4.setIconSize(QSize(50, 50))
        btn4.setMinimumWidth(130)
        grid.addWidget(btn4, 3, 1)

        btn5 = QToolButton()
        btn5.setText('Discretização\nEsférica')
        btn5.setIcon(QIcon('..\\icons\\cadIcons\\circle.png'))
        btn5.setToolButtonStyle(3)
        btn5.setIconSize(QSize(50, 50))
        btn5.setMinimumWidth(130)
        grid.addWidget(btn5, 4, 0)

        btn6 = QToolButton()
        btn6.setText('Discretização\nde Superfície')
        btn6.setIcon(QIcon('..\\icons\\cadIcons\\surface.png'))
        btn6.setToolButtonStyle(3)
        btn6.setIconSize(QSize(50, 50))
        btn6.setMinimumWidth(130)
        grid.addWidget(btn6, 4, 1)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(7, 1)

    def autoDiscretize(self, parent):
        autoDiscretize = autoDiscretizeAction(parent)
        autoDiscretize.autoDiscretizeActionProcedure(parent)

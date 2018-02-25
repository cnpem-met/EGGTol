"""
# Module: DiscretizeMenu.py
# Description: This module contains the Discretization Side Widget Menu UI
for calling the discretization functions.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

# Local Imports:
from Actions.ActionList import *
from Resources.Strings import MyStrings

class discretizeMenu(QWidget):
    """
    # Class: discretizeMenu.
    # Description: This class provides a side menu with 6 discretization options.
    Each discretization option calls a function to initiate the discretization process.
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
        # Description: This method initializes the User Interface Elements of the Discretize
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.discretizeDescription, self)
        grid.addWidget(label1, 0, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText(MyStrings.discretizeOptionAuto)
        btn1.setIcon(QIcon('..\\icons\\cadIcons\\star.png'))
        btn1.setToolButtonStyle(3)
        btn1.clicked.connect(lambda: self.autoDiscretizeMenuProcedure(parent))
        btn1.setIconSize(QSize(50, 50))
        btn1.setMinimumWidth(130)
        grid.addWidget(btn1, 1, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.discretizeOptionFace)
        btn2.setIcon(QIcon('..\\icons\\cadIcons\\cube.png'))
        btn2.setToolButtonStyle(3)
        btn2.clicked.connect(lambda: self.faceDiscretizeMenuProcedure(parent))
        btn2.setIconSize(QSize(50, 50))
        btn2.setMinimumWidth(130)
        grid.addWidget(btn2, 1, 1)

        btn3 = QToolButton()
        btn3.setText(MyStrings.discretizeOptionCylinder)
        btn3.setIcon(QIcon('..\\icons\\cadIcons\\cylinder.png'))
        btn3.setToolButtonStyle(3)
        btn3.setIconSize(QSize(50, 50))
        btn3.setMinimumWidth(130)
        btn3.setEnabled(False)
        grid.addWidget(btn3, 2, 0)

        btn4 = QToolButton()
        btn4.setText(MyStrings.discretizeOptionConic)
        btn4.setIcon(QIcon('..\\icons\\cadIcons\\cone.png'))
        btn4.setToolButtonStyle(3)
        btn4.setIconSize(QSize(50, 50))
        btn4.setMinimumWidth(130)
        btn4.setEnabled(False)
        grid.addWidget(btn4, 2, 1)

        btn5 = QToolButton()
        btn5.setText(MyStrings.discretizeOptionSphere)
        btn5.setIcon(QIcon('..\\icons\\cadIcons\\circle.png'))
        btn5.setToolButtonStyle(3)
        btn5.setIconSize(QSize(50, 50))
        btn5.setMinimumWidth(130)
        btn5.setEnabled(False)
        grid.addWidget(btn5, 3, 0)

        btn6 = QToolButton()
        btn6.setText(MyStrings.discretizeOptionSurface)
        btn6.setIcon(QIcon('..\\icons\\cadIcons\\surface.png'))
        btn6.setToolButtonStyle(3)
        btn6.setIconSize(QSize(50, 50))
        btn6.setMinimumWidth(130)
        btn6.setEnabled(False)
        grid.addWidget(btn6, 3, 1)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid.setRowStretch(4, 1)

    def autoDiscretizeMenuProcedure(self, parent):
        """
        # Method: autoDiscretizeMenuProcedure.
        # Description: This method calls the autoDiscretizeActionProcedure from the
        Actions package for displaying the Auto Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        autoDiscretize = autoDiscretizeAction(parent)
        autoDiscretize.autoDiscretizeActionProcedure(parent)

    def faceDiscretizeMenuProcedure(self, parent):
        """
        # Method: faceDiscretizeMenuProcedure.
        # Description: This method calls the faceDiscretizeActionProcedure from the
        Actions package for displaying the Face Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        faceDiscretize = faceDiscretizeAction(parent)
        faceDiscretize.faceDiscretizeActionProcedure(parent)

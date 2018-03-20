"""
# Module: DefectsMenu.py
# Description: This module contains the Defects Side Widget Menu UI
for calling the defects functions.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton

# Local Imports:
from Actions.ActionList import *
from Resources.Strings import MyStrings

class defectsMenu(QWidget):
    """
    # Class: defectsMenu.
    # Description: This class provides a side menu with 2 types of artificial deviation options.
    Each option calls a method to display the selected deviation insertion side widget.
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
        # Description: This method initializes the User Interface Elements of the Defects Menu
        side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.defectsDescription, self)
        grid.addWidget(label1, 0, 0, 1, 1)

        btn1 = QToolButton()
        btn1.setText(MyStrings.defectsOptionTranslation)
        btn1.clicked.connect(lambda: self.translationDefectsMenuProcedure(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 1, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.defectsOptionRotation)
        btn2.clicked.connect(lambda: self.rotationalDefectsMenuProcedure(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        grid.addWidget(btn2, 2, 0)

        btn3 = QToolButton()
        btn3.setText(MyStrings.defectsOptionRandom)
        btn3.clicked.connect(lambda: self.randomDefectsMenuProcedure(parent))
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 3, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(4, 1)

    def translationDefectsMenuProcedure(self, parent):
        """
        # Method: translationalDefectsMenuProcedure.
        # Description: This method calls the translationalDefectsActionProcedure from the
        Actions package for displaying the Translational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        translation = translationDefectsAction(parent)
        translation.translationDefectsActionProcedure(parent)

    def rotationalDefectsMenuProcedure(self, parent):
        """
        # Method: rotationalDefectsMenuProcedure.
        # Description: This method calls the rotationalDefectsActionProcedure from The
        Actions package for displaying the Rotational Defects Menu side widget.
        # Parameters: * MainWindow parent = A referente for the main window object.
        """
        rotational = rotationalDefectsAction(parent)
        rotational.rotationalDefectsActionProcedure(parent)

    def randomDefectsMenuProcedure(self, parent):
        """
        # Method: randomDefectsMenuProcedure.
        # Description: This method calls the randomDefectsActionProcedure from the
        Actions package for displaying the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        random = randomDefectsAction(parent)
        random.randomDefectsActionProcedure(parent)

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

        btn4 = QToolButton()
        btn4.setText(MyStrings.defectsOptionFlexion)
        btn4.clicked.connect(lambda: self.flexionDefectsMenuProcedure(parent))
        btn4.setMinimumHeight(50)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 4, 0)

        btn4 = QToolButton()
        btn4.setText("Wave Pattern Deflection")
        btn4.clicked.connect(lambda: self.waveDefectsMenuProcedure(parent))
        btn4.setMinimumHeight(50)
        btn4.setMinimumWidth(266)
        grid.addWidget(btn4, 5, 0)

        btn5 = QToolButton()
        btn5.setText("Ovalization of a round surface")
        btn5.clicked.connect(lambda: self.ovalDefectsMenuProcedure(parent))
        btn5.setMinimumHeight(50)
        btn5.setMinimumWidth(266)
        grid.addWidget(btn5, 6, 0)

        btn6 = QToolButton()
        btn6.setText("Twisting a surface")
        btn6.clicked.connect(lambda: self.torsionDefectsMenuProcedure(parent))
        btn6.setMinimumHeight(50)
        btn6.setMinimumWidth(266)
        grid.addWidget(btn6, 7, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(8, 1)

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

    def flexionDefectsMenuProcedure(self, parent):
        """
        # Method: randomDefectsMenuProcedure.
        # Description: This method calls the randomDefectsActionProcedure from the
        Actions package for displaying the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        flexion = flexionDefectsAction(parent)
        flexion.flexionDefectsActionProcedure(parent)

    def waveDefectsMenuProcedure(self, parent):
        """
        # Method: randomDefectsMenuProcedure.
        # Description: This method calls the randomDefectsActionProcedure from the
        Actions package for displaying the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        wave = waveDefectsAction(parent)
        wave.waveDefectsActionProcedure(parent)

    def ovalDefectsMenuProcedure(self, parent):
        """
        # Method: randomDefectsMenuProcedure.
        # Description: This method calls the randomDefectsActionProcedure from the
        Actions package for displaying the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        oval = ovalDefectsAction(parent)
        oval.ovalDefectsActionProcedure(parent)

    def torsionDefectsMenuProcedure(self, parent):
        """
        # Method: randomDefectsMenuProcedure.
        # Description: This method calls the randomDefectsActionProcedure from the
        Actions package for displaying the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        torsion = torsionDefectsAction(parent)
        torsion.torsionDefectsActionProcedure(parent)

"""
# Module: DefectsMenu.py
# Description: This module contains the Defects Side Widget Menu UI
for calling the defects functions.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QSpacerItem
from PyQt5.QtCore import QRect

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

        verticalSpacer = QSpacerItem(20,10)
        grid.addItem(verticalSpacer, 1, 0)

        label2 = QLabel(MyStrings.defectsGeneric, self)
        grid.addWidget(label2, 2, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText(MyStrings.defectsOptionTranslation)
        btn1.clicked.connect(lambda: self.translationDefectsMenuProcedure(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(160)
        grid.addWidget(btn1, 3, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.defectsOptionRotation)
        btn2.clicked.connect(lambda: self.rotationalDefectsMenuProcedure(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(160)
        grid.addWidget(btn2, 3, 1)

        btn3 = QToolButton()
        btn3.setText(MyStrings.defectsOptionRandom)
        btn3.clicked.connect(lambda: self.randomDefectsMenuProcedure(parent))
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(160)
        grid.addWidget(btn3, 4, 0)

        btn4 = QToolButton()
        btn4.setText(MyStrings.defectsOptionPeriodic)
        btn4.clicked.connect(lambda: self.periodicDefectsMenuProcedure(parent))
        btn4.setMinimumHeight(50)
        btn4.setMinimumWidth(160)
        grid.addWidget(btn4, 4, 1)

        btn4 = QToolButton()
        btn4.setText(MyStrings.defectsOptionFlexion)
        btn4.clicked.connect(lambda: self.flexionDefectsMenuProcedure(parent))
        btn4.setMinimumHeight(50)
        btn4.setMinimumWidth(160)
        grid.addWidget(btn4, 5, 0)

        btn6 = QToolButton()
        btn6.setText(MyStrings.defectsOptionTorsion)
        btn6.clicked.connect(lambda: self.torsionDefectsMenuProcedure(parent))
        btn6.setMinimumHeight(50)
        btn6.setMinimumWidth(160)
        grid.addWidget(btn6, 5, 1)

        btn5 = QToolButton()
        btn5.setText(MyStrings.defectsOptionOval)
        btn5.clicked.connect(lambda: self.ovalDefectsMenuProcedure(parent))
        btn5.setMinimumHeight(50)
        btn5.setMinimumWidth(160)
        grid.addWidget(btn5, 6, 0)

        verticalSpacer = QSpacerItem(20,20)
        grid.addItem(verticalSpacer, 7, 0)

        label2 = QLabel(MyStrings.defectsProcess, self)
        grid.addWidget(label2, 8, 0, 1, 2)

        btn7 = QToolButton()
        btn7.setText(MyStrings.defectsOptionSpindle)
        btn7.clicked.connect(lambda: self.spindleDefectsMenuProcedure(parent))
        btn7.setMinimumHeight(50)
        btn7.setMinimumWidth(160)
        grid.addWidget(btn7, 9, 0)

        btn7 = QToolButton()
        btn7.setText(MyStrings.defectsOptionMilling)
        btn7.clicked.connect(lambda: self.spindleDefectsMenuProcedure(parent))
        btn7.setMinimumHeight(50)
        btn7.setMinimumWidth(160)
        btn7.setEnabled(False)
        grid.addWidget(btn7, 9, 1)

        btn7 = QToolButton()
        btn7.setText(MyStrings.defectsOptionAdditive)
        btn7.clicked.connect(lambda: self.spindleDefectsMenuProcedure(parent))
        btn7.setMinimumHeight(50)
        btn7.setMinimumWidth(160)
        btn7.setEnabled(False)
        grid.addWidget(btn7, 10, 0)

        btn7 = QToolButton()
        btn7.setText(MyStrings.defectsOptionRectify)
        btn7.clicked.connect(lambda: self.spindleDefectsMenuProcedure(parent))
        btn7.setMinimumHeight(50)
        btn7.setMinimumWidth(160)
        btn7.setEnabled(False)
        grid.addWidget(btn7, 10, 1)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(11, 1)

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
        # Method: flexionDefectsMenuProcedure.
        # Description: This method calls the flexionDefectsActionProcedure from the
        Actions package for displaying the Flexion Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        flexion = flexionDefectsAction(parent)
        flexion.flexionDefectsActionProcedure(parent)

    def periodicDefectsMenuProcedure(self, parent):
        """
        # Method: periodicDefectsMenuProcedure.
        # Description: This method calls the periodicDefectsActionProcedure from the
        Actions package for displaying the Periodic Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        periodic = periodicDefectsAction(parent)
        periodic.periodicDefectsActionProcedure(parent)

    def ovalDefectsMenuProcedure(self, parent):
        """
        # Method: ovalDefectsMenuProcedure.
        # Description: This method calls the ovalDefectsActionProcedure from the
        Actions package for displaying the Oval Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        oval = ovalDefectsAction(parent)
        oval.ovalDefectsActionProcedure(parent)

    def torsionDefectsMenuProcedure(self, parent):
        """
        # Method: torsionDefectsMenuProcedure.
        # Description: This method calls the torsionDefectsActionProcedure from the
        Actions package for displaying the Torsion Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        torsion = torsionDefectsAction(parent)
        torsion.torsionDefectsActionProcedure(parent)

    def spindleDefectsMenuProcedure(self, parent):
        """
        # Method: spindleDefectsMenuProcedure.
        # Description: This method calls the spindleDefectsActionProcedure from the
        Actions package for displaying the Spindle Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        spindle = spindleDefectsAction(parent)
        spindle.spindleDefectsActionProcedure(parent)

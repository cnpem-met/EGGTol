"""
# Module: WelcomeMenu.py
# Description: This module contains the Welcome Menu DockWidget.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QTextEdit

# Local Imports:
from Resources.Strings import MyStrings

class welcomeMenu(QTextEdit):
    """
    # Class: welcomeMenu.
    # Description: This class provides welcome information, tips and the changelog.
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
        # Description: This method initializes the User Interface Elements of the Welcome
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        self.setText(MyStrings.welcomeMenuDescription)
        self.setReadOnly(True)

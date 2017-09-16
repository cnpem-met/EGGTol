"""
# Module: WelcomeMenu.py
# Description: This module contains the Welcome Menu DockWidget.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QTextEdit

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

        welcomeTextFile = open('..\\src\\Interface\\welcome.txt', encoding='utf-8', mode='r')
        with welcomeTextFile:
            text = welcomeTextFile.read()
            self.setText(text)

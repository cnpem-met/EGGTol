"""
# Module: LoadingMenu.py
# Description: This module contains a PyQt Window Widget that will be used
while the applications works in loading processes.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon

# Local Imports:
from Resources.Strings import MyStrings

class loadingMenu(QDialog):
    """
    # Class: loadingMenu.
    # Description: This class represents the loading window itself.
    """

    def __init__(self):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        # Method: initUI.
        # Description: This method initializes the User Interface Elements of the Export
        Menu side widget.
        """
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.setWindowTitle(MyStrings.popupLoadingTitle)
        self.resize(200, 1)

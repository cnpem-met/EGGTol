"""
# Module: LoadingMenu.py
# Description: This module contains a PyQt Window Widget that will be used
while the applications works in loading processes.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

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
        self.setWindowTitle('Carregando... Por favor, aguarde.')
        self.resize(400, 1)
        grid = QGridLayout()

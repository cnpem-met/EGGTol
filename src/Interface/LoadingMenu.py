# Module: LoadingMenu.py
# Description: This module contains a PyQt Window Widget that will be used
# while the applications works in loading processes.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 14, 2017.

import sys
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout
from PyQt5.QtGui import QIcon

# Class: loadingMenu
# Description: This class represents the loading window itself.
class loadingMenu(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.setWindowTitle('Carregando')
        grid = QGridLayout()
        label = QLabel('Carregando... Por favor, aguarde.')
        grid.addWidget(label, 0, 0)
        self.setLayout(grid)

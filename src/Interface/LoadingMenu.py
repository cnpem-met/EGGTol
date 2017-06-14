# Module: LoadingMenu.py
# Description: This module contains a PyQt Window Widget that will be used
# while the applications works in loading processes.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 14, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QLabel

# Class: loadingMenu
# Description: This class represents the loading window itself.
class loadingMenu(QWidget):

    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle('Carregando')
        label = QLabel('Carregando... Por favor, aguarde.')
        grid.addWidget(label, 0, 0, 1, 1)

# Module: DiscretizeMenu.py
# Description: This module contains the Discretization Side Widget Menu UI
# for calling the discretization functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 27, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtCore import QCoreApplication

class discretizeMenu(QWidget):
    
    def __init__(self, callback):
        super().__init__()
        self.initUI(callback)
        
    def initUI(self, discretizeCallback):
        label = QLabel('Selecione uma opção de discretização.', self)
        btn = QPushButton('Discretização Automática', self)
        btn.clicked.connect(discretizeCallback)
        btn.resize(200, 30)
        btn.move(0, 15)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = closeWindow()
    sys.exit(app.exec_())

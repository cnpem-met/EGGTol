# Module: DiscretizeMenu.py
# Description: This module contains the Discretization Side Widget Menu UI
# for calling the discretization functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 27, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, \
                            QGridLayout
from PyQt5.QtCore import QCoreApplication

class discretizeMenu(QWidget):
    
    def __init__(self, callback):
        super().__init__()
        self.initUI(callback)
        
    def initUI(self, discretizeCallback):
        grid = QGridLayout()
        self.setLayout(grid)
        
        label1 = QLabel('Selecione uma opção de discretização.', self)
        grid.addWidget(label1, 0, 0)

        label2 = QLabel('A discretização automática irá trabalhar sobre\n' +
                        'todas as superfícies planas do modelo CAD segundo\n' +
                        'uma precisão informada pelo usuário.', self)
        grid.addWidget(label2, 1, 0)
        
        btn1 = QPushButton('Discretização Automática', self)
        btn1.clicked.connect(discretizeCallback)
        btn1.setMinimumHeight(30)
        grid.setRowMinimumHeight(2, 30)
        grid.addWidget(btn1, 2, 0)

        btn2 = QPushButton('Discretizção de Faces', self)
        btn2.setMinimumHeight(30)
        grid.setRowMinimumHeight(3, 30)
        grid.addWidget(btn2, 3, 0)
        
        btn3 = QPushButton('Discretizção Cilíndrica', self)
        btn3.setMinimumHeight(30)
        grid.setRowMinimumHeight(4, 30)
        grid.addWidget(btn3, 4, 0)
        
        btn4 = QPushButton('Discretização Cônica', self)
        btn4.setMinimumHeight(30)
        grid.setRowMinimumHeight(5, 30)
        grid.addWidget(btn4, 5, 0)
        
        btn5 = QPushButton('Discretização Esférica', self)
        btn5.setMinimumHeight(30)
        grid.setRowMinimumHeight(6, 30)
        grid.addWidget(btn5, 6, 0)

        grid.setRowStretch(7, 1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = closeWindow()
    sys.exit(app.exec_())

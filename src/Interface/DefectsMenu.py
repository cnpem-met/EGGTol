# Module: DefectsMenu.py
# Description: This module contains the Defects Side Widget Menu UI
# for calling the defects functions.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 21, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox
from PyQt5.QtCore import QCoreApplication, QSize
from Actions.ActionList import *

# Class: defectsMenu
# Description: This class provides a side menu with 2 types of artificial deviation options.
# Each option calls a function to initiate the deviation insertion process.
class defectsMenu(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        
    def initUI(self, parent):
        grid = QGridLayout()
        self.setLayout(grid)
        
        label1 = QLabel('Selecione a transformação desejada.', self)
        grid.addWidget(label1, 0, 0, 1, 1)

        label2 = QLabel('As operações de translação e rotação podem ser\n' +
                        'aplicadas a uma superfície plana ou curva. A\n' +
                        'aplicação dos erros de forma ainda não está\n' +
                        'disponível.', self)
        grid.addWidget(label2, 1, 0, 1, 1)
        
        btn1 = QToolButton()
        btn1.setText('Translação de um Conj. de Pontos')
        btn1.clicked.connect(lambda: self.translationDefectsMenuProcedure(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Rotação de um Conj. de Pontos')
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        grid.addWidget(btn2, 3, 0)

        btn3 = QToolButton()
        btn3.setText('Inserção de Erros Aleatórios')
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn2, 4, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(5, 1)

    def translationDefectsMenuProcedure(self, parent):
        translation = translationDefectsAction(parent)
        translation.translationDefectsActionProcedure(parent)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = closeWindow()
    sys.exit(app.exec_())

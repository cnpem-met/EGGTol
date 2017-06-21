# Module: Exportenu.py
# Description: This module contains the Export Side Widget Menu UI
# for generating files such as .pcd or screenshots.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 21, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

# Class: exportMenu
# Description: This class provides a side menu with some types of export options.
# Each option calls a function to initiate the export process process.
class exportMenu(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        
    def initUI(self, parent):
        grid = QGridLayout()
        self.setLayout(grid)
        
        label1 = QLabel('Selecione uma opção de exportação.', self)
        grid.addWidget(label1, 0, 0, 1, 1)

        label2 = QLabel('As operações de exportação permitem gerar\n' +
                        'arquivos de dados em formato de imagem e\n' +
                        'nuvem de pontos.', self)
        grid.addWidget(label2, 1, 0, 1, 1)
        
        btn1 = QToolButton()
        btn1.setText('Exportar Nuvem de Pontos')
        #btn1.clicked.connect(None)
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Exportar uma Captura de Tela')
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        grid.addWidget(btn2, 3, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(4, 1)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = closeWindow()
    sys.exit(app.exec_())

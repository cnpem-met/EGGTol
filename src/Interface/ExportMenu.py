"""
# Module: ExportMenu.py
# Description: This module contains the Export Side Widget Menu UI for generating
files such as .pcd or screenshots.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class exportMenu(QWidget):
    """
    # Class: exportMenu.
    # Description: This class provides a side menu with some types of export options.
    Each option calls a function to initiate the export process.
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
        # Description: This method initializes the User Interface Elements of the Export
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

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

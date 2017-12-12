"""
# Module: ExportMenu.py
# Description: This module contains the Export Side Widget Menu UI for generating
files such as .pcd or screenshots.
# Author: Willian Hideak Arita da Silva.
"""

import os, sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QFileDialog
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

        label2 = QLabel('As operações de exportação permitem gerar arquivos\n' +
                        'de dados em formato de imagem e nuvem de pontos.', self)
        grid.addWidget(label2, 1, 0, 1, 1)

        btn1 = QToolButton()
        btn1.setText('Exportar Nuvem de Pontos em .pcd')
        btn1.clicked.connect(lambda: self.exportPcd(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Exportar Nuvem de Pontos em .txt')
        btn2.clicked.connect(lambda: self.exportTxt(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        grid.addWidget(btn2, 3, 0)

        btn3 = QToolButton()
        btn3.setText('Exportar uma Captura de Tela')
        btn3.clicked.connect(lambda: self.exportScreenshot(parent))
        btn3.setMinimumHeight(50)
        btn3.setMinimumWidth(266)
        grid.addWidget(btn3, 4, 0)

        label3 = QLabel('\nFormato .pcd (Point Cloud Data):\n' +
                        'formato padrão para exportação da nuvem de pontos\n' +
                        'que pode ser lido com grande maioria dos programas\n' +
                        'comerciais.\n\n' +
                        'Formato .txt (Texto Plano):\n' +
                        'formato contendo todos os pontos gerados ordenados\n' +
                        'na forma de uma lista.\n\n' +
                        'Formato .png (Captura de Tela):\n' +
                        'salva uma imagem do modelo atual no formato Portable\n' +
                        'Network Graphics.', self)
        grid.addWidget(label3, 5, 0, 1, 1)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(6, 1)

    def exportPcd(self, parent):
        """
        # Method: exportPcd
        # Description: This method exports the actual point cloud data into a .pcd file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Discretization.DiscretizeModel import generatePcd
        defaultName = (parent.lastPath).split('.')[0:-1]
        defaultName = '.'.join(defaultName)
        defaultName = defaultName + '.pcd'
        fileName = QFileDialog.getSaveFileName(parent, 'Exportar arquivo .pcd', defaultName, "Point Cloud Data (*.pcd)")[0]
        if not fileName:
            return
        generatePcd(parent.cloudPointsList, fileName)

    def exportTxt(self, parent):
        """
        # Method: exportTxt
        # Description: This method exports the actual point cloud data into a .txt file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Discretization.DiscretizeModel import generateTxt
        defaultName = (parent.lastPath).split('.')[0:-1]
        defaultName = '.'.join(defaultName)
        defaultName = defaultName + '.txt'
        fileName = QFileDialog.getSaveFileName(parent, 'Exportar arquivo .txt', defaultName, "Arquivo de Texto (*.txt)")[0]
        if not fileName:
            return
        generateTxt(parent.cloudPointsList, fileName)

    def exportScreenshot(self, parent):
        """
        # Method: exportScreenshot
        # Description: This method exports the actual visualization into a screenshot.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        pass

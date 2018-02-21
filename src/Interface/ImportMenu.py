"""
# Module: ImportMenu.py
# Description: This module contains the Import Side Widget Menu UI for importing data into the
application. These data can be a point cloud or an IGES model.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QInputDialog, \
                            QGridLayout, QToolButton, QMessageBox, QFileDialog
from PyQt5.QtCore import QCoreApplication

class importMenu(QWidget):
    """
    # Class: importMenu.
    # Description: This class provides a side menu with some types of import options.
    Each option calls a function to initiate the import process.
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
        # Description: This method initializes the User Interface Elements of the Import
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel('Selecione uma opção de importação.', self)
        grid.addWidget(label1, 0, 0, 1, 1)

        label2 = QLabel('As operações de importação permitem adicionar\n' +
                        'arquivos CAD em formato IGES ou uma nuvem de\n' +
                        'pontos na visualização atual.', self)
        grid.addWidget(label2, 1, 0, 1, 1)

        btn1 = QToolButton()
        btn1.setText('Importar um Arquivo .IGES')
        btn1.clicked.connect(lambda: self.importIges(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText('Importar uma Nuvem de Pontos .pcd')
        btn2.clicked.connect(lambda: self.importPcd(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        btn2.setEnabled(False)
        grid.addWidget(btn2, 3, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(4, 1)

    def importIges(self, parent):
        """
        # Method: exportPcd
        # Description: This method imports an IGES file to the current visualization.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        if parent.activeCADFile:
            QMessageBox.information(parent, 'Arquivo .IGES já está aberto',
                                    'O arquivo ' + str(parent.activeCADFile) + ' já está em excução ' +
                                    'no momento. Conclua suas atividades e feche o arquivo para ' +
                                    'realizar uma nova importação.', QMessageBox.Ok, QMessageBox.Ok)
            return
        from OCC.IGESControl import IGESControl_Reader
        from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
        from Import.IGESImport import loadIGESFile, loadEntities, getRawData, getRawParameters
        fileName = QFileDialog.getOpenFileName(parent, 'Abrir Arquivo .IGES', parent.lastPath)
        if not fileName[0]:
            parent.loadingWindow.close()
            return
        parent.loadingWindow.show()
        parent.loadingWindow.activateWindow()
        parent.lastPath = fileName[0]
        Reader = IGESControl_Reader()
        status = Reader.ReadFile(fileName[0])
        shape = None
        if status == IFSelect_RetDone:
            Reader.TransferList(Reader.GiveList('xst-model-all'))
            for i in range(1, Reader.NbShapes()+1):
                parent.shapeList.append(Reader.Shape(i))
            shape = Reader.Shape(1)
            parent.loadingWindow.close()
        else:
            QMessageBox.information(parent, 'Erro ao Processar Arquivo',
                                    'Não foi possível abrir o arquivo especificado.\n' +
                                    'Verifique se o arquivo possuí a extensão .IGS ou .IGS ' +
                                    'e tente novamente.', QMessageBox.Ok, QMessageBox.Ok)
            parent.loadingWindow.close()
            return
        parent.canvas._display.DisplayShape(shape, update=True)
        parent.canvas._display.FitAll()
        parent.canvas._display.ZoomFactor(0.6)
        parent.activeCADFile = fileName[0]
        myfile = loadIGESFile(parent.activeCADFile)
        parent.entitiesObject = loadEntities(getRawData(myfile), getRawParameters(myfile))
        for entity in parent.entitiesObject:
            if(entity != None):
                parent.entitiesList.append(entity.description())
            else:
                parent.entitiesList.append(('# Entidade Desconhecida', []))
        parent.setWindowTitle(parent.title + ' - ' + fileName[0])
        pass

    def importPcd(self, parent):
        """
        # Method: importPcd
        # Description: This method imports a point cloud data from a .pcd file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        pass

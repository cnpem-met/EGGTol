# Module: ActionList.py
# Description: This module contains all possible actions that can be performed
# in the program. These actions has internal functions that can be called by
# the main.py.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox, qApp, QDockWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

# Show/hide the Welcome SideWidget.
class welcomeAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\desktopIcons\\main.png'), 'welcomeAction', parent)
        self.setStatusTip('Exibe o menu de boas vindas, incluindo o welcome.txt')
        self.setIconText('Bem-Vindo!')

# Show/hide the Entities SideWidget.
class entitiesAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\Server.svg'), 'entitiesAction', parent)
        self.setStatusTip('Exibe a Árvore de Entidades')
        self.setIconText('Entidades')

# Opens a File Dialog to open and display an .IGES File.
class importAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\inbox.svg'), 'importAction', parent)
        self.setStatusTip('Importar Um Arquivo .IGES')
        self.setIconText('Importar')
        self.triggered.connect(lambda: self.importActionProcedure(parent))
    def importActionProcedure(self, parent):
        from OCC.IGESControl import IGESControl_Reader
        from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
        fileName = QFileDialog.getOpenFileName(parent, 'Abrir Arquivo .IGES', parent.lastPath)
        if not fileName[0]:
            return
        parent.lastPath = fileName[0]
        Reader = IGESControl_Reader()
        status = Reader.ReadFile(fileName[0])
        shape = None
        if status == IFSelect_RetDone:
            Reader.TransferRoots()
            shape = Reader.Shape(1)
        else:
            QMessageBox.information(parent, 'Erro ao Processar Arquivo',
                                    'Não foi possível abrir o arquivo especificado.\n' +
                                    'Verifique se o arquivo possuí a extensão .IGS ou .IGS ' +
                                    'e tente novamente.', QMessageBox.Ok, QMessageBox.Ok)
            return
        parent.canvas._display.DisplayShape(shape, update=True)
        parent.canvas._display.FitAll()
        parent.activeFile = fileName[0]
        parent.setWindowTitle('Gerador de Nuvem de Pontos v0.30' + ' - ' + fileName[0])

# Opens the exportMenu.
class exportAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\outbox.svg'), 'exportAction', parent)
        self.setStatusTip('Exportar Um Arquivo .IGES')
        self.setIconText('Exportar')
        '''
        TODO
        IMPLEMENT THE EXPORT MENU
        '''

# Show/hide the Discretization Menu.
class cloudAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\cloud-download.svg'), 'cloudAction', parent)
        self.setStatusTip('Gerar uma Nuvem de Pontos para o Modelo')
        self.setIconText('Gerar Nuvem')
        self.triggered.connect(lambda: self.cloudActionProcedure(parent))
    def cloudActionProcedure(self, parent):
        from Interface.DiscretizeMenu import discretizeMenu
        widget = discretizeMenu(parent)
        dock = QDockWidget('Gerar Nuvem de Pontos', parent)
        dock.setWidget(widget)
        parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)

# Close the current file.
class closeAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\cross.svg'), 'closeAction', parent)
        self.setStatusTip('Fecha o modelo CAD atual')
        self.setIconText('Fechar')
        self.triggered.connect(lambda: self.closeActionProcedure(parent))
    def closeActionProcedure(self, parent):
        '''
        TODO
        IMPLEMENT A QDIALOG ASKING FOR PERMISSION OF CLOSING AND LOSING CHANGES
        '''
        parent.canvas._display.EraseAll()
        parent.setWindowTitle('Gerador de Nuvem de Pontos v0.30')

# Close the application.
class exitAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\circle-cross.svg'), 'exitAction', parent)
        self.setStatusTip('Encerra o programa')
        self.setIconText('Encerrar')
        self.triggered.connect(qApp.quit)
        '''
        TODO
        IMPLEMENT A QDIALOG ASKING FOR PERMISSION OF CLOSING AND LOSING CHANGES
        '''

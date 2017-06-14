# Module: ActionList.py
# Description: This module contains all possible actions that can be performed
# in the program. These actions has internal functions that can be called by
# the main.py.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 08, 2017.

from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox, qApp, QDockWidget
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

# Show/hide the Welcome SideWidget.
class welcomeAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\desktopIcons\\main.png'), 'Menu de Boas-Vindas', parent)
        self.setStatusTip('Exibe o menu de boas vindas, incluindo o welcome.txt')
        self.setIconText('Bem-Vindo!')
        self.triggered.connect(lambda: self.welcomeActionProcedure(parent))
    def welcomeActionProcedure(self, parent):
        from Interface.WelcomeMenu import welcomeMenu
        if parent.leftDockWidget == None:
            widget = welcomeMenu(parent)
            dock = QDockWidget('Bem-Vindo!', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = 'welcomeMenu'
        elif parent.leftDockWidget == 'welcomeMenu':
            parent.removeDockWidget(parent.leftDockMenu)
            parent.leftDockMenu = None
            parent.leftDockWidget = None
        else:
            parent.removeDockWidget(parent.leftDockMenu)
            widget = welcomeMenu(parent)
            dock = QDockWidget('Bem-Vindo!', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = 'welcomeMenu'
            

# Show/hide the Entities SideWidget.
class entitiesAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\Server.svg'), 'Painel de Entidades', parent)
        self.setStatusTip('Exibe a Árvore de Entidades')
        self.setIconText('Entidades')
        self.triggered.connect(lambda: self.entitiesActionProcedure(parent))
    def entitiesActionProcedure(self, parent):
        from Interface.EntitiesMenu import entitiesMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.leftDockWidget == None:
            widget = entitiesMenu(parent)
            dock = QDockWidget('Painel de Entidades', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = 'entitiesMenu'
        elif parent.leftDockWidget == 'entitiesMenu':
            parent.removeDockWidget(parent.leftDockMenu)
            parent.leftDockMenu = None
            parent.leftDockWidget = None
        else:
            parent.removeDockWidget(parent.leftDockMenu)
            widget = entitiesMenu(parent)
            dock = QDockWidget('Painel de Entidades', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = 'entitiesMenu'

# Opens a File Dialog to open and display an .IGES File.
class importAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\inbox.svg'), 'Importar Arquivo .IGES', parent)
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
            Reader.TransferList(Reader.GiveList('xst-model-all'))
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
        parent.activeCADFile = fileName[0]

# Opens the exportMenu.
class exportAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\outbox.svg'), 'Painel de Exportação', parent)
        self.setStatusTip('Exportar Um Arquivo .IGES')
        self.setIconText('Exportar')
        '''
        TODO
        IMPLEMENT THE EXPORT MENU
        '''

# Show/hide the Discretization Menu.
class cloudAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\cloud-download.svg'), 'Painel de Discretização', parent)
        self.setStatusTip('Gerar uma Nuvem de Pontos para o Modelo')
        self.setIconText('Gerar Nuvem')
        self.triggered.connect(lambda: self.cloudActionProcedure(parent))
    def cloudActionProcedure(self, parent):
        from Interface.DiscretizeMenu import discretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = discretizeMenu(parent)
            dock = QDockWidget('Gerar Nuvem de Pontos', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'cloudMenu'
        elif parent.rightDockWidget == 'cloudMenu':
            parent.removeDockWidget(parent.rightDockMenu)
            parent.rightDockMenu = None
            parent.rightDockWidget = None
        else:
            parent.removeDockWidget(parent.rightDockMenu)
            widget = discretizeMenu(parent)
            dock = QDockWidget('Gerar Nuvem de Pontos', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'cloudMenu'

# Close the current file.
class closeAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\cross.svg'), 'Fechar Arquivo', parent)
        self.setStatusTip('Fecha o modelo CAD atual')
        self.setIconText('Fechar')
        self.triggered.connect(lambda: self.closeActionProcedure(parent))
    def closeActionProcedure(self, parent):
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        box.setWindowTitle('Fechar Arquivo')
        box.setText('Tem certeza que deseja fechar o arquivo? As alterações\n' +
                    'não salvas/exportadas serão perdidas.')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        buttonYes = box.button(QMessageBox.Yes)
        buttonYes.setText('Fechar')
        buttonNo = box.button(QMessageBox.No)
        buttonNo.setText('Cancelar')
        box.exec_()
        if box.clickedButton() == buttonYes:  
            if parent.leftDockWidget == 'entitiesMenu':
                parent.removeDockWidget(parent.leftDockMenu)
                parent.leftDockMenu = None
                parent.leftDockWidget = None
            if parent.rightDockWidget == 'cloudMenu':
                parent.removeDockWidget(parent.rightDockMenu)
                parent.rightDockMenu = None
                parent.rightDockWidget = None
            parent.canvas._display.EraseAll()
            parent.setWindowTitle('Gerador de Nuvem de Pontos v0.30')
            parent.activeCADFile = None
            parent.canvas._display.View_Iso()

# Close the application.
class exitAction(QAction):
    def __init__(self, parent):
        super().__init__(QIcon('..\\icons\\circle-cross.svg'), 'Encerrar', parent)
        self.setStatusTip('Encerra o programa')
        self.setIconText('Encerrar')
        self.triggered.connect(lambda: self.exitActionProcedure())
    def exitActionProcedure(self):
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        box.setWindowTitle('Encerrar o Gerador de Pontos')
        box.setText('Tem certeza que deseja encerrar? As alterações\n' +
                    'não salvas/exportadas serão perdidas.')
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        buttonYes = box.button(QMessageBox.Yes)
        buttonYes.setText('Encerrar')
        buttonNo = box.button(QMessageBox.No)
        buttonNo.setText('Cancelar')
        box.exec_()
        if box.clickedButton() == buttonYes:
            qApp.quit()

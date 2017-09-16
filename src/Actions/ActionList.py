"""
# Module: ActionList.py
# Description: This module contains all possible actions that can be performed
in the program. These actions has internal functions that can be called by the main.py.
# Author: Willian Hideak Arita da Silva.
"""
import webbrowser

from PyQt5.QtWidgets import QAction, QFileDialog, QMessageBox, qApp, QDockWidget, \
                            QDialog, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

from Import.IGESImport import *

class welcomeAction(QAction):
    """
    # Class: welcomeAction
    # Description: A PyQt5 action that opens the Welcome Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\desktopIcons\\main.png'), 'Painel de Boas-Vindas', parent)
        self.setStatusTip('Exibe o menu de boas vindas, incluindo o welcome.txt')
        self.setIconText('Bem-Vindo!')
        self.triggered.connect(lambda: self.welcomeActionProcedure(parent))

    def welcomeActionProcedure(self, parent):
        """
        # Method: welcomeActionProcedure.
        # Description: A procedure for opening the Welcome Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.WelcomeMenu import welcomeMenu
        if parent.leftDockWidget == None:
            widget = welcomeMenu(parent)
            dock = QDockWidget('Painel de Boas-Vindas!', parent)
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
            dock = QDockWidget('Painel de Boas-Vindas!', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = 'welcomeMenu'


class entitiesAction(QAction):
    """
    # Class: entitiesAction.
    # Description: A PyQt5 action that opens the Entities Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\Server.svg'), 'Painel de Entidades', parent)
        self.setStatusTip('Exibe a Árvore de Entidades')
        self.setIconText('Entidades')
        self.triggered.connect(lambda: self.entitiesActionProcedure(parent))

    def entitiesActionProcedure(self, parent):
        """
        # Method: entitiesActionProcedure
        # Description: A procedure for opening the Entities Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

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

class importAction(QAction):
    """
    # Class: importAction.
    # Description: A PyQt5 action that imports an IGES file to the current session.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\inbox.svg'), 'Importar Arquivo .IGES', parent)
        self.setStatusTip('Importar Um Arquivo .IGES')
        self.setIconText('Importar')
        self.triggered.connect(lambda: self.importActionProcedure(parent))

    def importActionProcedure(self, parent):
        """
        # Method: importActionProcedure
        # Description: A procedure that imports an IGES file to the current session.
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
        fileName = QFileDialog.getOpenFileName(parent, 'Abrir Arquivo .IGES', parent.lastPath)
        parent.loadingWindow.show()
        parent.loadingWindow.activateWindow()
        if not fileName[0]:
            parent.loadingWindow.close()
            return
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
        parent.activeCADFile = fileName[0]
        file = loadIGESFile(parent.activeCADFile)
        parent.entitiesObject = loadEntities(getRawData(file), getRawParameters(file))
        for entity in parent.entitiesObject:
            if(entity != None):
                parent.entitiesList.append(entity.description())
            else:
                parent.entitiesList.append(('Unsupported Object', []))
        parent.setWindowTitle(parent.windowTitle + ' - ' + fileName[0])

class exportAction(QAction):
    """
    # Class: exportAction.
    # Description: A PyQt5 action that opens the Export Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\outbox.svg'), 'Painel de Exportação', parent)
        self.setStatusTip('Exportar Um Arquivo .IGES')
        self.setIconText('Exportar')
        self.triggered.connect(lambda: self.exportActionProcedure(parent))

    def exportActionProcedure(self, parent):
        """
        # Method: exportActionProcedure.
        # Description: A procedure for opening the Export Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.ExportMenu import exportMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES ou .pcd foi aberto',
                                    'Não há nenhum arquivo .IGS, .IGES ou .pcd ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = exportMenu(parent)
            dock = QDockWidget('Painel de Exportação', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'exportMenu'
        elif parent.rightDockWidget == 'exportMenu':
            parent.removeDockWidget(parent.rightDockMenu)
            parent.rightDockMenu = None
            parent.rightDockWidget = None
        else:
            parent.removeDockWidget(parent.rightDockMenu)
            widget = exportMenu(parent)
            dock = QDockWidget('Painel de Exportação', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'exportMenu'

class cloudAction(QAction):
    """
    # Class: cloudAction.
    # Description: A PyQt5 action that opens the Discretize Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\cloud-download.svg'), 'Painel de Discretização', parent)
        self.setStatusTip('Gerar uma Nuvem de Pontos para o Modelo')
        self.setIconText('Gerar Nuvem')
        self.triggered.connect(lambda: self.cloudActionProcedure(parent))

    def cloudActionProcedure(self, parent):
        """
        # Method: cloudActionProcedure.
        # Description: A procedure for opening the Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.DiscretizeMenu import discretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = discretizeMenu(parent)
            dock = QDockWidget('Painel de Discretização', parent)
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
            dock = QDockWidget('Painel de Discretização', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'cloudMenu'

class autoDiscretizeAction(QAction):
    """
    # Class: autoDiscretizeAction.
    # Description: A PyQt5 action that opens the Auto Discretize Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Painel de Discretização Automática', parent)
        self.setStatusTip('Gerar uma Nuvem de Pontos para o Modelo Automaticamente')
        self.triggered.connect(lambda: self.autoDiscretizeActionProcedure(parent))

    def autoDiscretizeActionProcedure(self, parent):
        """
        # Method: autoDiscretizeActionProcedure.
        # Description: The procedure for opening the Auto Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.AutoDiscretizeMenu import autoDiscretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = autoDiscretizeMenu(parent)
            dock = QDockWidget('Painel de Discretização Automática', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'autoDiscretizeMenu'
        elif parent.rightDockWidget == 'autoDiscretizeMenu':
            parent.removeDockWidget(parent.rightDockMenu)
            parent.rightDockMenu = None
            parent.rightDockWidget = None
        else:
            parent.removeDockWidget(parent.rightDockMenu)
            widget = autoDiscretizeMenu(parent)
            dock = QDockWidget('Painel de Discretização Automática', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'autoDiscretizeMenu'

class defectsAction(QAction):
    """
    # Class: defectsAction.
    # Description: A PyQt5 action that opens the Defects Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\cloud-download.svg'), 'Painel de Geração de Erros', parent)
        self.setStatusTip('Inserir erros artificiais em nuvens de pontos.')
        self.setIconText('Gerar Erros')
        self.triggered.connect(lambda: self.defectsActionProcedure(parent))

    def defectsActionProcedure(self, parent):
        """
        # Method: defectsActionProcedure.
        # Description: The procedure for opening the Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.DefectsMenu import defectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, 'Nenhuma Nuvem de Pontos presente',
                                    'Não há nenhum arquivo .pcd aberto e nenhuma ' +
                                    'nuvem de pontos foi gerada no momento. Utilize ' +
                                    'o menu de discretização ou importe uma nuvem de pontos ' +
                                    'para inserir erros.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = defectsMenu(parent)
            dock = QDockWidget('Painel de Geração de Erros', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'defectsMenu'
        elif parent.rightDockWidget == 'defectsMenu':
            parent.removeDockWidget(parent.rightDockMenu)
            parent.rightDockMenu = None
            parent.rightDockWidget = None
        else:
            parent.removeDockWidget(parent.rightDockMenu)
            widget = defectsMenu(parent)
            dock = QDockWidget('Painel de Geração de Erros', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'defectsMenu'

class translationDefectsAction(QAction):
    """
    # Class: translationalDefectsAction.
    # Description: A PyQt5 action that opens the Translational Defects Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Painel de Geração de Erros por Translação', parent)
        self.setStatusTip('Inserir erros artificiais devido à translação em nuvens de pontos.')
        self.triggered.connect(lambda: self.translationDefectsActionProcedure(parent))

    def translationDefectsActionProcedure(self, parent):
        """
        # Method: translationDefectsActionProcedure.
        # Description: The procedure for opening the Translational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.TranslationDefectsMenu import translationDefectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, 'Nenhuma Nuvem de Pontos presente',
                                    'Não há nenhum arquivo .pcd aberto e nenhuma ' +
                                    'nuvem de pontos foi gerada no momento. Utilize ' +
                                    'o menu de discretização ou importe uma nuvem de pontos ' +
                                    'para inserir erros.', QMessageBox.Ok, QMessageBox.Ok)
            return
        if parent.rightDockWidget == None:
            widget = translationDefectsMenu(parent)
            dock = QDockWidget('Painel de Geração de Erros por Translação', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'translationDefectsMenu'
            parent.canvas._display.SetSelectionModeFace()
        elif parent.rightDockWidget == 'translationDefectsMenu':
            parent.removeDockWidget(parent.rightDockMenu)
            parent.rightDockMenu = None
            parent.rightDockWidget = None
            parent.canvas._display.SetSelectionModeNeutral()
        else:
            parent.removeDockWidget(parent.rightDockMenu)
            widget = translationDefectsMenu(parent)
            dock = QDockWidget('Painel de Geração de Erros por Translação', parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = 'translationDefectsMenu'
            parent.canvas._display.SetSelectionModeFace()

class closeAction(QAction):
    """
    # Class: closeAction
    # Description: A PyQt5 action that closes the current opened IGES file.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\cross.svg'), 'Fechar Arquivo', parent)
        self.setStatusTip('Fecha o modelo CAD atual')
        self.setIconText('Fechar')
        self.triggered.connect(lambda: self.closeActionProcedure(parent))

    def closeActionProcedure(self, parent):
        """
        # Method: closeActionProcedure.
        # Description: The procedure for closing the current opened IGES file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

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
            test = parent.leftDockWidget
            if test == 'entitiesMenu':
                parent.removeDockWidget(parent.leftDockMenu)
                parent.leftDockMenu = None
                parent.leftDockWidget = None
            test = parent.rightDockWidget
            if test == 'cloudMenu' or test == 'defectsMenu' or \
               test == 'translationDefectsMenu' or test == 'autoDiscretizeMenu':
                parent.removeDockWidget(parent.rightDockMenu)
                parent.rightDockMenu = None
                parent.rightDockWidget = None
            parent.canvas._display.SetSelectionModeNeutral()
            parent.canvas._display.EraseAll()
            parent.setWindowTitle(parent.windowTitle)
            parent.activeCADFile = None
            parent.activeCloudFile = None
            parent.entitiesList = []
            parent.shapeList = []
            parent.canvas._display.View_Iso()

class exitAction(QAction):
    """
    # Class: exitAction.
    # Description: A PyQt5 action that closes the application and all the opened files.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\circle-cross.svg'), 'Encerrar', parent)
        self.setStatusTip('Encerra o programa')
        self.setIconText('Encerrar')
        self.triggered.connect(lambda: self.exitActionProcedure())

    def exitActionProcedure(self):
        """
        # Method: exitActionProcedure.
        # Description: The procedure for closing the application and all the opened files.
        """

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

class darkAction(QAction):
    """
    # Class: darkAction.
    # Description: A PyQt5 action that sets a dark background of the 3D Viewer.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\moon.svg'), 'Definir Fundo Escuro', parent)
        self.setStatusTip('Configura o fundo de tela com uma cor escura')
        self.setIconText('Escuro')
        self.triggered.connect(lambda: self.darkActionProcedure(parent))

    def darkActionProcedure(self, parent):
        """
        # Method: darkActionProcedure.
        # Description: The procedure for setting a dark background.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.set_bg_gradient_color(10, 10, 10, 10, 10, 43)
        parent.canvas._display.Repaint()

class lightAction(QAction):
    """
    # Class: lightAction.
    # Description: A PyQt5 action that sets a light background of the 3D Viewer.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\sun.svg'), 'Definir Fundo Claro', parent)
        self.setStatusTip('Configura o fundo de tela com uma cor escura')
        self.setIconText('Claro')
        self.triggered.connect(lambda: self.lightActionProcedure(parent))

    def lightActionProcedure(self, parent):
        """
        # Method: lightActionProcedure.
        # Description: The procedure for setting a light background.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.set_bg_gradient_color(255, 255, 255, 210, 255, 222)
        parent.canvas._display.Repaint()

class githubAction(QAction):
    """
    # Class: githubAction.
    # Description: A PyQt5 action that opens the project website showing the gitHub
    information of the project.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Abrir Projeto no GitHub', parent)
        self.setStatusTip('Exibe informações sobre esse projeto, hospedado no GitHub.com')
        self.setIconText('Github')
        self.triggered.connect(lambda: webbrowser.open('https://github.com/hideak/pointCloudGenerator'))

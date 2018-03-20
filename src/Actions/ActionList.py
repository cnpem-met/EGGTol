"""
# Module: ActionList.py
# Description: This module contains all possible actions that can be performed
in the program. These actions has internal functions that can be called by the main.py.
# Author: Willian Hideak Arita da Silva.
"""

# System Imports:
import webbrowser

# PyQt5 Imports:
from PyQt5.QtWidgets import QAction, QMessageBox, qApp, QDockWidget, QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

# Local Imports:
from Resources.Strings import MyStrings

def switchLeftPanels(widget, name, prettyName, parent, scroll):
    """
    # Function: switchLeftPanels.
    # Description: This function opens/hide the side dock widget according to the dock informed
    in the 'widget' argument.
    # Parameters: * QDockWidget widget = The widget to be displayed in the side dock.
                  * Str name = The name which will be saved into the leftDockWidget attribute
                  of the main.py file for identification purposes.
                  * Str prettyName = String that will be displayed at the top of the dock widget.
                  * MainWindow parent = A reference for the main window object.
                  * Boolean scroll = Defines if the side menu will have a vertical scroll bar.
    """

    if parent.leftDockWidget == None:
        dock = QDockWidget(prettyName, parent)
        content = None
        if(scroll):
            content = QScrollArea(parent)
            content.setWidget(widget)
            dock.setMinimumWidth(303)
        else:
            content = widget
        dock.setWidget(content)
        parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
        parent.leftDockMenu = dock
        parent.leftDockWidget = name
    else:
        parent.removeDockWidget(parent.leftDockMenu)
        if parent.leftDockWidget == name:
            parent.leftDockMenu = None
            parent.leftDockWidget = None
        else:
            dock = QDockWidget(prettyName, parent)
            content = None
            if(scroll):
                content = QScrollArea(parent)
                content.setWidget(widget)
                dock.setMinimumWidth(303)
            else:
                content = widget
            dock.setWidget(content)

            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = name

def switchRightPanels(widget, name, prettyName, parent, scroll):
    """
    # Function: switchRightPanels.
    # Description: This function opens/hide the side dock widget according to the dock informed
    in the 'widget' argument.
    # Parameters: * QDockWidget widget = The widget to be displayed in the side dock.
                  * Str name = The name which will be saved into the rightDockWidget attribute
                  of the main.py file for identification purposes.
                  * Str prettyName = String that will be displayed at the top of the dock widget.
                  * MainWindow parent = A reference for the main window object.
                  * Boolean scroll = Defines if the side menu will have a vertical scroll bar.
    """

    if parent.rightDockWidget == None:
        dock = QDockWidget(prettyName, parent)
        content = None
        if(scroll):
            content = QScrollArea(parent)
            content.setWidget(widget)
            dock.setMinimumWidth(303)
        else:
            content = widget
        dock.setWidget(content)
        parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
        parent.rightDockMenu = dock
        parent.rightDockWidget = name
    else:
        parent.removeDockWidget(parent.rightDockMenu)
        if parent.rightDockWidget == name:
            parent.rightDockMenu = None
            parent.rightDockWidget = None
        else:
            dock = QDockWidget(prettyName, parent)
            content = None
            if(scroll):
                content = QScrollArea(parent)
                content.setWidget(widget)
                dock.setMinimumWidth(303)
            else:
                content = widget
            dock.setWidget(content)
            parent.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)
            parent.rightDockMenu = dock
            parent.rightDockWidget = name

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

        super().__init__(QIcon('..\\icons\\desktopIcons\\main.png'), MyStrings.actionWelcomePrettyName, parent)
        self.setStatusTip(MyStrings.actionWelcomeStatusTip)
        self.setIconText(MyStrings.actionWelcomeIconText)
        self.triggered.connect(lambda: self.welcomeActionProcedure(parent))

    def welcomeActionProcedure(self, parent):
        """
        # Method: welcomeActionProcedure.
        # Description: A procedure for opening the Welcome Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.WelcomeMenu import welcomeMenu
        widget = welcomeMenu(parent)
        name = MyStrings.actionWelcomeName
        prettyName = MyStrings.actionWelcomePrettyName
        if parent.leftDockWidget == None:
            dock = QDockWidget(prettyName, parent)
            dock.setWidget(widget)
            parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            parent.leftDockMenu = dock
            parent.leftDockWidget = name
        else:
            parent.removeDockWidget(parent.leftDockMenu)
            if parent.leftDockWidget == name:
                parent.leftDockMenu = None
                parent.leftDockWidget = None
            else:
                dock = QDockWidget(prettyName, parent)
                dock.setWidget(widget)
                parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
                parent.leftDockMenu = dock
                parent.leftDockWidget = name

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

        super().__init__(QIcon('..\\icons\\Server.svg'), MyStrings.actionEntitiesPrettyName, parent)
        self.setStatusTip(MyStrings.actionEntitiesStatusTip)
        self.setIconText(MyStrings.actionEntitiesIconText)
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
        widget = entitiesMenu(parent)
        switchLeftPanels(widget, MyStrings.actionEntitiesName, MyStrings.actionEntitiesPrettyName, parent, False)

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

        super().__init__(QIcon('..\\icons\\inbox.svg'), 'Painel de Importação', parent)
        self.setStatusTip('Importar Um Arquivo .IGES ou uma Nuvem de Pontos.')
        self.setIconText('Importar')
        self.triggered.connect(lambda: self.importActionProcedure(parent))

    def importActionProcedure(self, parent):
        """
        # Method: importActionProcedure
        # Description: A procedure for opening the Import Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.ImportMenu import importMenu
        widget = importMenu(parent)
        switchRightPanels(widget, 'importMenu', 'Painel de Importação', parent, True)

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
        self.setStatusTip('Exportar Um Modelo CAD como uma Captura de Tela ou uma Nuvem de Pontos.')
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
        widget = exportMenu(parent)
        switchRightPanels(widget, 'exportMenu', 'Painel de Exportação', parent, True)

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

        super().__init__(QIcon('..\\icons\\cloud.svg'), 'Painel de Discretização', parent)
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
        widget = discretizeMenu(parent)
        switchRightPanels(widget, 'cloudMenu', 'Painel de Discretização', parent, True)

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
        self.setStatusTip('Gerar uma nuvem de pontos para o modelo automaticamente')
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
        widget = autoDiscretizeMenu(parent)
        switchRightPanels(widget, 'autoDiscretizeMenu', 'Painel de Discretização ' +
                          'Automática', parent, True)

class faceDiscretizeAction(QAction):
    """
    # Class: faceDiscretizeAction.
    # Description: A PyQt5 action that opens the Face Discretize Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Painel de Discretização de Faces', parent)
        self.setStatusTip('Gerar uma nuvem de pontos para uma face específica do modelo')
        self.triggered.connect(lambda: self.faceDiscretizeActionProcedure(parent))

    def faceDiscretizeActionProcedure(self, parent):
        """
        # Method: faceDiscretizeActionProcedure.
        # Description: The procedure for opening the Face Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.FaceDiscretizeMenu import faceDiscretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = faceDiscretizeMenu(parent)
        switchRightPanels(widget, 'faceDiscretizeMenu', 'Painel de Discretização de ' +
                          'Faces', parent, True)

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

        super().__init__(QIcon('..\\icons\\move.svg'), 'Painel de Geração de Erros', parent)
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
        widget = defectsMenu(parent)
        switchRightPanels(widget, 'defectsMenu', 'Painel de Geração de Erros', parent, True)

class pointsListAction(QAction):
    """
    # Class: pointsListAction.
    # Description: A PyQt5 action that opens the Points List Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\paper.svg'), 'Painel de Pontos Gerados', parent)
        self.setStatusTip('Mostra todos os pontos gerados no modelo CAD atual.')
        self.setIconText('Lista de Pontos')
        self.triggered.connect(lambda: self.pointsListActionProcedure(parent))

    def pointsListActionProcedure(self, parent):
        """
        # Method: pointsListActionProcedure.
        # Description: The procedure for opening the Points List Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        from Interface.PointsListMenu import pointsListMenu
        if not parent.activeCloudFile:
            QMessageBox.information(parent, 'Nenhuma Nuvem de Pontos presente',
                                    'Não há nenhum arquivo .pcd aberto e nenhuma ' +
                                    'nuvem de pontos foi gerada no momento. Utilize ' +
                                    'o menu de discretização ou importe uma nuvem de pontos ' +
                                    'para inserir erros.', QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = pointsListMenu(parent)
        switchLeftPanels(widget, 'pointsListMenu', 'Painel de Pontos Gerados', parent, False)

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
        widget = translationDefectsMenu(parent)
        switchRightPanels(widget, 'translationDefectsMenu', 'Painel de Geração de Erros por ' +
                          'Translação', parent, True)

class rotationalDefectsAction(QAction):
    """
    # Class: rotationalDefectsAction.
    # Description: A PyQt5 action that opens the Rotational Defects Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Painel de Geração de Erros por Rotação', parent)
        self.setStatusTip('Inserir erros artificiais devido à rotação em nuvens de pontos.')
        self.triggered.connect(lambda: self.translationDefectsActionProcedure(parent))

    def rotationalDefectsActionProcedure(self, parent):
        """
        # Method: rotationalDefectsActionProcedure.
        # Description: The procedure for opening the Rotational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.RotationalDefectsMenu import rotationalDefectsMenu
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
        widget = rotationalDefectsMenu(parent)
        switchRightPanels(widget, 'rotationalDefectsMenu', 'Painel de Geração de Erros por ' +
                          'Rotação', parent, True)

class randomDefectsAction(QAction):
    """
    # Class: randomDefectsAction.
    # Description: A PyQt5 action that opens the Random Defects Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Painel de Geração de Erros Aleatórios', parent)
        self.setStatusTip('Inserir erros artificiais aleatoriamente em nuvens de pontos.')
        self.triggered.connect(lambda: self.randomDefectsActionProcedure(parent))

    def randomDefectsActionProcedure(self, parent):
        """
        # Method: randomDefectsActionProcedure.
        # Description: The procedure for opening the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.RandomDefectsMenu import randomDefectsMenu
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
        widget = randomDefectsMenu(parent)
        switchRightPanels(widget, 'randomDefectsMenu', 'Painel de Geração de Erros ' +
                          'Aleatórios', parent, True)

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

        from Interface.WelcomeMenu import welcomeMenu

        # Checking if there is a current file:
        if not parent.activeCADFile:
            QMessageBox.information(parent, 'Nenhum arquivo .IGES foi aberto',
                                    'Não há nenhum arquivo .IGS ou .IGES ativo no\n' +
                                    'momento. Utilize o menu Arquivo > Importar para\n' +
                                    'para abrir um arquivo.', QMessageBox.Ok, QMessageBox.Ok)
            return

        # Creating a confirmation dialog asking for permission to close the file:
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

        # Executing a routine for closing the current file:
        if box.clickedButton() == buttonYes:
            parent.removeDockWidget(parent.leftDockMenu)
            parent.removeDockWidget(parent.rightDockMenu)
            parent.leftDockMenu = parent.leftDockWidget = None
            parent.rightDockMenu = parent.rightDockWidget = None
            widget = welcomeMenu(parent)
            name = 'welcomeMenu'
            prettyName = 'Painel de Boas-Vindas!'
            if parent.leftDockWidget == None:
                dock = QDockWidget(prettyName, parent)
                dock.setWidget(widget)
                parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
                parent.leftDockMenu = dock
                parent.leftDockWidget = name
            else:
                parent.removeDockWidget(parent.leftDockMenu)
                if parent.leftDockWidget == name:
                    parent.leftDockMenu = None
                    parent.leftDockWidget = None
                else:
                    dock = QDockWidget(prettyName, parent)
                    dock.setWidget(widget)
                    parent.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
                    parent.leftDockMenu = dock
                    parent.leftDockWidget = name
            parent.canvas._display.SetSelectionModeNeutral()
            parent.canvas._display.Context.CloseAllContexts()
            parent.canvas._display.Context.RemoveAll()
            parent.canvas._display.Repaint()
            parent.setWindowTitle(parent.title)
            parent.activeCADFile = None
            parent.activeCloudFile = None
            parent.entitiesObject = []
            parent.pointCloudObject = None
            parent.pointAspectObject = None
            parent.entitiesList = []
            parent.cloudPointsList = []
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

        parent.light = False
        parent.canvas._display.set_bg_gradient_color(10, 10, 10, 10, 10, 43)
        parent.canvas._display.display_trihedron_white()
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
        self.setStatusTip('Configura o fundo de tela com uma cor clara')
        self.setIconText('Claro')
        self.triggered.connect(lambda: self.lightActionProcedure(parent))

    def lightActionProcedure(self, parent):
        """
        # Method: lightActionProcedure.
        # Description: The procedure for setting a light background.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.light = True
        parent.canvas._display.set_bg_gradient_color(255, 255, 255, 210, 255, 222)
        parent.canvas._display.display_trihedron()
        parent.canvas._display.Repaint()

class selectionNeutralAction(QAction):
    """
    # Class: selectionNeutralAction.
    # Description: A PyQt5 Action that enables the solid selection mode.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__(QIcon('..\icons\\arrow-right.svg'), 'Modo de Seleção de Sólidos', parent)
        self.setStatusTip('Define como padrão o modo de seleção de sólidos')
        self.triggered.connect(lambda: self.selectionNeutralActionProcedure(parent))

    def selectionNeutralActionProcedure(self, parent):
        """
        # Method: selectionNeutralActionProcedure.
        # Description: A function call that enables the solid selection mode.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeNeutral()

class selectionFaceAction(QAction):
    """
    # Class: selectionFaceAction.
    # Description: A PyQt5 Action that enables the face selection mode.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__(QIcon('..\icons\\arrow-right.svg'), 'Modo de Seleção de Faces', parent)
        self.setStatusTip('Define como padrão o modo de seleção de faces')
        self.triggered.connect(lambda: self.selectionFaceActionProcedure(parent))

    def selectionFaceActionProcedure(self, parent):
        """
        # Method: selectionFaceActionProcedure.
        # Description: A function call that enables the face selection mode.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeFace()

class selectionEdgeAction(QAction):
    """
    # Class: selectionEdgeAction.
    # Description: A PyQt5 Action that enables the edge selection mode.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__(QIcon('..\icons\\arrow-right.svg'), 'Modo de Seleção de Arestas', parent)
        self.setStatusTip('Define como padrão o modo de seleção de arestas')
        self.triggered.connect(lambda: self.selectionEdgeActionProcedure(parent))

    def selectionEdgeActionProcedure(self, parent):
        """
        # Method: selectionEdgeActionProcedure.
        # Description: A function call that enables the edge selection mode.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeEdge()

class selectionVertexAction(QAction):
    """
    # Class: selectionVertexAction.
    # Description: A PyQt5 Action that enables the vertex selection mode.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__(QIcon('..\icons\\arrow-right.svg'), 'Modo de Seleção de Vértices', parent)
        self.setStatusTip('Define como padrão o modo de seleção de vértices')
        self.triggered.connect(lambda: self.selectionVertexActionProcedure(parent))

    def selectionVertexActionProcedure(self, parent):
        """
        # Method: selectionVertexActionProcedure.
        # Description: A function call that enables the vertex selection mode.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        parent.canvas._display.SetSelectionModeVertex()

class viewTopAction(QAction):
    """
    # Class: viewTopAction.
    # Description: A PyQt5 action that generates the top view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Superior', parent)
        self.setStatusTip('Exibe a vista superior do modelo CAD atual')
        self.setIconText('Vista Superior')
        self.triggered.connect(lambda: self.viewTopActionProcedure(parent))

    def viewTopActionProcedure(self, parent):
        """
        # Method: viewTopActionProcedure.
        # Description: The procedure for setting the top view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Top()
        parent.canvas._display.Repaint()

class viewBottomAction(QAction):
    """
    # Class: viewBottomAction.
    # Description: A PyQt5 action that generates the bottom view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Inferior', parent)
        self.setStatusTip('Exibe a vista inferior do modelo CAD atual')
        self.setIconText('Vista Inferior')
        self.triggered.connect(lambda: self.viewBottomActionProcedure(parent))

    def viewBottomActionProcedure(self, parent):
        """
        # Method: viewBottomActionProcedure.
        # Description: The procedure for setting the bottom view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Bottom()
        parent.canvas._display.Repaint()

class viewLeftAction(QAction):
    """
    # Class: viewLeftAction.
    # Description: A PyQt5 action that generates the left view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Lateral Esquerda', parent)
        self.setStatusTip('Exibe a vista lateral esquerda do modelo CAD atual')
        self.setIconText('Vista Lateral Esquerda')
        self.triggered.connect(lambda: self.viewLeftActionProcedure(parent))

    def viewLeftActionProcedure(self, parent):
        """
        # Method: viewLeftActionProcedure.
        # Description: The procedure for setting the left view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Left()
        parent.canvas._display.Repaint()

class viewRightAction(QAction):
    """
    # Class: viewRightAction.
    # Description: A PyQt5 action that generates the right view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Lateral Direita', parent)
        self.setStatusTip('Exibe a vista lateral direita do modelo CAD atual')
        self.setIconText('Vista Lateral Direita')
        self.triggered.connect(lambda: self.viewRightActionProcedure(parent))

    def viewRightActionProcedure(self, parent):
        """
        # Method: viewRightActionProcedure.
        # Description: The procedure for setting the right view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Right()
        parent.canvas._display.Repaint()

class viewFrontAction(QAction):
    """
    # Class: viewFrontAction.
    # Description: A PyQt5 action that generates the front view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Frontal', parent)
        self.setStatusTip('Exibe a vista frontal do modelo CAD atual')
        self.setIconText('Vista Frontal')
        self.triggered.connect(lambda: self.viewFrontActionProcedure(parent))

    def viewFrontActionProcedure(self, parent):
        """
        # Method: viewFrontActionProcedure.
        # Description: The procedure for setting the front view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Front()
        parent.canvas._display.Repaint()

class viewRearAction(QAction):
    """
    # Class: viewRearAction.
    # Description: A PyQt5 action that generates the rear view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Posterior', parent)
        self.setStatusTip('Exibe a vista posterior do modelo CAD atual')
        self.setIconText('Vista Posterior')
        self.triggered.connect(lambda: self.viewRearActionProcedure(parent))

    def viewRearActionProcedure(self, parent):
        """
        # Method: viewRearActionProcedure.
        # Description: The procedure for setting the rear view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Rear()
        parent.canvas._display.Repaint()

class viewIsoAction(QAction):
    """
    # Class: viewIsoAction.
    # Description: A PyQt5 action that generates the isometric view of a CAD model.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\box.svg'), 'Vista Isométrica', parent)
        self.setStatusTip('Exibe a vista isométrica do modelo CAD atual')
        self.setIconText('Vista Isométrica')
        self.triggered.connect(lambda: self.viewIsoActionProcedure(parent))

    def viewIsoActionProcedure(self, parent):
        """
        # Method: viewIsoActionProcedure.
        # Description: The procedure for setting the isometric view of a CAD model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.View_Iso()
        parent.canvas._display.Repaint()

class setWireframeAction(QAction):
    """
    # Class: setWireframeAction.
    # Description: A PyQt5 action that displays a model in wireframe visualization.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Exibir Modelo Wireframe', parent)
        self.setStatusTip('Exibe um modelo Wireframe do CAD atual')
        self.setIconText('Modelo Wireframe')
        self.triggered.connect(lambda: self.setWireframeActionProcedure(parent))

    def setWireframeActionProcedure(self, parent):
        """
        # Method: setWireframeActionProcedure.
        # Description: The procedure for displaying a model in wireframe visualization.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.SetModeWireFrame()
        parent.canvas._display.Repaint()

class setShadedAction(QAction):
    """
    # Class: setShadedAction.
    # Description: A PyQt5 action that displays a shaded (solid) model visualization.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Exibir Modelo Sólido', parent)
        self.setStatusTip('Exibe um modelo sólido do CAD atual')
        self.setIconText('Modelo Sólido')
        self.triggered.connect(lambda: self.setShadedActionProcedure(parent))

    def setShadedActionProcedure(self, parent):
        """
        # Method: setShadedActionProcedure.
        # Description: The procedure for displaying a model in shaded (solid) visualization.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.SetModeShaded()
        parent.canvas._display.Repaint()

class fitAllAction(QAction):
    """
    # Class: fitAllAction.
    # Description: A PyQt5 action that adjusts all elements to fit on the screen.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Ajustar Elementos à Tela', parent)
        self.setStatusTip('Ajusta o zoom para que todos os elementos fiquem no visualizador')
        self.setIconText('Ajustar Elementos')
        self.triggered.connect(lambda: self.fitAllActionProcedure(parent))

    def setShadedActionProcedure(self, parent):
        """
        # Method: fitAllActionProcedure.
        # Description: The procedure for adjusting all elements to fit on the screen.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        parent.canvas._display.FitAll()
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
        self.setIconText('GitHub')
        self.triggered.connect(lambda: webbrowser.open('https://github.com/hideak/pointCloudGenerator'))

class developerPageAction(QAction):
    """
    # Class: projectPageAction.
    # Description: A PyQt5 action that opens the developer's personal webpage.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Abrir https://hideak.github.io', parent)
        self.setStatusTip('Exibe o site do desenvolvedor, incluindo projetos em progresso')
        self.setIconText('Página do Desenvolvedor')
        self.triggered.connect(lambda: webbrowser.open('https://hideak.github.io'))

class emailAction(QAction):
    """
    # Class: emailAction.
    # Description: A PyQt5 action that opens an email prompt for reporting bugs.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\mail.svg'), 'Enviar Email ao Desenvolvedor', parent)
        self.setStatusTip('Abre uma janela para envio de email ao desenvolvedor')
        self.setIconText('Email')
        self.triggered.connect(lambda: webbrowser.open('mailto:willianhideak@hotmail.com'))

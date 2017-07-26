# Module: main.py
# Description: This is the main file of the program. It will run the initial UI Elements.

# Autor: Willian Hideak Arita da Silva.
# Last edit: June, 22, 2017.

# System Imports:
import sys
import getpass
import os

# Importing the load_backend e get_qt_modules from pythonOCC:
from OCC.Display.backend import get_qt_modules
from OCC.Display.backend import load_backend
load_backend('qt-pyqt5')

# Loading the viewer:
from OCC.Display.qtDisplay import qtViewer3d

# Loading PyQt5 Modules for the interface:
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, \
                            QDockWidget, QFileDialog, QTreeWidget, QWidget, \
                            QPushButton, QToolBar, QTreeView, QInputDialog
from PyQt5.QtCore import QCoreApplication, QDir
from PyQt5.QtGui import QIcon

QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()

# Importing PyQt5 elements:
from Interface.DefectsMenu import *
from Interface.DiscretizeMenu import *
from Interface.LoadingMenu import *
from Actions.ActionList import *

# Defining the Main Window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Defining Main Window Properties:
        self.setWindowTitle('Gerador de Nuvem de Pontos v0.41')
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.resize(1300, 650)

        # Defining modeless windows:
        self.loadingWindow = loadingMenu()

        # Control Variables. Used to storage current session information.
        # Information about the current opened file.
        self.lastPath = 'C:\\Users\\' + getpass.getuser() + '\\Desktop'
        self.activeCADFile = None
        self.activeCloudFile = None

        # Information about active docks and windows.
        self.leftDockMenu = None
        self.leftDockWidget = None
        self.rightDockMenu = None
        self.rightDockWidget = None

        # Information about the loaded IGES Entities.
        self.entitiesObject = []
        self.entitiesList = []
        self.shapeList = []
        self.selectedShape = None

        # Information about the loaded Cloud Points.
        self.faceSequenceNumbers = []
        self.faceNormalVectors = []
        self.cloudPointsList = []

        # Information about selected parameters:
        self.shapeParameter1 = None
        self.shapeParameter2 = None
        self.shapeParameter3 = None

        # Defining Actions.
        welcome = welcomeAction(self)
        entities = entitiesAction(self)
        importCAD = importAction(self)
        exportCAD = exportAction(self)
        cloud = cloudAction(self)
        autoDiscretize = autoDiscretizeAction(self)
        defects = defectsAction(self)
        close = closeAction(self)
        exitApp = exitAction(self)
        translationDefects = translationDefectsAction(self)
        light = lightAction(self)
        dark = darkAction(self)
        github = githubAction(self)

        # Defining the default Side Widgets:
        welcome.welcomeActionProcedure(self)

        # Defining the MenuBar:
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('Arquivo')
        fileMenu.addAction(welcome)
        fileMenu.addAction(importCAD)
        fileMenu.addAction(close)
        fileMenu.addAction(exitApp)
        panelsMenu = menubar.addMenu('Painéis e Menus')
        panelsMenu.addAction(exportCAD)
        panelsMenu.addAction(entities)
        panelsMenu.addAction(cloud)
        panelsMenu.addAction(autoDiscretize)
        panelsMenu.addAction(defects)
        panelsMenu.addAction(translationDefects)
        menubar.addMenu('Importar')
        menubar.addMenu('Exportar')
        visualizationMenu = menubar.addMenu('Visualização')
        visualizationMenu.addAction(light)
        visualizationMenu.addAction(dark)
        aboutMenu = menubar.addMenu('Sobre este Aplicativo')
        aboutMenu.addAction(github)

        # Defining the StatusBar:
        self.statusBar()

        # Setting the Viewer as a Widget of the Main Window:
        self.canvas = qtViewer3d(self)
        self.setCentralWidget(self.canvas)

        # Defining the ToolBar:
        self.toolbar = self.addToolBar('Tools')
        self.toolbar.addAction(welcome)
        self.toolbar.addAction(entities)
        self.toolbar.addAction(importCAD)
        self.toolbar.addAction(exportCAD)
        self.toolbar.addAction(cloud)
        self.toolbar.addAction(defects)
        self.toolbar.addSeparator()
        self.toolbar.addAction(close)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exitApp)
        self.toolbar.setToolButtonStyle(3)
        self.toolbar.setMovable(False)

    # Substituting the default method for closing the application.
    def closeEvent(self, event):
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
            event.accept()
        elif box.clickedButton() == buttonNo:
            event.ignore()

# Setting the exhibition of elements and configuring the screen:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    window.canvas.InitDriver()
    window.canvas.qApp = app
    display = window.canvas._display
    display.set_bg_gradient_color(255, 255, 255, 210, 255, 222)
    display.display_trihedron()
    sys.exit(app.exec_())

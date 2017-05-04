# Module: main.py
# Description: This is the main file of the program. It will run the initial UI Elements.

# Autor: Willian Hideak Arita da Silva.
# Last edit: May, 05, 2017.

# System Imports:
import sys
import getpass
import os

# Discretize Functions Import:
from Import.IGESImport import *
from Discretization.DiscretizeFace import *

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
from Interface.DiscretizeMenu import *
from Actions.ActionList import *

# Defining the Main Window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Defining Main Window Properties:
        self.setWindowTitle('Gerador de Nuvem de Pontos v0.30')
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.resize(1300, 800)
        
        # Control Variables. Used to storage current session information.
        self.lastPath = 'C:\\Users\\' + getpass.getuser() + '\\Desktop'
        self.activeFile = None
        self.activeMiniToolbar = None
        self.activeLeftWidget = None
        self.activeRightWidget = None
        self.activeCentralWidget = None
        self.activeCloudFile = None
        self.entitiesList = []

        # Defining Actions.
        welcome = welcomeAction(self)
        entities = entitiesAction(self)
        importCAD = importAction(self)
        exportCAD = exportAction(self)
        cloud = cloudAction(self)
        close = closeAction(self)
        exitApp = exitAction(self)
        
        # Defining the MenuBar:
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Arquivo')
        fileMenu.addAction(importCAD)
        fileMenu.addAction(exitApp)
        menubar.addMenu('&Editar')
        menubar.addMenu('&Ferramentas')
        menubar.addMenu('&Importar')
        menubar.addMenu('&Exportar')
        menubar.addMenu('&Janela')
        menubar.addMenu('&Ajuda')
        
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
        self.toolbar.addSeparator()
        self.toolbar.addAction(close)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exitApp)
        self.toolbar.setToolButtonStyle(3)
        self.toolbar.setMovable(False)

        # Defining the Welcome Widget:
        welcome = QtWidgets.QTextEdit()
        fchangelog = open('..\\src\\Interface\\welcome.txt', 'r')
        with fchangelog:
            changelog = fchangelog.read()
            welcome.setText(changelog)
        
        # Setting the Welcome Widget as a Lateral Widget:
        self.dock = QDockWidget('Bem-Vindo!', self)
        self.dock.setWidget(welcome)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock)

    # Defining Customized Actions:
    def autoDiscretization(self):
        precision, ok = QInputDialog.getText(self, 'Tamanho do Grid', 'Digite o tamanho ' +
                                             'n para obter uma\ndiscretização quadriculada ' +
                                             'n por n:')
        precision = int(precision)
        file = loadIGESFile(self.activeFile)
        data = getRawData(file)
        param = getRawParameters(file)
        res = loadEntities(data, param)
        points = discretizeModel(res, precision)
        generatePcd(points)
        self.bunny()
        
    def bunny(event=None):
        pcd_file = open(os.path.join('', 'CloudData.pcd'), 'r').readlines()[10:]
        # create the point_cloud
        pc = Graphic3d_ArrayOfPoints(len(pcd_file))
        for line in pcd_file:
            x, y, z = map(float, line.split())
            pc.AddVertex(x, y, z)
        point_cloud = AIS_PointCloud()
        point_cloud.SetPoints(pc.GetHandle())
        ais_context = display.GetContext().GetObject()
        ais_context.Display(point_cloud.GetHandle())

# Setting the exhibition of elements and configuring the screen:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.canvas.InitDriver()
    window.canvas.qApp = app
    display = window.canvas._display
    display.set_bg_gradient_color(255, 255, 255, 210, 255, 222)
    display.display_trihedron()
    sys.exit(app.exec_())

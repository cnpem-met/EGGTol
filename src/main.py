# Module: main.py
# Description: This is the main file of the program. It will run the initial UI Elements.

# Autor: Willian Hideak Arita da Silva
# Last edit: April, 24, 2017.

# System Imports:
import sys
import getpass
import os

# Discretize Functions Import:
from Import.IGESImport import *
from Discretization.DiscretizeFace import *

# Callback Imports:
'''
These Imports were used to implement the callback functions.
The callback functions retuns content from the model to be displayed in the python console.
These functionalities can be removed in a final version of the software.
'''
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox, BRepPrimAPI_MakeTorus
from OCC.Bnd import Bnd_Box
from OCC.BRepBndLib import brepbndlib_Add
from OCC.Display.SimpleGui import init_display
from OCC.AIS import AIS_Shape, AIS_PointCloud, AIS_ColoredShape
from OCC.Graphic3d import Graphic3d_ArrayOfPoints
from Topology.core_topology_traverse import Topo
from OCC.Display.OCCViewer import rgb_color

# Importing the load_backend e get_qt_modules from pythonOCC:
from OCC.Display.backend import get_qt_modules
from OCC.Display.backend import load_backend

# Setting the backend to PyQt version 5:
load_backend('qt-pyqt5')

# Loading the viewer:
from OCC.Display.qtDisplay import qtViewer3d

# Loading PyQt5 Modules for generating interface:
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, \
                            QDockWidget, QFileDialog, QTreeWidget, QWidget, \
                            QPushButton, QToolBar, QTreeView, QFileSystemModel, \
                            QInputDialog
from PyQt5.QtCore import QCoreApplication, QDir
from PyQt5.QtGui import QIcon

# Importing PyQt5 elements:
from Interface.DiscretizeMenu import discretizeMenu
from Actions.ActionList import welcomeAction

QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()

# Defining the Main Window:
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Control Variables. Used to storage current session information.
        self.lastPath = 'C:\\Users\\' + getpass.getuser() + '\\Desktop'
        self.activeFile = None
        self.activeMiniToolbar = None
        self.activeLeftWidget = None
        self.activeRightWidget = None
        self.activeCentralWidget = None
        self.activeCloudFile = None
        
        # Defining Actions:
        welcome = welcomeAction(self)
        
        arquivo = QAction(QIcon("..\\icons\\Server.svg"), 'Entidades', self)
        arquivo.setStatusTip('Exibe a Árvore de Entidades')
        arquivo.setIconText('Entidades')
        
        importar = QAction(QIcon("..\\icons\\inbox.svg"), 'Importar', self)
        importar.setStatusTip('Importar Um Arquivo .IGES')
        importar.setIconText('Importar')
        importar.triggered.connect(self.AbrirArquivo)

        exportar = QAction(QIcon("..\\icons\\outbox.svg"), 'Exportar', self)
        exportar.setStatusTip('Exportar Um Arquivo .IGES')
        exportar.setIconText('Exportar')

        nuvem = QAction(QIcon("..\\icons\\cloud-download.svg"), 'Gerar Nuvem', self)
        nuvem.setStatusTip('Gerar uma Nuvem de Pontos para o Modelo')
        nuvem.setIconText('Gerar Nuvem')
        nuvem.triggered.connect(self.newMenu)

        zoomIn = QAction(QIcon("..\\icons\\zoom-in.svg"), 'Zoom +', self)
        zoomIn.setStatusTip('Aumenta o Zoom')
        zoomIn.setIconText('Zoom +')

        zoomOut = QAction(QIcon("..\\icons\\zoom-out.svg"), 'Zoom -', self)
        zoomOut.setStatusTip('Diminui o Zoom')
        zoomOut.setIconText('Zoom -')

        close = QAction(QIcon("..\\icons\\cross.svg"), 'Fechar', self)
        close.setStatusTip('Fecha o arquivo atual')
        close.setIconText('Fechar')
        close.triggered.connect(self.resetView)

        sair = QAction(QIcon("..\\icons\\circle-cross.svg"), 'Encerrar', self)
        sair.setStatusTip('Encerrar o Programa')
        sair.setIconText('Encerrar')
        sair.triggered.connect(qApp.quit)
        
        # Defining the MenuBar:
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Arquivo')
        fileMenu.addAction(importar)
        fileMenu.addAction(sair)
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
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(welcome)
        self.toolbar.addAction(arquivo)
        self.toolbar.addAction(importar)
        self.toolbar.addAction(exportar)
        self.toolbar.addAction(nuvem)
        self.toolbar.addSeparator()
        self.toolbar.addAction(zoomIn)
        self.toolbar.addAction(zoomOut)
        self.toolbar.addAction(close)
        self.toolbar.addSeparator()
        self.toolbar.addAction(sair)
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
        
        # Defining Main Window Properties:
        self.setWindowTitle('Gerador de Nuvem de Pontos v0.30')
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.resize(1300, 800)

    # Defining Customized Actions:
    def newMenu(self):
        self.dock2 = QDockWidget('Gerar Nuvem de Pontos', self)
        newWindow = discretizeMenu(self.autoDiscretization)
        self.dock2.setWidget(newWindow)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.dock2)
    
    def resetView(self):
        display.EraseAll()

    def AbrirArquivo(self):
        from OCC.IGESControl import IGESControl_Reader
        from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
        fileName = QFileDialog.getOpenFileName(self, 'Abrir Arquivo .IGES', self.lastPath)
        self.lastPath = fileName[0]
        iges_reader = IGESControl_Reader()
        if not fileName[0]:
           return
        status = iges_reader.ReadFile(fileName[0])
        if status == IFSelect_RetDone:
            failsonly = False
            iges_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
            iges_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)
            ok = iges_reader.TransferRoots()
            aResShape = iges_reader.Shape(1)
        else:
            print("Error: Can't Read File.")
        ais = AIS_ColoredShape(aResShape)
        for face in Topo(aResShape).faces():
            ais.SetCustomColor(face, rgb_color(0.5, 0.5, 1))
        display.Context.Display(ais.GetHandle())
        display.FitAll()
        #display.DisplayShape(aResShape, update=True)
        self.activeFile = fileName[0]

    def autoDiscretization(self):
        precision, ok = QInputDialog.getText(self, 'Precision', 'Digite a precisão:')
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

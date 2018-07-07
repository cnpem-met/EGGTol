"""
# Module: main.py
# Description: This is the main file of the application. It can provide a full interface written
and inhirited from the PyQt5 QMainWindow class.
# Author: Willian Hideak Arita da Silva.
"""

# System Imports:
import sys       # sys module is used to call sys.exit() when the application ends.
import getpass   # getpass module is used to get the current user name on Windows.
import os        # os module is used to handle files and directory operations.

# Importing the load_backend and get_qt_modules from pythonOCC:
from OCC.Display.backend import get_qt_modules
from OCC.Display.backend import load_backend
load_backend('qt-pyqt5')

# Loading the viewer:
from OCC.Display.qtDisplay import qtViewer3d

# Loading PyQt5 Modules for the interface:
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

# Getting the PyQt5 modules from the PythonOCC lib:
QtCore, QtGui, QtWidgets, QtOpenGL = get_qt_modules()

# Importing PyQt5 elements and menus from the Interface package:
from Resources.Strings import MyStrings
from Interface.DefectsMenu import *
from Interface.DiscretizeMenu import *
from Interface.LoadingMenu import *
from Actions.ActionList import *

# Defining the Main Window:
class MainWindow(QMainWindow):
    """
    # Class: MainWindow.
    # Description: This class inherits the QMainWindow class from the PyQt5 framework and
    prepare the main contents to be displayed using the initUI() method.
    """

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        # Method: initUI.
        # Description: This method initialize everything in the main window, like its properties
        and User Interface Elements (Buttons, Menus, ToolBars and so on). It also prepares some
        variables for handling the current information of files and CAD models.
        """

        # Defining Main Window Properties:
        # self.light is a property used by the OpenCASCADE modified libraries to decide
        # which cursor model to use.
        self.light = True
        self.title = MyStrings.applicationTitle + ' ' + MyStrings.applicationVersion
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        self.resize(1300, 650)

        # Defining a modeless windows:
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

        # The actual loaded IGES entities into Python objects.
        self.entitiesObject = []

        # The actual pointCloud object loaded:
        self.pointCloudObject = None
        self.pointAspectObject = None

        # The description of each loaded IGES entity for the TreeView.
        self.entitiesList = []
        self.pointsList = []

        # The actual loaded IGES OpenCASCADE Shapes.
        self.shapeList = []
        self.selectedShape = None
        self.selectedSequenceNumber = None

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
        faceDiscretize = faceDiscretizeAction(self)
        defects = defectsAction(self)
        pointsList = pointsListAction(self)
        close = closeAction(self)
        exitApp = exitAction(self)
        translationDefects = translationDefectsAction(self)
        randomDefects = randomDefectsAction(self)
        light = lightAction(self)
        dark = darkAction(self)
        selectionNeutral = selectionNeutralAction(self)
        selectionFace = selectionFaceAction(self)
        selectionEdge = selectionEdgeAction(self)
        selectionVertex = selectionVertexAction(self)
        viewTop = viewTopAction(self)
        viewBottom = viewBottomAction(self)
        viewLeft = viewLeftAction(self)
        viewRight = viewRightAction(self)
        viewFront = viewFrontAction(self)
        viewRear = viewRearAction(self)
        viewIso = viewIsoAction(self)
        setWireframe = setWireframeAction(self)
        setShaded = setShadedAction(self)
        fitAll = fitAllAction(self)
        devPage = developerPageAction(self)
        email = emailAction(self)
        github = githubAction(self)

        # Defining the default Side Widgets:
        welcome.welcomeActionProcedure(self)

        # Defining the MenuBar:
        menubar = self.menuBar()

        fileMenu = menubar.addMenu(MyStrings.menuBarFile)
        fileMenu.addAction(welcome)
        fileMenu.addSeparator()
        fileMenu.addAction(close)
        fileMenu.addAction(exitApp)

        panelsMenu = menubar.addMenu(MyStrings.menuBarPanels)
        panelsMenu.addAction(entities)
        panelsMenu.addAction(importCAD)
        panelsMenu.addAction(exportCAD)
        panelsMenu.addAction(cloud)
        panelsMenu.addAction(defects)
        panelsMenu.addAction(pointsList)
        panelsMenu.addSeparator()
        panelsMenu.addAction(autoDiscretize)
        panelsMenu.addAction(faceDiscretize)
        panelsMenu.addSeparator()
        panelsMenu.addAction(translationDefects)
        panelsMenu.addAction(randomDefects)

        visualizationMenu = menubar.addMenu(MyStrings.menuBarVisualization)
        visualizationMenu.addAction(light)
        visualizationMenu.addAction(dark)
        visualizationMenu.addSeparator()
        visualizationMenu.addAction(viewTop)
        visualizationMenu.addAction(viewBottom)
        visualizationMenu.addAction(viewLeft)
        visualizationMenu.addAction(viewRight)
        visualizationMenu.addAction(viewFront)
        visualizationMenu.addAction(viewRear)
        visualizationMenu.addSeparator()
        visualizationMenu.addAction(viewIso)
        visualizationMenu.addSeparator()
        visualizationMenu.addAction(setWireframe)
        visualizationMenu.addAction(setShaded)
        visualizationMenu.addSeparator()
        visualizationMenu.addAction(fitAll)

        selectionMenu = menubar.addMenu(MyStrings.menuBarSelection)
        selectionMenu.addAction(selectionNeutral)
        selectionMenu.addAction(selectionFace)
        selectionMenu.addAction(selectionEdge)
        selectionMenu.addAction(selectionVertex)

        aboutMenu = menubar.addMenu(MyStrings.menuBarAbout)
        aboutMenu.addAction(github)
        aboutMenu.addAction(devPage)
        aboutMenu.addSeparator()
        aboutMenu.addAction(email)

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
        self.toolbar.addAction(pointsList)
        self.toolbar.addSeparator()
        self.toolbar.addAction(close)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exitApp)
        self.toolbar.setToolButtonStyle(3)
        self.toolbar.setMovable(False)

    # Overriding the default method for closing the application.
    def closeEvent(self, event):
        """
        # Method: closeEvent.
        # Description: This method overrides the default method for closing the application.
        It just displays a confirmation window asking permission for end the actual work.
        # Parameters: * QCloseEvent event = The default event of the overrided method.
        """

        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        box.setWindowTitle(MyStrings.popupExitTitle)
        box.setText(MyStrings.popupExitMessage)
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        buttonYes = box.button(QMessageBox.Yes)
        buttonYes.setText(MyStrings.popupExitButtonOK)
        buttonNo = box.button(QMessageBox.No)
        buttonNo.setText(MyStrings.popupExitButtonCancel)
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
    display.DisableAntiAliasing()
    display.SetSelectionModeNeutral()
    display.set_bg_gradient_color(255, 255, 255, 210, 255, 222)
    display.display_trihedron()
    sys.exit(app.exec_())

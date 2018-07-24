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
from Actions.Functions import rebuildCloud

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
        super().__init__(QIcon('..\\icons\\desktopIcons\\egg.png'), MyStrings.actionWelcomePrettyName, parent)
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
        switchLeftPanels(widget, MyStrings.actionWelcomeName, MyStrings.actionWelcomePrettyName,
                         parent, False)

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
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
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

        super().__init__(QIcon('..\\icons\\inbox.svg'), MyStrings.actionImportPrettyName, parent)
        self.setStatusTip(MyStrings.actionImportStatusTip)
        self.setIconText(MyStrings.actionImportIconText)
        self.triggered.connect(lambda: self.importActionProcedure(parent))

    def importActionProcedure(self, parent):
        """
        # Method: importActionProcedure
        # Description: A procedure for opening the Import Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.ImportMenu import importMenu
        widget = importMenu(parent)
        switchRightPanels(widget, MyStrings.actionImportName,  MyStrings.actionImportPrettyName, parent, True)

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

        super().__init__(QIcon('..\\icons\\outbox.svg'), MyStrings.actionExportPrettyName, parent)
        self.setStatusTip(MyStrings.actionExportStatusTip)
        self.setIconText(MyStrings.actionExportIconText)
        self.triggered.connect(lambda: self.exportActionProcedure(parent))

    def exportActionProcedure(self, parent):
        """
        # Method: exportActionProcedure.
        # Description: A procedure for opening the Export Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.ExportMenu import exportMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = exportMenu(parent)
        switchRightPanels(widget, MyStrings.actionExportName, MyStrings.actionExportPrettyName, parent, True)

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

        super().__init__(QIcon('..\\icons\\cloud.svg'), MyStrings.actionCloudPrettyName, parent)
        self.setStatusTip(MyStrings.actionCloudStatusTip)
        self.setIconText(MyStrings.actionCloudIconText)
        self.triggered.connect(lambda: self.cloudActionProcedure(parent))

    def cloudActionProcedure(self, parent):
        """
        # Method: cloudActionProcedure.
        # Description: A procedure for opening the Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.DiscretizeMenu import discretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = discretizeMenu(parent)
        switchRightPanels(widget, MyStrings.actionCloudName, MyStrings.actionCloudPrettyName, parent, True)

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

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionAutoDiscretizePrettyName, parent)
        self.setStatusTip(MyStrings.actionAutoDiscretizeStatusTip)
        self.triggered.connect(lambda: self.autoDiscretizeActionProcedure(parent))

    def autoDiscretizeActionProcedure(self, parent):
        """
        # Method: autoDiscretizeActionProcedure.
        # Description: The procedure for opening the Auto Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.AutoDiscretizeMenu import autoDiscretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = autoDiscretizeMenu(parent)
        switchRightPanels(widget, MyStrings.actionAutoDiscretizeName, MyStrings.actionAutoDiscretizePrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionFaceDiscretizePrettyName, parent)
        self.setStatusTip(MyStrings.actionFaceDiscretizeStatusTip)
        self.triggered.connect(lambda: self.faceDiscretizeActionProcedure(parent))

    def faceDiscretizeActionProcedure(self, parent):
        """
        # Method: faceDiscretizeActionProcedure.
        # Description: The procedure for opening the Face Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.FaceDiscretizeMenu import faceDiscretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = faceDiscretizeMenu(parent)
        switchRightPanels(widget, MyStrings.actionFaceDiscretizeName, MyStrings.actionFaceDiscretizePrettyName,
                          parent, True)

class surfaceDiscretizeAction(QAction):
    """
    # Class: surfaceDiscretizeAction.
    # Description: A PyQt5 action that opens the Surface Discretize Menu side widget.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionSurfaceDiscretizePrettyName, parent)
        self.setStatusTip(MyStrings.actionSurfaceDiscretizeStatusTip)
        self.triggered.connect(lambda: self.surfaceDiscretizeActionProcedure(parent))

    def surfaceDiscretizeActionProcedure(self, parent):
        """
        # Method: surfaceDiscretizeActionProcedure.
        # Description: The procedure for opening the Surface Discretize Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.SurfaceDiscretizeMenu import surfaceDiscretizeMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = surfaceDiscretizeMenu(parent)
        switchRightPanels(widget, MyStrings.actionSurfaceDiscretizeName, MyStrings.actionSurfaceDiscretizePrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\move.svg'), MyStrings.actionDefectsPrettyName, parent)
        self.setStatusTip(MyStrings.actionDefectsStatusTip)
        self.setIconText(MyStrings.actionDefectsIconText)
        self.triggered.connect(lambda: self.defectsActionProcedure(parent))

    def defectsActionProcedure(self, parent):
        """
        # Method: defectsActionProcedure.
        # Description: The procedure for opening the Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.DefectsMenu import defectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, MyStrings.popupNoCloudTitle,
                                    MyStrings.popupNoCloudDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = defectsMenu(parent)
        switchRightPanels(widget, MyStrings.actionDefectsName, MyStrings.actionDefectsPrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\paper.svg'), MyStrings.actionPointsListPrettyName, parent)
        self.setStatusTip(MyStrings.actionPointsListStatusTip)
        self.setIconText(MyStrings.actionPointsListIconText)
        self.triggered.connect(lambda: self.pointsListActionProcedure(parent))

    def pointsListActionProcedure(self, parent):
        """
        # Method: pointsListActionProcedure.
        # Description: The procedure for opening the Points List Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        from Interface.PointsListMenu import pointsListMenu
        if not parent.activeCloudFile:
            QMessageBox.information(parent, MyStrings.popupNoCloudTitle,
                                    MyStrings.popupNoCloudDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = pointsListMenu(parent)
        switchLeftPanels(widget, MyStrings.actionPointsListName, MyStrings.actionPointsListPrettyName,
                         parent, False)

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

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionTranslationPrettyName, parent)
        self.setStatusTip(MyStrings.actionTranslationStatusTip)
        self.triggered.connect(lambda: self.translationDefectsActionProcedure(parent))

    def translationDefectsActionProcedure(self, parent):
        """
        # Method: translationDefectsActionProcedure.
        # Description: The procedure for opening the Translational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.TranslationDefectsMenu import translationDefectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, MyStrings.popupNoCloudTitle,
                                    MyStrings.popupNoCloudDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = translationDefectsMenu(parent)
        switchRightPanels(widget, MyStrings.actionTranslationName, MyStrings.actionTranslationPrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionRotationPrettyName, parent)
        self.setStatusTip(MyStrings.actionRotationStatusTip)
        self.triggered.connect(lambda: self.rotationalDefectsActionProcedure(parent))

    def rotationalDefectsActionProcedure(self, parent):
        """
        # Method: rotationalDefectsActionProcedure.
        # Description: The procedure for opening the Rotational Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.RotationalDefectsMenu import rotationalDefectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, MyStrings.popupNoCloudTitle,
                                    MyStrings.popupNoCloudDescription,
                                    MessageBox.Ok, QMessageBox.Ok)
            return
        widget = rotationalDefectsMenu(parent)
        switchRightPanels(widget, MyStrings.actionRotationName, MyStrings.actionRotationPrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionRandomPrettyName, parent)
        self.setStatusTip(MyStrings.actionRandomStatusTip)
        self.triggered.connect(lambda: self.randomDefectsActionProcedure(parent))

    def randomDefectsActionProcedure(self, parent):
        """
        # Method: randomDefectsActionProcedure.
        # Description: The procedure for opening the Random Defects Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        from Interface.RandomDefectsMenu import randomDefectsMenu
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        if not parent.activeCloudFile:
            QMessageBox.information(parent, MyStrings.popupNoCloudTitle,
                                    MyStrings.popupNoCloudDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return
        widget = randomDefectsMenu(parent)
        switchRightPanels(widget, MyStrings.actionRandomName, MyStrings.actionRandomPrettyName,
                          parent, True)

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

        super().__init__(QIcon('..\\icons\\cross.svg'), MyStrings.actionClosePrettyName, parent)
        self.setStatusTip(MyStrings.actionCloseStatusTip)
        self.setIconText(MyStrings.actionCloseIconText)
        self.triggered.connect(lambda: self.closeActionProcedure(parent))

    def closeActionProcedure(self, parent):
        """
        # Method: closeActionProcedure.
        # Description: The procedure for closing the current opened IGES file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Checking if there is a current opened file:
        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

        # Creating a confirmation dialog asking for permission to close the file:
        box = QMessageBox()
        box.setIcon(QMessageBox.Question)
        box.setWindowIcon(QIcon('..\\icons\\desktopIcons\\main.png'))
        box.setWindowTitle(MyStrings.popupCloseTitle)
        box.setText(MyStrings.popupCloseMessage)
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        box.setDefaultButton(QMessageBox.No)
        buttonYes = box.button(QMessageBox.Yes)
        buttonYes.setText(MyStrings.popupCloseButtonOK)
        buttonNo = box.button(QMessageBox.No)
        buttonNo.setText(MyStrings.popupCloseButtonCancel)
        box.exec_()

        # Executing a routine for closing the current file:
        if box.clickedButton() == buttonYes:

            # Importing the Welcome Menu Side Widget:
            from Interface.WelcomeMenu import welcomeMenu

            # Removing all the current displayed side widgets:
            parent.removeDockWidget(parent.leftDockMenu)
            parent.removeDockWidget(parent.rightDockMenu)
            parent.leftDockMenu = parent.leftDockWidget = None
            parent.rightDockMenu = parent.rightDockWidget = None

            # Redisplaying the Welcome Menu
            widget = welcomeMenu(parent)
            switchLeftPanels(widget, MyStrings.actionWelcomeName, MyStrings.actionWelcomePrettyName,
                            parent, False)

            # Defining the default display mode for a clean session:
            parent.canvas._display.SetSelectionModeNeutral()
            parent.canvas._display.Context.CloseAllContexts()
            parent.canvas._display.Context.RemoveAll()
            parent.canvas._display.Repaint()

            # Definint the original window title:
            parent.setWindowTitle(parent.title)

            # Erasing all the current saved parameters:
            parent.activeCADFile = None
            parent.activeCloudFile = None
            parent.entitiesObject = []
            parent.pointCloudObject = None
            parent.pointAspectObject = None
            parent.entitiesList = []
            parent.pointsList = []
            parent.shapeList = []
            parent.selectedShape = None
            parent.selectedSequenceNumber = None
            parent.faceSequenceNumbers = []
            parent.faceNormalVectors = []
            parent.cloudPointsList = []
            parent.shapeParameter1 = None
            parent.shapeParameter2 = None
            parent.shapeParameter3 = None

            # Applying an isometric visualization mode:
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

        super().__init__(QIcon('..\\icons\\circle-cross.svg'), MyStrings.actionExitPrettyName, parent)
        self.setStatusTip(MyStrings.actionExitStatusTip)
        self.setIconText(MyStrings.actionExitIconText)
        self.triggered.connect(lambda: self.exitActionProcedure())

    def exitActionProcedure(self):
        """
        # Method: exitActionProcedure.
        # Description: The procedure for closing the application and all the opened files.
        """
        # Create a confirmation dialog asking for permission to quit the application:
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

        # Executing a routine for quitting the application:
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
        super().__init__(QIcon('..\\icons\\moon.svg'), MyStrings.actionDarkPrettyName, parent)
        self.setStatusTip(MyStrings.actionDarkStatusTip)
        self.setIconText(MyStrings.actionDarkIconText)
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
        super().__init__(QIcon('..\\icons\\sun.svg'), MyStrings.actionLightPrettyName, parent)
        self.setStatusTip(MyStrings.actionLightStatusTip)
        self.setIconText(MyStrings.actionLightIconText)
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
        super().__init__(QIcon('..\icons\\arrow-right.svg'), MyStrings.actionSelectionNeutralPrettyName, parent)
        self.setStatusTip(MyStrings.actionSelectionNeutralStatusTip)
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
        super().__init__(QIcon('..\icons\\arrow-right.svg'), MyStrings.actionSelectionFacePrettyName, parent)
        self.setStatusTip(MyStrings.actionSelectionFaceStatusTip)
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
        super().__init__(QIcon('..\icons\\arrow-right.svg'), MyStrings.actionSelectionEdgePrettyName, parent)
        self.setStatusTip(MyStrings.actionSelectionEdgeStatusTip)
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
        super().__init__(QIcon('..\icons\\arrow-right.svg'), MyStrings.actionSelectionVertexPrettyName, parent)
        self.setStatusTip(MyStrings.actionSelectionVertexStatusTip)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewTopPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewTopStatusTip)
        self.setIconText(MyStrings.actionViewTopIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewBottomPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewBottomStatusTip)
        self.setIconText(MyStrings.actionViewBottomIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewLeftPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewLeftStatusTip)
        self.setIconText(MyStrings.actionViewLeftIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewRightPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewRightStatusTip)
        self.setIconText(MyStrings.actionViewRightIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewFrontPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewFrontStatusTip)
        self.setIconText(MyStrings.actionViewFrontIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewRearPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewRearStatusTip)
        self.setIconText(MyStrings.actionViewRearIconText)
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
        super().__init__(QIcon('..\\icons\\box.svg'), MyStrings.actionViewIsoPrettyName, parent)
        self.setStatusTip(MyStrings.actionViewIsoStatusTip)
        self.setIconText(MyStrings.actionViewIsoIconText)
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
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionWireframePrettyName, parent)
        self.setStatusTip(MyStrings.actionWireframeStatusTip)
        self.setIconText(MyStrings.actionWireframeIconText)
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
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionShadedPrettyName, parent)
        self.setStatusTip(MyStrings.actionShadedStatusTip)
        self.setIconText(MyStrings.actionShadedIconText)
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
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionFitAllPrettyName, parent)
        self.setStatusTip(MyStrings.actionFitAllStatusTip)
        self.setIconText(MyStrings.actionFitAllIconText)
        self.triggered.connect(lambda: self.fitAllActionProcedure(parent))

    def fitAllActionProcedure(self, parent):
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
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionGithubPrettyName, parent)
        self.setStatusTip(MyStrings.actionGithubStatusTip)
        self.setIconText(MyStrings.actionGithubIconText)
        self.triggered.connect(lambda: webbrowser.open('https://github.com/hideak/EGGTol'))

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
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), MyStrings.actionDeveloperPrettyName, parent)
        self.setStatusTip(MyStrings.actionDeveloperStatusTip)
        self.setIconText(MyStrings.actionDeveloperIconText)
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
        super().__init__(QIcon('..\\icons\\mail.svg'), MyStrings.actionEmailPrettyName, parent)
        self.setStatusTip(MyStrings.actionEmailStatusTip)
        self.setIconText(MyStrings.actionEmailIconText)
        self.triggered.connect(lambda: webbrowser.open('mailto:whideak@hotmail.com'))

class deletePointAction(QAction):
    """
    # Class: deletePonitAction.
    # Description: A PyQt5 action that delete selected points or group of points.
    """
    def __init__(self, parent, currentLevel, currentInnerIndex, currentOuterIndex):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
                      * Int currentIndex =
                      * Int currentLevel =
                      * Int currentInnerIndex =
                      * Int currentOuterIndex =
        """
        super().__init__("Delete this group/point", parent)
        self.triggered.connect(lambda: self.deletePointActionProcedure(parent))
        self.currentLevel = currentLevel
        self.currentInnerIndex = currentInnerIndex
        self.currentOuterIndex = currentOuterIndex

    def deletePointActionProcedure(self, parent):
        """
        # Method: deletePointActionProcedure.
        # Description: The procedure for deleting points or a group of points.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        from Actions.ActionList import pointsListAction
        # Checking the current level of the selected item and applying the delete process:
        if(self.currentLevel == 0):
            if(self.currentOuterIndex == 5):
                parent.faceSequenceNumbers = []
                parent.faceNormalVectors = []
                parent.cloudPointsList = []
            elif(self.currentOuterIndex >= 7):
                del parent.faceSequenceNumbers[self.currentOuterIndex-7]
                del parent.faceNormalVectors[self.currentOuterIndex-7]
                del parent.cloudPointsList[self.currentOuterIndex-7]
        elif(self.currentLevel == 1):
            del parent.faceNormalVectors[self.currentOuterIndex-7][self.currentInnerIndex]
            del parent.cloudPointsList[self.currentOuterIndex-7][self.currentInnerIndex]

        # Rebuilding the cloud and updating the Point List Side Widget:
        rebuildCloud(parent)
        action = pointsListAction(parent)
        action.pointsListActionProcedure(parent)
        action.pointsListActionProcedure(parent)

class saveProjectAction(QAction):
    """
    # Class: saveProjectAction.
    # Description: A PyQt5 action that saves the current point cloud state on the hard drive
    using a new file specification for the software.
    """

    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Save Point Cloud State', parent)
        self.setStatusTip('Save the current state of the point cloud on the hard drive.')
        self.setIconText('Save')
        self.triggered.connect(lambda: self.saveProjectActionProcedure(parent))

    def saveProjectActionProcedure(self, parent):
        """
        # Method: saveProjectActionProcedure.
        # Description: The procedure for saving the current point cloud.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # PyQt5 Imports:
        from PyQt5.QtWidgets import QFileDialog

        # Invoking a file dialog for saving the current state of the point cloud:
        defaultName = (parent.lastPath).split('.')[0:-1]
        defaultName = '.'.join(defaultName)
        defaultName = defaultName + '.eggproj'
        if(defaultName == '.eggproj'):
            defaultName = 'Empty.eggproj'
        fileName = QFileDialog.getSaveFileName(parent, 'Save Point Cloud State', defaultName,
                                               'EGGTol Project File (*.eggproj)')[0]

        # Checking if the provided filename is valid:
        if not fileName:
            return

        # Opening a file to save the current project:
        file = open(fileName, 'w')

        # Preparing the data for being stored:
        data = '# EGGTol Project File (.eggproj)\n'
        data += '# File for storing cloud data, normal directions and face sequence numbers\n'
        data += '# Content marked with a # will be considered as comments on the file\n'
        data += 'applicationVersion\n'
        data += str(MyStrings.applicationVersion) + '\n'
        data += 'activeCloudFile\n'
        data += str(parent.activeCloudFile) + '\n'
        data += 'faceSequenceNumbers\n'
        for element in parent.faceSequenceNumbers:
            data += str(element) + ','
        data += '\n'
        data += 'faceNormalVectors\n'
        for element in parent.faceNormalVectors:
            for subelement in element:
                data += str(subelement[0]) + ' '
                data += str(subelement[1]) + ' '
                data += str(subelement[2]) + ','
            data += ';'
        data += '\n'
        data += 'cloudPointsList\n'
        for element in parent.cloudPointsList:
            for subelement in element:
                data += str(subelement[0]) + ' '
                data += str(subelement[1]) + ' '
                data += str(subelement[2]) + ','
            data += ';'
        data += '\n'

        # Dumping all the gathered data to the informed file.
        file.write(data)
        file.close()

class loadProjectAction(QAction):
    """
    # Class: loadProjectAction.
    # Description: A PyQt5 action that loads a previous saved point cloud state using a
    new file specification for the software.
    """
    def __init__(self, parent):
        """
        # Method: __init__.
        # Description: The init method for initializing the inhirited properties.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        super().__init__(QIcon('..\\icons\\arrow-right.svg'), 'Load Point Cloud State', parent)
        self.setStatusTip('Load a previous saved point cloud state on the project.')
        self.setIconText('Load')
        self.triggered.connect(lambda: self.loadProjectActionProcedure(parent))

    def loadProjectActionProcedure(self, parent):
        """
        # Method: loadProjectActionProcedure.
        # Description: The procedure for loading a previous saved project.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # PyQt5 Imports:
        from PyQt5.QtWidgets import QFileDialog

        # Local Imports:
        from Actions.Functions import rebuildCloud

        # Invoking a file dialog for loading the current state of the point cloud:
        fileName = QFileDialog.getOpenFileName(parent, 'Load Point Cloud State', parent.lastPath,
                                               'EGG Tol Project File (*.eggproj)')[0]

        # Checking if the provided filename is valid:
        if not fileName:
            return

        # Opening a file to save the current project:
        file = open(fileName, 'r')

        # Restoring the parameters:
        parent.activeCloudFile = ''
        parent.faceSequenceNumbers = []
        parent.faceNormalVectors = []
        parent.cloudPointsList = []

        line = file.readline()
        while line:
            if line[0:15] == 'activeCloudFile':
                line = file.readline()[0:-1]
                parent.activeCloudFile = line
            elif line[0:19] == 'faceSequenceNumbers':
                line = file.readline()[0:-1]
                line = line.split(',')[0:-1]
                line = [int(element) for element in line]
                parent.faceSequenceNumbers = line
            elif line[0:17] == 'faceNormalVectors':
                line = file.readline()[0:-1]
                line = line.split(';')[0:-1]
                line = [element.split(',')[0:-1] for element in line]
                line = [[subelement.split(' ') for subelement in element] for element in line]
                line = [[tuple([float(value) for value in subelement]) for subelement in element] for element in line]
                parent.faceNormalVectors = line
            elif line[0:15] == 'cloudPointsList':
                line = file.readline()[0:-1]
                line = line.split(';')[0:-1]
                line = [element.split(',')[0:-1] for element in line]
                line = [[subelement.split(' ') for subelement in element] for element in line]
                line = [[tuple([float(value) for value in subelement]) for subelement in element] for element in line]
                parent.cloudPointsList = line
            line = file.readline()

        # Updating the visualization:
        rebuildCloud(parent)

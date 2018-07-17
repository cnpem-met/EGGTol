"""
# Module: ImportMenu.py
# Description: This module contains the Import Side Widget Menu UI for importing data into the
application. These data can be a point cloud or an IGES model.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QToolButton, QMessageBox, QFileDialog

# OpenCASCADE Imports:
from OCC.IGESControl import IGESControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity

# Local Imports:
from Import.IGESImport import loadIGESFile, loadEntities, getRawData, getRawParameters
from Resources.Strings import MyStrings

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

        label1 = QLabel(MyStrings.importDescription, self)
        grid.addWidget(label1, 0, 0, 1, 1)

        btn1 = QToolButton()
        btn1.setText(MyStrings.importOptionIges)
        btn1.clicked.connect(lambda: self.importIges(parent))
        btn1.setMinimumHeight(50)
        btn1.setMinimumWidth(266)
        grid.addWidget(btn1, 2, 0)

        btn2 = QToolButton()
        btn2.setText(MyStrings.importOptionPcd)
        btn2.clicked.connect(lambda: self.importPcd(parent))
        btn2.setMinimumHeight(50)
        btn2.setMinimumWidth(266)
        btn2.setEnabled(False)
        grid.addWidget(btn2, 3, 0)

        grid.setColumnStretch(0, 1)
        grid.setRowStretch(4, 1)

    def importIges(self, parent):
        """
        # Method: exportIges
        # Description: This method imports an IGES file to the current visualization.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Checking if there is already an opened file:
        if parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupOpenedIgesTitle,
                                    (MyStrings.popupOpenedIgesDescription1 + str(parent.activeCADFile) +
                                    MyStrings.popupOpenedIgesDescription2), QMessageBox.Ok, QMessageBox.Ok)
            return

        # Invoking a File Dialog for selecting the IGES file:
        fileName = QFileDialog.getOpenFileName(parent, MyStrings.importIgesTitle, parent.lastPath,
                                               MyStrings.importIgesFormat)

        # Checking if the informed path is a valid file:
        if not fileName[0]:
            return

        # Starting the loading window:
        parent.loadingWindow.show()
        parent.loadingWindow.activateWindow()

        # Setting the correct filename to call the OpenCASCADE IGES Reader function:
        parent.lastPath = fileName[0]
        Reader = IGESControl_Reader()
        status = Reader.ReadFile(fileName[0])

        # Checking if the file were read successfully and creating a OpenCASCADE shape object:
        shape = None
        if status == IFSelect_RetDone:
            Reader.TransferList(Reader.GiveList('xst-model-all'))
            for i in range(1, Reader.NbShapes()+1):
                parent.shapeList.append(Reader.Shape(i))
            shape = Reader.Shape(1)

        else:
            QMessageBox.information(parent, MyStrings.popupInvalidIgesFileTitle,
                                    MyStrings.popupInvalidIgesFileDescription, QMessageBox.Ok, QMessageBox.Ok)
            parent.loadingWindow.close()
            return

        # Displaying the loaded entity as an OpenCASCADE shape:
        parent.canvas._display.DisplayShape(shape, update=True)

        # Defining some visualization parameters:
        parent.canvas._display.FitAll()
        parent.canvas._display.ZoomFactor(0.6)
        parent.activeCADFile = fileName[0]
        parent.setWindowTitle(parent.title + ' - ' + fileName[0])

        # Loading the IGES entities as Python objects for generating the entitiesList:
        myfile = loadIGESFile(parent.activeCADFile)
        parent.entitiesObject = loadEntities(getRawData(myfile), getRawParameters(myfile))
        for entity in parent.entitiesObject:
            if(entity != None):
                parent.entitiesList.append(entity.description())
            else:
                parent.entitiesList.append((MyStrings.nonImplementedEntity, []))
        parent.loadingWindow.close()

    def importPcd(self, parent):
        """
        # Method: importPcd
        # Description: This method imports a point cloud data from a .pcd file.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        pass

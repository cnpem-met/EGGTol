"""
# Module: PointsListMenu.py
# Description: This module contains the Points List Side Widget Menu UI for displaying
a list of generated or loaded point cloud and their properties.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QTreeView, QMenu
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

# Local Imports:
from Actions.ActionList import deletePointAction

class pointsListMenu(QTreeView):
    """
    # Class: pointsListMenu
    # Description: This class provides a side menu Tree View of each IGES face entity.
    Each face contains a finite number of generated cloud points, which will also be
    displayed in the side widget.
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
        # Description: This method initializes the User Interface Elements of the Points
        List Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        # Defining some properties for the treeView:
        self.setAnimated(True)
        self.setHeaderHidden(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda position : self.openMenu(position, parent))
        self.model = QStandardItemModel()
        self.model.appendRow(QStandardItem(''))
        self.model.appendRow(QStandardItem('To delete a point or a group of points,'))
        self.model.appendRow(QStandardItem('right-click on the corresponding group'))
        self.model.appendRow(QStandardItem('and select DELETE.'))
        self.model.appendRow(QStandardItem(''))
        self.model.appendRow(QStandardItem('ALL POINTS'))
        self.model.appendRow(QStandardItem(''))
        self.addItems(self.model, parent.pointsList)
        self.setModel(self.model)

    def addItems(self, parent, elements):
        """
        # Method: addItems.
        # Description: This method adds the entries on the TreeView side widget using the
        parent.pointsList property of the main window.
        # Parameters: * MainWindow parent = A reference for the main window object.
                      * List elements = A list of tuples. Each tuple represents an entity, and
                      has another list of elements inside it representing each IGES property.
        """
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

    def openMenu(self, position, parent):
        """
        # Method: openMenu.
        # Description: This method creates a context menu for handling the erasing process of
        a selected point or a group of points.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """
        # Checking the current level of the selected line on the list of points:
        indexes = self.selectedIndexes()
        currentLevel = 0
        if len(indexes) > 0:
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                currentLevel += 1

        # Gathering information about the current selected point or face on the list:
        if(currentLevel == 0):
            currentInnerIndex = None
            currentOuterIndex = self.currentIndex().row()
        if(currentLevel == 1):
            currentInnerIndex = self.currentIndex().row()
            currentOuterIndex = self.currentIndex().parent().row()

        # Generating the menu object and the corresponding action for deleting the points:
        menu = QMenu()
        action = deletePointAction(parent, currentLevel, currentInnerIndex, currentOuterIndex)
        menu.addAction(action)
        menu.exec_(self.viewport().mapToGlobal(position))

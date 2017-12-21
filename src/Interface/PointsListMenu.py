"""
# Module: PointsListMenu.py
# Description: This module contains the Points List Side Widget Menu UI for displaying
a list of generated or loaded point cloud and their properties.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QCoreApplication, QSize, Qt

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
        self.setHeaderHidden(True)
        self.model = QStandardItemModel()
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

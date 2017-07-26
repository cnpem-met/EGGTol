"""
# Module: EntitiesMenu.py
# Description: This module contains the Entities Side Widget Menu UI for displaying
a list of loaded IGES entities and their properties.
# Author: Willian Hideak Arita da Silva.
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QCoreApplication, QSize, Qt

class entitiesMenu(QTreeView):
    """
    # Class: entitiesMenu
    # Description: This class provides a side menu Tree View of each IGES entity.
    Each entity can be selected for individual discretization / individual options.
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
        # Description: This method initializes the User Interface Elements of the Entities
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        self.setHeaderHidden(True)
        self.model = QStandardItemModel()
        self.addItems(self.model, parent.entitiesList)
        self.setModel(self.model)

    def addItems(self, parent, elements):
        """
        # Method: addItems.
        # Description: This method adds the entities on the TreeView side widget using the
        parent.entitiesList property of the main window.
        # Parameters: * MainWindow parent = A reference for the main window object.
                      * List elements = A list of tuples. Each tuple represents an entity, and
                      has another list of elements inside it representing each IGES property.
        """

        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

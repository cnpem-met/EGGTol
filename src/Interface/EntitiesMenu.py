# Module: EntitiesMenu.py
# Description: This module contains the Entities Side Widget Menu UI
# for displaying a list of loaded IGES entities and their properties.

# Author: Willian Hideak Arita da Silva.
# Last edit: May, 04, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QCoreApplication, QSize, Qt

# Class: entitiesMenu
# Description: This class provides a side menu a Tree View of each IGES entity.
# Each entity can be selected for individual discretization / individual options.

class entitiesMenu(QTreeView):
    
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        self.setHeaderHidden(True)
        self.model = QStandardItemModel()
        self.addItems(self.model, parent.entitiesList)
        self.setModel(self.model)
        
    def addItems(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text)
            parent.appendRow(item)
            if children:
                self.addItems(item, children)

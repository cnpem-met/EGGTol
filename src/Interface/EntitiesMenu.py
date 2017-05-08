# Module: EntitiesMenu.py
# Description: This module contains the Entities Side Widget Menu UI
# for displaying a list of loaded IGES entities and their properties.

# Author: Willian Hideak Arita da Silva.
# Last edit: May, 04, 2017.

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView, QStandardItemModel
from PyQt5.QtCore import QCoreApplication, QSize

# Class: entitiesMenu
# Description: This class provides a side menu a Tree View of each IGES entity.
# Each entity can be selected for individual discretization / individual options.

'''
ATTENTION!
DATA FOR TESTING PURPOSES!
'''
data = [
    ("Alice", [
        ("Keys", []),
        ("Purse", [
            ("Cellphone", [])
            ])
        ]),
    ("Bob", [
        ("Wallet", [
            ("Credit card", []),
            ("Money", [])
            ])
        ])
    ]

class entitiesMenu(QWidget):
    
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        '''
        TODO
        A UI INTERFACE NEEDS TO BE IMPLEMENTED HERE
        '''
        self.treeView = QTreeView()
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.openMenu)

        self.model = QStandardItemModel()
        self.addItems(self.model, data)
        self.treeView.setModel(self.model)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wn = closeWindow()
    sys.exit(app.exec_())
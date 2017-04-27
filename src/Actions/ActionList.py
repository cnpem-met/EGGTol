# Module: ActionList.py
# Description: This module contains all possible actions that can be performed
# in the program. These actions has internal functions that can be called by
# the main.py.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

class welcomeAction(QAction):
    
    def __init__(self, parent):
        super().__init__(QIcon("..\\icons\\desktopIcons\\main.png"), 'welcomeAction', parent)
        self.setStatusTip('Exibe o menu de boas vindas, incluindo o changelog.txt')
        self.setIconText('Bem-Vindo!')
        

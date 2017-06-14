# Module: WelcomeMenu.py
# Description: This module contains the Welcome Menu DockWidget.

# Author: Willian Hideak Arita da Silva.
# Last edit: June, 08, 2017.

import sys
from PyQt5.QtWidgets import QTextEdit

# Class: welcomeMenu
# Description: This class provides welcome information, tips and the changelog.
class welcomeMenu(QTextEdit):

    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)

    def initUI(self, parent):
        welcomeTextFile = open('..\\src\\Interface\\welcome.txt', 'r')
        with welcomeTextFile:
            text = welcomeTextFile.read()
            self.setText(text)

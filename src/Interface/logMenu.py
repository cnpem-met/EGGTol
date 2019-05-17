"""
# Module: WelcomeMenu.py
# Description: This module contains the Welcome Menu DockWidget.
# Author: Willian Hideak Arita da Silva.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QTextEdit, QWidget, QGridLayout, QLabel, QFileDialog, QToolButton

# Local Imports:
from Resources.Strings import MyStrings

class logMenu(QWidget):
    """
    # Class: welcomeMenu.
    # Description: This class provides welcome information, tips and the changelog.
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
        # Description: This method initializes the User Interface Elements of the Welcome
        Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel("All actions, including discretization\nand deviation, showed here.", self)
        grid.addWidget(label1, 0, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText("Save Log")
        grid.addWidget(btn1, 1, 0)
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(70)
        btn1.clicked.connect(lambda: self.saveLog(parent))

        btn2 = QToolButton()
        btn2.setText("Load Log")
        grid.addWidget(btn2, 1, 1)
        btn2.setMinimumHeight(30)
        btn2.setMinimumWidth(70)
        btn2.setEnabled(False)
        # btn2.clicked.connect(lambda: self.loadLog(parent))

        log = QTextEdit()
        log.setMinimumHeight(50)
        grid.addWidget(log, 2, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        #grid.setRowStretch(3, 1)

        # Prints logbookList, tupple in which all the actions were recorded in string form
        logText = ''
        for i in parent.logbookList:
            logText += i
        log.setText(logText)
        log.setReadOnly(True)

    def saveLog(self, parent):
        defaultName = (parent.lastPath).split('.')[0:-1]
        defaultName = '.'.join(defaultName)
        defaultName = defaultName + '.txt'
        fileName = QFileDialog.getSaveFileName(parent, "Save log in .txt format", defaultName, MyStrings.exportTxtFormat)[0]
        if not fileName:
            return
        self.generateLogTxt(parent.logbookList, fileName)

    def generateLogTxt(self, logList, filePath):
        logText = ''
        for i in logList:
            logText += i
        fileName = open(filePath, 'w')
        fileName.write(logText)
        fileName.close()

    def loadLog(self, parent):
        # Invoking a file dialog for loading the current state of the point cloud:
        fileName = QFileDialog.getOpenFileName(parent, 'Load and apply actions from a saved log file', parent.lastPath,
                                               'Text file (*.txt)')[0]

        # Checking if the provided filename is valid:
        if not fileName:
            return

        # Opening a file to save the current project:
        file = open(fileName, 'r')

        line = file.readline()
        while line:
            if line[0:27] == '> [Discretization] Automatic':
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

"""
# Module: logMenu.py
# Description: This module contains the log book side widget menu UI to
               visualize and import actions of/for the current session's model
# Author: Rodrigo de Oliveira Neto.
"""

# PyQt5 Imports:
from PyQt5.QtWidgets import QTextEdit, QWidget, QGridLayout, QLabel, QFileDialog, QToolButton, QMessageBox

# Local Imports:
from Resources.Strings import MyStrings

class logMenu(QWidget):
    """
    # Class: logMenu.
    # Description: This class implements functions associated with the logbook panel
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
        # Description: This method initializes the User Interface Elements of the Log Menu side widget.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        grid = QGridLayout()
        self.setLayout(grid)

        label1 = QLabel(MyStrings.logDescription, self)
        grid.addWidget(label1, 0, 0, 1, 2)

        btn1 = QToolButton()
        btn1.setText(MyStrings.logSave)
        grid.addWidget(btn1, 1, 0)
        btn1.setMinimumHeight(30)
        btn1.setMinimumWidth(70)
        btn1.clicked.connect(lambda: self.saveLog(parent))

        btn2 = QToolButton()
        btn2.setText(MyStrings.logLoad)
        grid.addWidget(btn2, 1, 1)
        btn2.setMinimumHeight(30)
        btn2.setMinimumWidth(70)
        btn2.clicked.connect(lambda: self.loadLog(parent))

        log = QTextEdit()
        log.setMinimumHeight(50)
        log.setMinimumWidth(250)
        grid.addWidget(log, 2, 0, 1, 2)

        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        #grid.setRowStretch(3, 1)

        logText = ''
        for i in parent.logbookList:
            logText += i
        log.setText(logText)
        log.setReadOnly(True)

    def saveLog(self, parent):
        """
        # Method: saveLog.
        # Description: This method saves information about the current session's actions.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        defaultName = (parent.lastPath).split('.')[0:-1]
        defaultName = '.'.join(defaultName)
        defaultName = defaultName + '.txt'
        fileName = QFileDialog.getSaveFileName(parent, MyStrings.logSaveMsg, defaultName, MyStrings.exportTxtFormat)[0]
        if not fileName:
            return
        self.generateLogTxt(parent.logbookList, fileName)

    def generateLogTxt(self, logList, filePath):
        """
        # Method: generateLogTxt.
        # Description: This complementary method writes the log information in a .txt file.
        # Parameters: * String logList = A text containing the log informations.
                      * String filePath = A reference for the selectec file path.
        """

        logText = ''
        for i in logList:
            logText += i
        fileName = open(filePath, 'w')
        fileName.write(logText)
        fileName.close()

    def loadLog(self, parent):
        """
        # Method: loadLog.
        # Description: This method loads actions information from a external .txt file
                       and apply then into the current session's model.
        # Parameters: * MainWindow parent = A reference for the main window object.
        """

        if not parent.activeCADFile:
            QMessageBox.information(parent, MyStrings.popupNoIgesFileTitle,
                                    MyStrings.popupNoIgesFileDescription,
                                    QMessageBox.Ok, QMessageBox.Ok)
            return

        # Invoking a file dialog for loading the current state of the point cloud
        fileName = QFileDialog.getOpenFileName(parent, MyStrings.logLoadMsg, parent.lastPath,
                                               'Text file (*.txt)')[0]

        # Checking if the provided filename is valid
        if not fileName:
            return

        # Opening the file that contains the log to be loaded
        file = open(fileName, 'r')

        line = file.readline()
        # Iterative process that reads each line of the file and internally calls the associated functions
        while line:
            if line == '> [Discretization] Automatic:\n':
                mode = file.readline()[7:-1]
                N = float(file.readline()[10:-1])
                precision = float(file.readline()[12:-1])
                try:
                    U = float(file.readline()[10:-1])
                    V = float(file.readline()[10:-1])
                except:
                    U, V = None, None
                paramList = [mode, N, precision, U, V]

                from Interface.AutoDiscretizeMenu import autoDiscretizeMenu
                autoDiscretizeCall = autoDiscretizeMenu(parent)
                autoDiscretizeCall.autoDiscretize(parent, True, paramList)

            elif line == '> [Discretization] Flat:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                mode = file.readline()[7:-1]
                N = float(file.readline()[10:-1])
                precision = float(file.readline()[12:-1])
                paramList = [entList, mode, N, precision]

                from Interface.FaceDiscretizeMenu import faceDiscretizeMenu
                faceDiscretizeCall = faceDiscretizeMenu(parent)
                faceDiscretizeCall.faceDiscretize(parent, True, paramList)
            elif line == '> [Discretization] Parametric:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                U = float(file.readline()[10:-1])
                V = float(file.readline()[10:-1])
                paramList = [entList, U, V]

                from Interface.SurfaceDiscretizeMenu import surfaceDiscretizeMenu
                surfaceDiscretizeCall = surfaceDiscretizeMenu(parent)
                surfaceDiscretizeCall.surfaceDiscretize(parent, True, paramList)
            elif line == '> [Deviation] Translational:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                X = file.readline()[10:-1]
                Y = file.readline()[10:-1]
                Z = file.readline()[10:-1]
                offset = float(file.readline()[9:-4])
                paramList = [entList, X, Y, Z, offset]

                from Interface.TranslationDefectsMenu import translationDefectsMenu
                translationDefectsCall = translationDefectsMenu(parent)
                translationDefectsCall.translatePoints(parent, True, paramList)
            elif line == '> [Deviation] Rotation:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                xAng = float(file.readline()[10:-2])
                yAng = float(file.readline()[10:-2])
                zAng = float(file.readline()[10:-2])
                paramList = [entList, xAng, yAng, zAng]

                from Interface.RotationalDefectsMenu import rotationalDefectsMenu
                rotationalDefectsCall = rotationalDefectsMenu(parent)
                rotationalDefectsCall.rotatePoints(parent, True, paramList)
            elif line == '> [Deviation] Random:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                minOffset = float(file.readline()[14:-4])
                maxOffset = float(file.readline()[14:-4])
                paramList = [entList, minOffset, maxOffset]

                from Interface.RandomDefectsMenu import randomDefectsMenu
                randomDefectsCall = randomDefectsMenu(parent)
                randomDefectsCall.randomPoints(parent, True, paramList)
            elif line == '> [Deviation] Flexion:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                longAxis = file.readline()[13:-1]
                perpAxis = file.readline()[13:-1]
                maxDef = float(file.readline()[18:-4])
                paramList = [entList, longAxis, perpAxis, maxDef]

                from Interface.FlexionDefectsMenu import flexionDefectsMenu
                flexionDefectsCall = flexionDefectsMenu(parent)
                flexionDefectsCall.flexionPoints(parent, True, paramList)
            elif line == '> [Deviation] Periodic Pattern:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                drillAxis = file.readline()[19:-1]
                drillAxis = self.str2bool(drillAxis)
                amp = float(file.readline()[12:-4])
                freq = float(file.readline()[12:-1])
                paramList = [entList, drillAxis, amp, freq]
                from Interface.WaveDefectsMenu import waveDefectsMenu
                waveDefectsCall = waveDefectsMenu(parent)
                waveDefectsCall.wavePoints(parent, True, paramList)
            elif line == '> [Deviation] Ovalization:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                maxDef = float(file.readline()[14:-4])
                paramList = [entList, maxDef]

                from Interface.OvalDefectsMenu import ovalDefectsMenu
                ovalDefectsCall = ovalDefectsMenu(parent)
                ovalDefectsCall.ovalPoints(parent, True, paramList)
            elif line == '> [Deviation] Torsion:\n':
                entList = file.readline()[15:-2]
                entList = entList.split(',')
                entList = [float(element) for element in entList]
                longAxis = file.readline()[13:-1]
                perpAxis = file.readline()[13:-1]
                maxDef = float(file.readline()[18:-4])
                paramList = [entList, longAxis, perpAxis, maxDef]

                from Interface.TorsionDefectsMenu import torsionDefectsMenu
                torsionDefectsCall = torsionDefectsMenu(parent)
                torsionDefectsCall.torsionPoints(parent, True, paramList)
            line = file.readline()

    def str2bool(self, v):
        """
        # Method: str2bool.
        # Description: This method converts a string variable to a bool.
        # Parameters: * String v = The variable to be converted.
        """

        return v.lower() in ('True', 'true')

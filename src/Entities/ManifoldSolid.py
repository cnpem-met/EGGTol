"""
# Module: ManifoldSolid.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class ManifoldSolid(Entity):
    """
    # Class: ManifoldSolid
    # Description: This class contains data from the Manifold Solid entity.
    """

    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 SHELL, SOF, N, VOIDList, VOFList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str SHELL = Pointer to Shell.
                      * Str SOF = Orientation Flag.
                      * Str N = Number of void Shells.
                      * List VOIDList = List of pointers to the void Shells.
                      * List VOFList = List of orientations of the void Shells.
        """

        super().__init__(186, PDPointer, parCount, seqNumber)
        self.SHELL = SHELL
        self.SOF = SOF
        self.N = N
        self.VOIDList = VOIDList
        self.VOFList = VOFList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('(' + str(int(self.seqNumber)//2+1) + ') Manifold Solid (IGES 186)', [])
        out[1].append(('- Pointer to Shell (SHELL): ' + str(self.SHELL), []))
        out[1].append(('- Orientation Flag (SOF): ' + str(self.SOF), []))
        out[1].append(('- Number of Void Shells (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('- Pointer to Void Shell (VOID(' + str(i+1) + ')): ' + str(self.VOIDList[i]), []))
            out[1].append(('- Orientation Flag of Void Shell (VOF(' + str(i+1) + ')): ' + str(self.VOFList[i]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Manifold Solid B-Rep Object (Type 186)\n'
        out += '* Pointer to Shell (SHELL): ' + str(self.SHELL) + '\n'
        out += '* Orientation Flag (SOF): ' + str(self.SOF) + '\n'
        out += '* Number of Void Shells (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Pointer to Void Shell (VOID(' + str(i+1) + ')): ' + str(self.VOIDList[i]) + '\n'
            out += '* Orientation Flag of Void Shell (VOF(' + str(i+1) + ')): ' + str(self.VOFList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

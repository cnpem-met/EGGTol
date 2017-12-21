"""
# Module: Shell.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class Shell(Entity):
    """
    # Class: Shell.
    # Description: This class contains data from Shell entities.
    """

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber,
                 N, FACEList, OFList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str N = Number of faces.
                      * List FACEList = List of pointers to Faces.
                      * List OFList = List of orientation flags.
        """

        super().__init__(514, PDPointer, parCount, seqNumber)
        self.N = N
        self.FACEList = FACEList
        self.OFList = OFList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('(' + str(int(self.seqNumber)//2+1) + ') Casco Sólido (IGES 514)', [])
        out[1].append(('- Number of Faces (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('- Pointer to Face (FACE(' + str(i+1) + ')): ' + str(self.FACEList[i]), []))
            out[1].append(('- Orientation Flag (OF(' + str(i+1) + ')): ' + str(self.OFList[i]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Shell (Type 514)\n'
        out += '* Number of Faces (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Pointer to Face (FACE(' + str(i+1) + ')): ' + str(self.FACEList[i]) + '\n'
            out += '* Orientation Flag (OF(' + str(i+1) + ')): ' + str(self.OFList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

"""
# Module: Face.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class Face(Entity):
    """
    # Class: Face.
    # Description: This class represents data from Face entities.
    """

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 SURF, N, OF, LOOPList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str SURF = Underlying surface pointer.
                      * Str N = Number of loops.
                      * Str OF = Outer Loop flag.
                      * List LOOPList = List of pointers to the Loops.
        """

        super().__init__(510, PDPointer, parCount, seqNumber)
        self.SURF = SURF
        self.N = N
        self.OF = OF
        self.LOOPList = LOOPList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('#' + str(int(self.seqNumber)//2+1) + ' Face (IGES 510)', [])
        out[1].append(('* Underlying Surface (SURF): ' + str(self.SURF), []))
        out[1].append(('* Number of Loops (N): ' + str(self.N), []))
        out[1].append(('* Outer Loop Flag (OF): ' + str(self.OF), []))
        for i in range(int(self.N)):
            out[1].append(('* Pointer to the Loops (LOOP(' + str(i+1) + ')): ' + str(self.LOOPList[i]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Face (Type 510)\n'
        out += '* Underlying Surface (SURF): ' + str(self.SURF) + '\n'
        out += '* Number of Loops (N): ' + str(self.N) + '\n'
        out += '* Outer Loop Flag (OF): ' + str(self.OF) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Pointer to the Loops (LOOP(' + str(i+1) + ')): ' + str(self.LOOPList[i]) + '\n'
        out += '* -----------------------------------\n'
        return out

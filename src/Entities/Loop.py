"""
# Module: Loop.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class Loop(Entity):
    """
    # Class: Loop.
    # Description: This class represents data from Loop entities.
    """

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, TYPEList, EDGEList, NDXList, OFList, KList, ISOPList, CURVList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str N = Number of edge tuples.
                      * List TYPEList = List of Edge Types (0=Edge and 1=Vertex).
                      * List EDGEList = List of pointers to Edge of Vertex List.
                      * List NDXList = List of indexes of the Edge or Vertex.
                      * List OFList = List of orientation flags.
                      * List KList = List of numbers of underlying Space Curves.
                      * List ISOPList = List of isoparametric flags.
                      * List CURVList = List of pointers to Space Curves.
        """

        super().__init__(508, PDPointer, parCount, seqNumber)
        self.N = N
        self.TYPEList = TYPEList
        self.EDGEList = EDGEList
        self.NDXList = NDXList
        self.OFList = OFList
        self.KList = KList
        self.ISOPList = ISOPList
        self.CURVList = CURVList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('(' + str(int(self.seqNumber)//2+1) + ') Boundary Loop (IGES 508)', [])
        out[1].append(('- Number of Edge Tuples (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('- Edge or Vertex? (TYPE(' + str(i+1) + ')): ' + str(self.TYPEList[i]), []))
            out[1].append(('- Pointer to Edge/Vertex List (EDGE(' + str(i+1) + ')): ' + str(self.EDGEList[i]), []))
            out[1].append(('- Index of the Edge/Vertex (NDX(' + str(i+1) + ')): ' + str(self.NDXList[i]), []))
            out[1].append(('- Orientation Flag of First Edge (OF(' + str(i+1) + ')): ' + str(self.OFList[i]), []))
            out[1].append(('- Number of Under. Space Curves (K(' + str(i+1) + ')): ' + str(self.KList[i]), []))
            for j in range(int(self.KList[i])):
                out[1].append(('- Isoparametric Flag (ISOP(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.ISOPList[i][j]), []))
                out[1].append(('- Pointer to Space Curve (CURV(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.CURVList[i][j]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Loop (Type 508)\n'
        out += '* Number of Edge Tuples (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Edge or Vertex? (TYPE(' + str(i+1) + ')): ' + str(self.TYPEList[i]) + '\n'
            out += '* Pointer to Edge/Vertex List (EDGE(' + str(i+1) + ')): ' + str(self.EDGEList[i]) + '\n'
            out += '* Index of the Edge/Vertex (NDX(' + str(i+1) + ')): ' + str(self.NDXList[i]) + '\n'
            out += '* Orientation Flag of First Edge (OF(' + str(i+1) + ')): ' + str(self.OFList[i]) + '\n'
            out += '* Number of Under. Space Curves (K(' + str(i+1) + ')): ' + str(self.KList[i]) + '\n'
            for j in range(int(self.KList[i])):
                out += '* Isoparametric Flag (ISOP(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.ISOPList[i][j]) + '\n'
                out += '* Pointer to Space Curve (CURV(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.CURVList[i][j]) + '\n'
            out += '* -----------------------------------\n'
        return out

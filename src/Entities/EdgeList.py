"""
# Module: EdgeList.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class EdgeList(Entity):
    """
    # Class: EdgeList.
    # Description: This class contains data from an Edge List.
    """

    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, CURVList, SVPList, SVList, TVPList, TVList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str N = Number of edges.
                      * List CURVList = List of Space Curves.
                      * List SVPList = List of Start Vertices pointers.
                      * List SVList = List of Start Vertices indexes.
                      * List TVPList = List of Terminate Vertices pointers.
                      * List TVList = List of Terminate Vertices indexes.
        """

        super().__init__(entityType, PDPointer, parCount, seqNumber)
        self.N = N
        self.CURVList = CURVList
        self.SVPList = SVPList
        self.SVList = SVList
        self.TVPList = TVPList
        self.TVList = TVList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('#' + str(int(self.seqNumber)//2+1) + ' Edge List (IGES 504)', [])
        out[1].append(('* Number of Edges (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('* Space Curve (CURV(' + str(i+1) + ')): ' + str(self.CURVList[i]), []))
            out[1].append(('* Start Vertex List Pointer (SVP(' + str(i+1) + ')): ' + str(self.SVPList[i]), []))
            out[1].append(('* Start Vertex Index (SV(' + str(i+1) + ')): ' + str(self.SVList[i]), []))
            out[1].append(('* Terminate Vertex List Pointer (TVP(' + str(i+1) + ')): ' + str(self.TVPList[i]), []))
            out[1].append(('* Terminate Vertex Index (TV(' + str(i+1) + ')): ' + str(self.TVList[i]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Edge List (Type 504)\n'
        out += '* Number of Edges (N): ' + str(self.N) + '\n'
        out += '* ----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Space Curve (CURV(' + str(i+1) + ')): ' + str(self.CURVList[i]) + '\n'
            out += '* Start Vertex List Pointer (SVP(' + str(i+1) + ')): ' + str(self.SVPList[i]) + '\n'
            out += '* Start Vertex Index (SV(' + str(i+1) + ')): ' + str(self.SVList[i]) + '\n'
            out += '* Terminate Vertex List Pointer (TVP(' + str(i+1) + ')): ' + str(self.TVPList[i]) + '\n'
            out += '* Terminate Vertex Index (TV(' + str(i+1) + ')): ' + str(self.TVList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

"""
# Module: VertexList.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class VertexList(Entity):
    """
    # Class: VertexList.
    # Description: This class contains data from a Vertex List.
    """

    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, XList, YList, ZList):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str N = Number of vertex tuples.
                      * List XList = List of coordinates X.
                      * List YList = List of coordinates Y.
                      * List ZList = List of coordinates Z.
        """

        super().__init__(entityType, PDPointer, parCount, seqNumber)
        self.N = N
        self.XList = XList
        self.YList = YList
        self.ZList = ZList

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('(' + str(int(self.seqNumber)//2+1) + ') Vertex List (IGES 502)', [])
        out[1].append(('- Number of Vertex Tuples (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('- Coordinate X(' + str(i+1) + ')): ' + str(self.XList[i]), []))
            out[1].append(('- Coordinate Y(' + str(i+1) + ')): ' + str(self.YList[i]), []))
            out[1].append(('- Coordinate Z(' + str(i+1) + ')): ' + str(self.ZList[i]), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Vertex List (Type 502)\n'
        out += '* Number of Vertex Tuples (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Coordinate X(' + str(i+1) + ')): ' + str(self.XList[i]) + '\n'
            out += '* Coordinate Y(' + str(i+1) + ')): ' + str(self.YList[i]) + '\n'
            out += '* Coordinate Z(' + str(i+1) + ')): ' + str(self.ZList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

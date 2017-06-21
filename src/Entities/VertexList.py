# Module: VertexList.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: VertexList
# Type: 502
# Description: This class contains data from a Vertex List.

class VertexList(Entity):

    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, XList, YList, ZList):
        super().__init__(entityType, PDPointer, parCount, seqNumber)
        self.N = N
        self.XList = XList
        self.YList = YList
        self.ZList = ZList

    def description(self):
        out = ('#' + str(int(self.seqNumber)//2+1) + ' Vertex List (IGES 502)', [])
        out[1].append(('* Number of Vertex Tuples (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('* Coordinate X(' + str(i+1) + ')): ' + str(self.XList[i]), []))
            out[1].append(('* Coordinate Y(' + str(i+1) + ')): ' + str(self.YList[i]), []))
            out[1].append(('* Coordinate Z(' + str(i+1) + ')): ' + str(self.ZList[i]), []))
        return out
    
    def __str__(self):
        out = 'Vertex List (Type 502)\n'
        out += '* Number of Vertex Tuples (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Coordinate X(' + str(i+1) + ')): ' + str(self.XList[i]) + '\n'
            out += '* Coordinate Y(' + str(i+1) + ')): ' + str(self.YList[i]) + '\n'
            out += '* Coordinate Z(' + str(i+1) + ')): ' + str(self.ZList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

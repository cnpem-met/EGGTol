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

    def discretize(self):
        '''TODO'''
        pass

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

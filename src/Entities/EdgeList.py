# Module: EdgeList.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: EdgeList
# Type: 504
# Description: This class contains data from an Edge List.

class EdgeList(Entity):

    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, CURVList, SVPList, SVList, TVPList, TVList):
        super().__init__(entityType, PDPointer, parCount, seqNumber)
        self.N = N
        self.CURVList = CURVList
        self.SVPList = SVPList
        self.SVList = SVList
        self.TVPList = TVPList
        self.TVList = TVList

    def description(self):
        pass

    def __str__(self):
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

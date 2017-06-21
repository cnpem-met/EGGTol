# Module: Loop.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: Loop
# Type: 508
# Description: This class cointais data from Loop entities.

class Loop(Entity):

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 N, TYPEList, EDGEList, NDXList, OFList, KList, ISOPList, CURVList):
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
        out = ('#' + str(int(self.seqNumber)//2+1) + ' Loop (IGES 508)', [])
        out[1].append(('* Number of Edge Tuples (N): ' + str(self.N), []))
        for i in range(int(self.N)):
            out[1].append(('* Edge or Vertex? (TYPE(' + str(i+1) + ')): ' + str(self.TYPEList[i]), []))
            out[1].append(('* Pointer to Edge/Vertex List (EDGE(' + str(i+1) + ')): ' + str(self.EDGEList[i]), []))
            out[1].append(('* Index of the Edge/Vertex (NDX(' + str(i+1) + ')): ' + str(self.NDXList[i]), []))
            out[1].append(('* Orientation Flag of First Edge (OF(' + str(i+1) + ')): ' + str(self.OFList[i]), []))
            out[1].append(('* Number of Under. Space Curves (K(' + str(i+1) + ')): ' + str(self.KList[i]), []))
            for j in range(int(self.KList[i])):
                out[1].append(('* Isoparametric Flag (ISOP(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.ISOPList[i][j]), []))
                out[1].append(('* Pointer to Space Curve (CURV(' + str(i+1) + ', ' + str(j+1) + ')): ' + str(self.CURVList[i][j]), []))
        return out

    def __str__(self):
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

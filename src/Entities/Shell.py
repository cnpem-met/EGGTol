# Module: Shell.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: Shell
# Type: 514
# Description: This class cointais data from Shell entities.

class Shell(Entity):

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber,
                 N, FACEList, OFList):
        super().__init__(514, PDPointer, parCount, seqNumber)
        self.N = N
        self.FACEList = FACEList
        self.OFList = OFList

    def description(self):
        pass

    def __str__(self):
        out = 'Shell (Type 514)\n'
        out += '* Number of Faces (N): ' + str(self.N) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Pointer to Face (FACE(' + str(i+1) + ')): ' + str(self.FACEList[i]) + '\n'
            out += '* Orientation Flag (OF(' + str(i+1) + ')): ' + str(self.OFList[i]) + '\n'
            out += '* -----------------------------------\n'
        return out

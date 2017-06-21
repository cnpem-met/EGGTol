# Module: Face.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: Face
# Type: 510
# Description: This class cointais data from Face entities.

class Face(Entity):

    # Defining Properties
    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 SURF, N, OF, LOOPList):
        super().__init__(510, PDPointer, parCount, seqNumber)
        self.SURF = SURF
        self.N = N
        self.OF = OF
        self.LOOPList = LOOPList


    def description(self):
        out = ('#' + str(int(self.seqNumber)//2+1) + ' Face (IGES 510)', [])
        out[1].append(('* Underlying Surface (SURF): ' + str(self.SURF), []))
        out[1].append(('* Number of Loops (N): ' + str(self.N), []))
        out[1].append(('* Outer Loop Flag (OF): ' + str(self.OF), []))
        for i in range(int(self.N)):
            out[1].append(('* Pointer to the Loops (LOOP(' + str(i+1) + ')): ' + str(self.LOOPList[i]), []))
        return out        
    
    def __str__(self):
        out = 'Face (Type 510)\n'
        out += '* Underlying Surface (SURF): ' + str(self.SURF) + '\n'
        out += '* Number of Loops (N): ' + str(self.N) + '\n'
        out += '* Outer Loop Flag (OF): ' + str(self.OF) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.N)):
            out += '* Pointer to the Loops (LOOP(' + str(i+1) + ')): ' + str(self.LOOPList[i]) + '\n'
        out += '* -----------------------------------\n'
        return out

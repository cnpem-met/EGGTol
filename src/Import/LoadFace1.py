# Module: LoadFace.py
# Description: This module allow us to import a Face data from an .IGES
# and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

# Function to load a Face (Type 510)
def loadFace(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    SURF = RawParameterList[1]
    N = RawParameterList[2]
    OF = RawParameterList[3]
    LOOPList = []
    for i in range(1, int(N)+1):
        LOOPList.append(RawParameterList[3+i])
    loadedObject = Face(entityType, PDPointer, parCount, seqNumber, \
                        SURF, N, OF, LOOPList)
    return loadedObject

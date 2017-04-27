# Module: loadShell.py
# Description: This module allow us to import data from a Shell in an .IGES
# and .IGS file..

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

# Function to load a Shell (Type 514).
def loadShell(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    N = RawParameterList[1]
    FACEList = []
    OFList = []
    for i in range(1, int(N)+1):
        FACEList.append(RawParameterList[2*i])
        OFList.append(RawParameterList[1+2*i])
    loadedObject = Shell(entityType, PDPointer, parCount, seqNumber, \
                         N, FACEList, OFList)
    return loadedObject

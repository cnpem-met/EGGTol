# Module: LoadShell.py
# Description: This module allow us to import data from a Shell in an .IGES
# and .IGS file..

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from Entities.Shell import Shell

# Function to load a Shell (Type 514).
def loadShell(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    N = RawParameterList[1]
    FACEList = []
    OFList = []
    for i in range(1, int(N)+1):
        FACEList.append(RawParameterList[2*i])
        OFList.append(RawParameterList[1+2*i])
    loadedObject = Shell(entityType, PDPointer, parCount, seqNumber, \
                         N, FACEList, OFList)
    return loadedObject

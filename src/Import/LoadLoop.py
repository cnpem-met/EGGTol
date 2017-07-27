"""
# Module: LoadLoop.py
# Description: This module allow us to import a Loop data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Loop import Loop

# Function to load a Loop (Type 508)
def loadLoop(RawDataList, RawParameterList):
    """
    # Function: loadLoop.
    # Description: Creates a Loop Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """

    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    N = RawParameterList[1]
    TYPEList = []
    EDGEList = []
    NDXList = []
    OFList = []
    KList = []
    ISOPList = []
    CURVList = []
    i = 2
    for j in range(int(N)):
        TYPEList.append(RawParameterList[i]); i += 1
        EDGEList.append(RawParameterList[i]); i += 1
        NDXList.append(RawParameterList[i]); i += 1
        OFList.append(RawParameterList[i]); i += 1
        KList.append(RawParameterList[i]); i += 1
        ISOPList.append([])
        CURVList.append([])
        for k in range(int(KList[j])):
            ISOPList[j].append(RawParameterList[i]); i += 1
            CURVList[j].append(RawParameterList[i]); i += 1
    loadedObject = Loop(entityType, PDPointer, parCount, seqNumber, \
                        N, TYPEList, EDGEList, NDXList, OFList, KList, ISOPList, CURVList)
    return loadedObject

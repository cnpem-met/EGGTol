# Module: LoadLoop.py
# Description: This module allow us to import a Loop data from an .IGES
# and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

# Function to load a Loop (Type 508)
def loadLoop(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
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

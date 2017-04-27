# Module: LoadVertexList.py
# Description: This module allow us to import a VertexList data from an
# .IGES and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

# Function to load a Vertex List (Type 502)
def loadVertexList(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    N = RawParameterList[1]
    XList = []
    YList = []
    ZList = []
    for i in range(1, int(N)+1):
        XList.append(RawParameterList[-1+3*i])
        YList.append(RawParameterList[3*i])
        ZList.append(RawParameterList[1+3*i])
    loadedObject = VertexList(entityType, PDPointer, parCount, seqNumber, \
                              N, XList, YList, ZList)
    return loadedObject

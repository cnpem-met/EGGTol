# Module: LoadEdgeList.py
# Description: This module allow us to import an EdgeList data from an .IGES
# and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from Entities.EdgeList import EdgeList

# Function to load a Edge List (Type 504)
def loadEdgeList(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    N = RawParameterList[1]
    CURVList = []
    SVPList = []
    SVList = []
    TVPList = []
    TVList = []
    for i in range(1, int(N)+1):
        CURVList.append(RawParameterList[-3+5*i])
        SVPList.append(RawParameterList[-2+5*i])
        SVList.append(RawParameterList[-1+5*i])
        TVPList.append(RawParameterList[5*i])
        TVList.append(RawParameterList[1+5*i])
    loadedObject = EdgeList(entityType, PDPointer, parCount, seqNumber, \
                            N, CURVList, SVPList, SVList, TVPList, TVList)
    return loadedObject

"""
# Module: LoadEdgeList.py
# Description: This module allow us to import an EdgeList data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.EdgeList import EdgeList

# Function to load a Edge List (Type 504)
def loadEdgeList(RawDataList, RawParameterList):
    """
    # Function: loadEdgeList.
    # Description: Creates an EdgeList Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """

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

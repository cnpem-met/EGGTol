"""
# Module: LoadVertexList.py
# Description: This module allow us to import a VertexList data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.VertexList import VertexList

# Function to load a Vertex List (Type 502)
def loadVertexList(RawDataList, RawParameterList):
    """
    # Function: loadVertexList.
    # Description: Creates a VertexList Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """
    
    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
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

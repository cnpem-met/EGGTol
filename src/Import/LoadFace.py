"""
# Module: LoadFace.py
# Description: This module allow us to import a Face data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Face import Face

# Function to load a Face (Type 510)
def loadFace(RawDataList, RawParameterList):
    """
    # Function: loadFace.
    # Description: Creates a Face Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """

    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    SURF = RawParameterList[1]
    N = RawParameterList[2]
    OF = RawParameterList[3]
    LOOPList = []
    for i in range(1, int(N)+1):
        LOOPList.append(RawParameterList[3+i])
    loadedObject = Face(entityType, PDPointer, parCount, seqNumber, \
                        SURF, N, OF, LOOPList)
    return loadedObject

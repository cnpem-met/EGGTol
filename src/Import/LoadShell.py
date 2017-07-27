"""
# Module: LoadShell.py
# Description: This module allow us to import a Shell data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Shell import Shell

# Function to load a Shell (Type 514).
def loadShell(RawDataList, RawParameterList):
    """
    # Function: loadShell.
    # Description: Creates a Shell Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """

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

"""
# Module: LoadManifoldSolid.py
# Description: This module allow us to import a Manifold Solid data from .IGES or .IGS file.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.ManifoldSolid import ManifoldSolid

# Function to load a Manifold B-Rep Object (Type 186).
def loadManifoldSolid(RawDataList, RawParameterList):
    """
    # Function: loadManifoldSolid.
    # Description: Creates a ManifoldSolid Entity object given a RawDataList and a RawParameterList.
    # Parameters: * List RawDataList = A list of strings, each string being an entry in the
                  Data Section of the IGES file.
                  * List RawParameterList = A list of strings, each string being an entry in the
                  Parameter Section of the IGES file.
    # Returns: * Entity loadedObject = The corresponding Entity object.
    """

    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    SHELL = RawParameterList[1]
    SOF = RawParameterList[2]
    N = RawParameterList[3]
    VOIDList = []
    VOFList = []
    for i in range(1, int(N)+1):
        VOIDList.append(RawParameterList[2+2*i])
        VOFList.append(RawParameterList[3+2*i])
    loadedObject = ManifoldSolid(entityType, PDPointer, parCount, seqNumber, \
                                 SHELL, SOF, N, VOIDList, VOFList)
    return loadedObject

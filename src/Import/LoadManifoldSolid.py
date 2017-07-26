# Module: LoadManifoldSolid.py
# Description: This module allow us to import a Manifold Solid data from
# an .IGES and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from Entities.ManifoldSolid import ManifoldSolid

# Function to load a Manifold B-Rep Object (Type 186).
def loadManifoldSolid(RawDataList, RawParameterList):
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

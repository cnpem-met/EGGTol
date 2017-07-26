# Module: LoadRationalBSplineSurface.py
# Description: This module allow us to import a RationalBSplineSurface data
# from an .IGES and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

from Entities.RationalBSplineSurface import RationalBSplineSurface

# Function to load a Rational B-Spline Surface (Type 128)
def loadRationalBSplineSurface(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = \
    RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3]
    K1 = RawParameterList[1]
    K2 = RawParameterList[2]
    M1 = RawParameterList[3]
    M2 = RawParameterList[4]
    PROP1 = RawParameterList[5]
    PROP2 = RawParameterList[6]
    PROP3 = RawParameterList[7]
    PROP4 = RawParameterList[8]
    PROP5 = RawParameterList[9]
    SList = []
    TList = []
    WList = []
    XList = []
    YList = []
    ZList = []
    i = 10
    for j in range(int(K1)+int(M1)+2):
        SList.append(RawParameterList[i]); i += 1
    for k in range(int(K2)+int(M2)+2):
        TList.append(RawParameterList[i]); i += 1
    for w in range(int(K1)+1):
        WList.append([])
    for z in range(int(K2)+1):
        for x in range(int(K1)+1):
            WList[x].append(RawParameterList[i]); i += 1
    for a in range(int(K1)+1):
        XList.append([])
        YList.append([])
        ZList.append([])
    for b in range(int(K2)+1):
        for c in range(int(K1)+1):
            XList[c].append(RawParameterList[i]); i += 1
            YList[c].append(RawParameterList[i]); i += 1
            ZList[c].append(RawParameterList[i]); i += 1
    U0 = RawParameterList[i]; i += 1
    U1 = RawParameterList[i]; i += 1
    V0 = RawParameterList[i]; i += 1
    V1 = RawParameterList[i]; i += 1
    loadedObject = RationalBSplineSurface(entityType, PDPointer, parCount, seqNumber, \
                                          K1, K2, M1, M2, PROP1, PROP2, PROP3, PROP4, PROP5, \
                                          SList, TList, WList, XList, YList, ZList, \
                                          U0, U1, V0, V1)
    return loadedObject

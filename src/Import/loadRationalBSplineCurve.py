# Module: loadRationalBSplineCurve.py
# Description: This module allow us to import a RationalBSplineCurve data
# from an .IGES and .IGS file.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

# Function to load a Rational B-Spline Curve (Type 126)
def loadRationalBSplineCurve(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    K = RawParameterList[1]
    M = RawParameterList[2]
    PROP1 = RawParameterList[3]
    PROP2 = RawParameterList[4]
    PROP3 = RawParameterList[5]
    PROP4 = RawParameterList[6]
    TList = []
    WList = []
    XList = []
    YList = []
    ZList = []
    i = 7
    for j in range(int(K)+int(M)+2):
        TList.append(RawParameterList[i]); i += 1
    for k in range(int(K)+1):
        WList.append(RawParameterList[i]); i += 1
    for w in range(int(K)+1):
        XList.append(RawParameterList[i]); i += 1
        YList.append(RawParameterList[i]); i += 1
        ZList.append(RawParameterList[i]); i += 1
    V0 = RawParameterList[i]; i += 1
    V1 = RawParameterList[i]; i += 1
    XNORM = RawParameterList[i]; i += 1
    YNORM = RawParameterList[i]; i += 1
    ZNORM = RawParameterList[i]; i += 1
    loadedObject = RationalBSplineCurve(entityType, PDPointer, parCount, seqNumber, \
                                        K, M, PROP1, PROP2, PROP3, PROP4, TList, WList, XList, \
                                        YList, ZList, V0, V1, XNORM, YNORM, ZNORM)
    return loadedObject

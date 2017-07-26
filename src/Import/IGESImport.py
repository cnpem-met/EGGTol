"""
# Module: IGESImport.py
# Description: This module allow us to import data from an .IGES and .IGS
file, such as geometrical entities.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.EdgeList import EdgeList
from Entities.Face import Face
from Entities.Loop import Loop
from Entities.ManifoldSolid import ManifoldSolid
from Entities.RationalBSplineCurve import RationalBSplineCurve
from Entities.RationalBSplineSurface import RationalBSplineSurface
from Entities.Shell import Shell
from Entities.VertexList import VertexList

def convertData(data):
    """
    # Function: convertData.
    # Description: Function to convert an IGES parameter (as specified in IGES Specification
    version 6) to a Python string, float or int data type. Also change the exponetial character
    from 'D' to 'e', for conversion purposes.
    # Parameters: * Str data = String representing the IGES parameter.
    # Returns: * Int, Float, Str data = The same data, after the parsing.
    """

    if(('.' in data) or ('D' in data)):
        data = data.replace('D', 'e')
        try:
            data = float(data)
            return data
        except ValueError:
            data = data.replace('e', 'D')
            return data
    else:
        try:
            data = int(data)
            return data
        except ValueError:
            return data

def loadIGESFile(IGESPath):
    """
    # Function: loadIGESFile.
    # Description: This function loads an .IGS or .IGES file.
    # Parameters: * Str IGESPath = The path to the IGES file.
    # Returns: * _io.TextIOWrapper IGESFile = The Python object for the IGES file.
    """

    IGESFile = open(IGESPath, mode='r')
    return IGESFile

def getRawHeader(IGESFile):
    """
    # Function: getRawHeader.
    # Description: Function to retrieve the data of the Header Section of an IGES file.
    # Parameters: * _io.TextIOWrapper IGESFile = The Python object for the IGES file.
    # Returns: * Str header = A string containing the information of the Header Section.
    """

    IGESFile.seek(3)
    header = []
    for line in IGESFile:
        if line[72] == 'G':
            header.append(line)
    return header

def getRawData(IGESFile):
    """
    # Function: getRawData.
    # Description: Function to retrieve the data of the Data Entry Section of an IGES file.
    # Parameters: * _io.TextIOWrapper IGESFile = The Python object for the IGES file.
    # Returns: * List data = A list of strings containing each entry of the Data Section.
    """

    IGESFile.seek(3)
    data = []
    while True:
        firstRead = IGESFile.readline()
        if not firstRead:
            break
        elif firstRead[72] == 'D':
            secondRead = IGESFile.readline()
            data.append(firstRead+secondRead)
    return data

def getRawParameters(IGESFile):
    """
    # Function: getRawParameters.
    # Description: Function to retrieve the data of the Parameter Data Section of an IGES file.
    # Parameters: * _io.TextIOWrapper IGESFile = The Python object for the IGES file.
    # Returns: * List parameters = A list of strings containing each entry of the Parameter
    Section.
    """

    IGESFile.seek(3)
    parameters = []
    lastSeqNumber = None
    while True:
        firstRead = IGESFile.readline()
        if not firstRead:
            break
        elif firstRead[72] == 'P':
            if int(firstRead[64:72]) == lastSeqNumber:
                parameters[len(parameters)-1] += firstRead
            else:
                parameters.append(firstRead)
                lastSeqNumber = int(firstRead[64:72])
    return parameters

def loadEntities(RawData, RawParameters):
    """
    # Function: loadEntities.
    # Description: Function to load and transform IGES entities into Python Objects.
    # Parameters: * Str RawData = A raw string of the Data Section.
                  * Str RawParameters = A raw string of the Parameter Section.
    # Returns: * List loadedEntities = A list of Entity Python objects representing each
    IGES entity.
    """

    # Note: This  function assumes that all the entities and their respective
    # properties data is sorted in the same way, with a one-to-one relationship
    # between their indexes.

    loadedEntities = []
    if len(RawData) != len(RawParameters):
        print('Imcompatible Number of Data and Parameters!')
        return
    for i in range(len(RawData)):
        loadedObject = loadSingleEntity(RawData[i], RawParameters[i])
        loadedEntities.append(loadedObject)
    return loadedEntities

def loadSingleEntity(RawDataItem, RawParameterItem):
    """
    # Function: loadSingleEntity.
    # Description: Function to load a single entity from an IGES File given its Data Section
    and Parameter Section strings.
    # Parameters: * Str RawDataItem = A string containing the Data Section of an entity.
                  * Str RawParameterItem = A string containing the Parameter Section of an entity.
    # Returns: * Entity loadedObject = The Python object representing the entity.
    """

    # Splitting the String RawDataItem into a RawDataList
    RawDataList = []
    RawDataList.append(RawDataItem[1:8])     # Entity Type
    RawDataList.append(RawDataItem[9:16])    # Parameter Data Pointer
    RawDataList.append(RawDataItem[105:112]) # Parameter Line Counter
    RawDataList.append(RawDataItem[73:80])   # Sequence Number

    # Splitting the String RawParameterItem into a RawParameterList
    numLines = len(RawParameterItem)//81
    parameterString = ''
    for i in range(numLines):
        parameterString += RawParameterItem[(0 + i*81):(64 + i*81)]
    parameterString = parameterString.replace(' ', '')
    parameterString = parameterString.replace(';', '')
    RawParameterList = parameterString.split(',')
    for i in range(len(RawParameterList)):
        RawParameterList[i] = convertData(RawParameterList[i])
    entityType = RawParameterList[0]

    # Loading the object
    loadedObject = None
    if entityType == 186:
        loadedObject = loadManifoldSolid(RawDataList, RawParameterList)
    elif entityType == 514:
        loadedObject = loadShell(RawDataList, RawParameterList)
    elif entityType == 510:
        loadedObject = loadFace(RawDataList, RawParameterList)
    elif entityType == 508:
        loadedObject = loadLoop(RawDataList, RawParameterList)
    elif entityType == 126:
        loadedObject = loadRationalBSplineCurve(RawDataList, RawParameterList)
    elif entityType == 128:
        loadedObject = loadRationalBSplineSurface(RawDataList, RawParameterList)
    elif entityType == 502:
        loadedObject = loadVertexList(RawDataList, RawParameterList)
    elif entityType == 504:
        loadedObject = loadEdgeList(RawDataList, RawParameterList)
    return loadedObject

def getTupleData(RawDataList):
    """
    # Function: getTupleData
    # Description: Function to return a tuple of Global Parameters.
    # Parameters: * List RawDataList = A list of 4 parameteres from the Data Section.
    # Returns: * Tuple = A tuple of the 4 parameters.
    """

    return (RawDataList[0], RawDataList[1], RawDataList[2], RawDataList[3])

# Function to load a Manifold B-Rep Object (Type 186).
def loadManifoldSolid(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
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

# Function to load a Shell (Type 514).
def loadShell(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    N = RawParameterList[1]
    FACEList = []
    OFList = []
    for i in range(1, int(N)+1):
        FACEList.append(RawParameterList[2*i])
        OFList.append(RawParameterList[1+2*i])
    loadedObject = Shell(entityType, PDPointer, parCount, seqNumber, \
                         N, FACEList, OFList)
    return loadedObject

# Function to load a Face (Type 510)
def loadFace(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    SURF = RawParameterList[1]
    N = RawParameterList[2]
    OF = RawParameterList[3]
    LOOPList = []
    for i in range(1, int(N)+1):
        LOOPList.append(RawParameterList[3+i])
    loadedObject = Face(entityType, PDPointer, parCount, seqNumber, \
                        SURF, N, OF, LOOPList)
    return loadedObject

# Function to load a Loop (Type 508)
def loadLoop(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
    N = RawParameterList[1]
    TYPEList = []
    EDGEList = []
    NDXList = []
    OFList = []
    KList = []
    ISOPList = []
    CURVList = []
    i = 2
    for j in range(int(N)):
        TYPEList.append(RawParameterList[i]); i += 1
        EDGEList.append(RawParameterList[i]); i += 1
        NDXList.append(RawParameterList[i]); i += 1
        OFList.append(RawParameterList[i]); i += 1
        KList.append(RawParameterList[i]); i += 1
        ISOPList.append([])
        CURVList.append([])
        for k in range(int(KList[j])):
            ISOPList[j].append(RawParameterList[i]); i += 1
            CURVList[j].append(RawParameterList[i]); i += 1
    loadedObject = Loop(entityType, PDPointer, parCount, seqNumber, \
                        N, TYPEList, EDGEList, NDXList, OFList, KList, ISOPList, CURVList)
    return loadedObject

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

# Function to load a Rational B-Spline Surface (Type 128)
def loadRationalBSplineSurface(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
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

# Function to load a Edge List (Type 504)
def loadEdgeList(RawDataList, RawParameterList):
    entityType, PDPointer, parCount, seqNumber = getTupleData(RawDataList)
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

"""
# Module: IGESImport.py
# Description: This module allow us to import data from an .IGES and .IGS
file, such as geometrical entities.
# Author: Willian Hideak Arita da Silva.
"""

from Import.LoadEdgeList import loadEdgeList
from Import.LoadFace import loadFace
from Import.LoadLoop import loadLoop
from Import.LoadManifoldSolid import loadManifoldSolid
from Import.LoadRationalBSplineCurve import loadRationalBSplineCurve
from Import.LoadRationalBSplineSurface import loadRationalBSplineSurface
from Import.LoadShell import loadShell
from Import.LoadVertexList import loadVertexList

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

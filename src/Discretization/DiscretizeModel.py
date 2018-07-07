"""
# Module: DiscretizeModel.py
# Description: This module aims the discretization of CAD Models
defined in an .IGES and .IGS files.
# Author: Willian Hideak Arita da Silva
"""

from Discretization.PointInPolygon import pointInPolygon
from Discretization.DiscreteNurbCurve import Curve
from Discretization.DiscreteNurbSurface import Surface
from Discretization.Utilities import knotvector_normalize
from numpy import array, dot
from numpy.linalg import inv

def pos(i):
    """
    # Function: pos.
    # Description: Function for getting a correspondent list index using the Sequence Number,
    as definied in an .IGES file.
    # Parameters: * Int i = an index according to the IGES Sequence Number.
    # Returns: * Int = an index according to the Python Lists implementation.
    """
    return ((int(i)-1)//2)

def dotProduct(u, v):
    """
    # Function: dotProduct.
    # Description: Definition of the dot product between two vectors.
    # Parameters: * Tuple u = A tuple of 3 coordinates (x, y, z) representing a vector.
                  * Tuple v = A tuple of 3 coordinates (x, y, z) representing a vector.
    # Returns: * Float dot = The dot product of the two vectors.
    """
    dot = (u[0]*v[0] + u[1]*v[1] + u[2]*v[2])
    return dot

def crossProduct(u, v):
    """
    # Function: crossProduct.
    # Description: Definition of the cross product between two vectors.
    # Parameters: * Tuple u = A tuple of 3 coordinates (x, y, z) representing a vector.
                  * Tuple v = A tuple of 3 coordinates (x, y, z) representing a vector.
    # Returns: * Tuple = The cross product of the two vectors.
    """
    x, y, z = (u[1]*v[2]-u[2]*v[1]), (u[2]*v[0]-u[0]*v[2]), (u[0]*v[1]-u[1]*v[0])
    return (x, y, z)

def subVec(u, v):
    """
    # Function: subVec.
    # Description: Definition of subtraction of vectors.
    # Parameters: * Tuple u = A tuple of 3 coordinates (x, y, z) representing a vector.
                  * Tuple v = A tuple of 3 coordinates (x, y, z) representing a vector.
    # Returns: * Tuple = The subtraction (u - v) where u and v are vectors.
    """
    return ((u[0]-v[0]), (u[1]-v[1]), (u[2]-v[2]))

def scalarVec(s, v):
    """
    # Function: scalarVec.
    # Description: Definition of multiplication of a vector by a scalar.
    # Parameters: * Tuple v = A tuple of 3 coordinates (x, y, z) representing a vector.
    # Returns: * Tuple = The product s*v where s is a scalar and v is a vector.
    """
    newV = [s*i for i in v]
    return (newV[0], newV[1], newV[2])

def normVec(v):
    """
    # Function: normVec.
    # Description: Definition of the norm of a vector.
    # Parameters: * Tuple v = A tuple of 3 coordinates (x, y, z) representing a vector.
    # Returns: * Float = The norm |v|, where v is a vector.
    """
    return ((v[0]**2) + (v[1]**2) + (v[2]**2))**(1/2)

def minimumEdge(vertices):
    """
    # Function: minimumEdge.
    # Description: Definition of the minimum edge. The minimum edge is a group of minimum and
    maximum coordinate of points that lies in a square region and covers a cad model face.
    # Parameters: * List vertices = A list of vertices of a polygon.
    # Returns: * List = A list of two vectors (tuples), each representing the minimum coordinates
                        and the maximum coordinates occupied by the vertices of the polygon.
    """
    minX = maxX = vertices[0][0]
    minY = maxY = vertices[0][1]
    minZ = maxZ = vertices[0][2]
    for point in vertices:
        if point[0] < minX:
            minX = point[0]
        if point[0] > maxX:
            maxX = point[0]
        if point[1] < minY:
            minY = point[1]
        if point[1] > maxY:
            maxY = point[1]
        if point[2] < minZ:
            minZ = point[2]
        if point[2] > maxZ:
            maxZ = point[2]
    minValues = (minX, minY, minZ)
    maxValues = (maxX, maxY, maxZ)
    return [minValues, maxValues]

def changeBasis(vertices, newBaseVector):
    """
    # Function: changeBasis.
    # Description: Performs a basis change of a list of vectors given three new basis vectors.
    # Parameters: * List vertices = A list of points (tuples) that need to change basis.
                  * Tuple newBaseVector = A tuple of three linear independent vectors.
    # Returns: * List newVertices = A list of points (tuples) after the transformation.
    """

    # Find the transformation matrix:
    i, j, k = newBaseVector
    matrix = array([[i[0], j[0], k[0]],
                    [i[1], j[1], k[1]],
                    [i[2], j[2], k[2]]])
    matrix = inv(matrix)
    # Apply the transformation matrix:
    newVertices = []
    for point in vertices:
        x, y, z = point
        vector = array([[x], [y], [z]])
        vector = dot(matrix, vector)
        newVector = (vector[0][0], vector[1][0], vector[2][0])
        newVertices.append(newVector)
    return newVertices

def returnBasis(points, newBaseVector):
    """
    # Function: returnBasis.
    # Description: Returns a list of vectors to the canonical base.
    # Parameters: * List points = A list of points (tuples) that need to return basis.
                  * Tuple newBaseVector = A tuple of three linear independent vectors.
    # Return: * List newPoints = A list of points (tuples) after returning the basis.
    """

    # Find the reverse transformation matrix:
    i, j, k = newBaseVector
    matrix = array([[i[0], j[0], k[0]],
                    [i[1], j[1], k[1]],
                    [i[2], j[2], k[2]]])
    # Apply the reverse transformation matrix:
    newPoints = []
    for point in points:
        x, y, z = point
        vector = array([[x], [y], [z]])
        vector = dot(matrix, vector)
        newVector = (vector[0][0], vector[1][0], vector[2][0])
        newPoints.append(newVector)
    return newPoints

def orthonormalizeBasis(basisVector):
    """
    # Function: orthonormalizeBasis.
    # Description: Function to orthonormalize components i and j of a basis using
    the Gram-Schmidt Process assuming k is already orthogonal to i and j.
    # Parameters: * Tuple basisVector = A tuple of three linear independent vectors.
    # Returns: * Tuple = A tuple of three linear independent orthonormalized vectors.
    """
    i = basisVector[0]
    j = basisVector[1]
    k = basisVector[2]
    s = ((dotProduct(j, i))/(dotProduct(i, i)))
    proj = scalarVec(s, i)
    newJ = subVec(j, proj)
    return [scalarVec((1/normVec(i)), i),
            scalarVec((1/normVec(newJ)), newJ),
            scalarVec((1/normVec(k)), k)]

def discretizeModel(objectList, density, precision, Uparam, Vparam, useParametric, gridDiscretization):
    """
    # Function: discretizeModel.
    # Description: This function receives an objectList
    # Parameters: * List objectList = A list of Entity objects obtained with the IGESImport module.
                  * Float density = Number of points/cm desired in the discretization.
                  * Float precision = The number of discrete intervals desired for discretization of
                  the loop that surrounds the surface. This is necessary for using the PointInPolygon
                  module.
                  * Int Uparam = The number of discrete intervals desired for the discretization
                  in the parametric U direction of the surface.
                  * Int Vparam = The number of discrete intervals desired for the discretization
                  in the parametric V direction of the surface.
                  * Boolean useParametric = Determines if the parametric discretization will be used.
    # Returns: * Tuple = A list containing the sequence numbers of the IGES file, a list containing
               the normal vector of each point related to the suface and a list containing the
               discretized points.
    """

    # Get a list of planar faces in the model:
    planarFacePointers = []
    nonPlanarFacePointers = []
    for myObject in objectList:
        if (myObject != None and myObject.entityType == 510 and \
        objectList[pos(myObject.SURF)].K1 == 1 and \
        objectList[pos(myObject.SURF)].K2 == 1 and \
        objectList[pos(myObject.SURF)].M1 == 1 and \
        objectList[pos(myObject.SURF)].M2 == 1):
            planarFacePointers.append(int(myObject.seqNumber))
        elif(myObject != None and myObject.entityType == 510 and useParametric):
            nonPlanarFacePointers.append(int(myObject.seqNumber))
    # Discretize each planar face:
    faceSequenceNumbers = []
    faceNormalVectors = []
    cloudPointsList = []
    for i in planarFacePointers:
        points, normals = discretizeFace(objectList[pos(i)], objectList, density, precision, gridDiscretization)
        faceSequenceNumbers.append(i)
        faceNormalVectors.append(normals)
        cloudPointsList.append(points)
    # Discretize each non-planar face:
    for i in nonPlanarFacePointers:
        points, normals = discretizeSurface(objectList[pos(i)], objectList, Uparam, Vparam)
        faceSequenceNumbers.append(i)
        faceNormalVectors.append(normals)
        cloudPointsList.append(points)
    return faceSequenceNumbers, faceNormalVectors, cloudPointsList

def discretizeFace(face, objectList, density, precision, gridDiscretization):
    """
    # Function: discretizeFace.
    # Description: This function generates a list of cloud points based on a specific face.
    A face is a surface surrounded by a loop.
    # Parameters: * Entity face = The Python object representing the face for discretization.
                  * List objectList = A list of Entity objects obtained with the IGESImport module.
                  * Float density = Number of points/cm desired in the discretization.
                  * Float precision = The number of discrete intervals desired for discretization of
                  the loop that surrounds the surface. This is necessary for using the PointInPolygon
                  module.
    # Returns: * List newPoints = A list of discretized vertices.
               * List normals = A list of normal vectors of to each point related to the surface.
    """

    # List to storage all the tuples (x, y, z) due to discretization.
    points = []

    # List to storage all the normal vectors due to discretization.
    normals = []

    # Collecting all the vertices of the planar face.
    currentLoop = objectList[pos(face.LOOPList[0])]
    vertices = discretizeLoop(currentLoop, objectList, precision)

    if (len(vertices) < 3):
        return points, normals

    # Estabilishing three base vectors for the plane:
    a, b, c = vertices[0], vertices[1], vertices[2]
    i = subVec(a, b)
    j = subVec(a, c)
    k = crossProduct(i, j)
    newBasisVector = (i, j, k)

    # Checking if vector k is a zero-length vector:
    if normVec(k) == 0:
        return points, normals

    # Orthogonalizing the basis vector through the Gram-Schmidt process.
    newBasisVector = orthonormalizeBasis(newBasisVector)

    # Changing the coordinates from original basis to the new one.
    newVertices = changeBasis(vertices, newBasisVector)

    # Getting the miminum and maximum edges:
    minEdges, maxEdges = minimumEdge(newVertices)
    zCoord = minEdges[2]

    if(gridDiscretization):
        # Discretizing the model with the N x N grid parameter:
        spacingX = (maxEdges[0]-minEdges[0])/density
        spacingY = (maxEdges[1]-minEdges[1])/density

        # Creating additional points due to discretization:
        for i in range(1, int(density)):
            for j in range(1, int(density)):
                newX = minEdges[0] + i*spacingX
                newY = minEdges[1] + j*spacingY
                newPoint = (newX, newY, zCoord)
                points.append(newPoint)
    else:
        # Discretizing the model with the N points/mm parameter:
        numSpacesX = (maxEdges[0]-minEdges[0])*density
        numSpacesY = (maxEdges[1]-minEdges[1])*density

        # Creating additional points due to discretization:
        for i in range(1, int(numSpacesX)+1):
            for j in range(1, int(numSpacesY)+1):
                newX = minEdges[0] + i*(1/density)
                newY = minEdges[1] + j*(1/density)
                newPoint = (newX, newY, zCoord)
                points.append(newPoint)

    # Verifying if the new points lies inside the original boundary:
    auxList = []
    for point in points:
        if(pointInPolygon(point[0], point[1], newVertices)):
            auxList.append(point)
    points = auxList

    # Verifying if the new points has some inner loops to consider;
    for i in range(1, len(face.LOOPList)):
        currentLoop = objectList[pos(face.LOOPList[i])]
        vertices = discretizeLoop(currentLoop, objectList, precision)

        # Converting the 3D vertices to 2D:
        newVertices = changeBasis(vertices, newBasisVector)

        auxList = []
        auxList = []
        for point in points:
            if(not pointInPolygon(point[0], point[1], newVertices)):
                auxList.append(point)
        points = auxList

    # Changing the new points to the original basis:
    newPoints = returnBasis(points, newBasisVector)

    # Creating a vector of normal vectors:
    for i in range(len(newPoints)):
        normals.append(newBasisVector[2])
    return newPoints, normals

def discretizeLoop(currentLoop, objectList, precision):
    """
    # Function: discretizeLoop.
    # Description: This function generates a list of points that lies in a specific loop using
    the NURBS parametric discretization provided by the DiscreteNurbCurve module.
    # Parameters: * Entity currentLoop = The Python object representing the loop for discretization.
                  * List objectList = A list of Entity objects obtained with the IGESImport module.
                  * Float precision = The number of discrete intervals desired for discretization.
    # Returns: * List vertices = A list of discretized vertices.
    """

    unsortedVertices = []

    for i in range(int(currentLoop.N)):
        currentEdge = int(currentLoop.EDGEList[i])
        currentEdgeIndex = int(currentLoop.NDXList[i])

        startVertex = int(objectList[pos(currentEdge)].SVPList[currentEdgeIndex-1])
        startVertexIndex = int(objectList[pos(currentEdge)].SVList[currentEdgeIndex-1])
        endVertex = int(objectList[pos(currentEdge)].TVPList[currentEdgeIndex-1])
        endVertexIndex = int(objectList[pos(currentEdge)].TVList[currentEdgeIndex-1])

        unsortedVertices.append([])

        # Getting the Start Vertex tuple.
        x = objectList[pos(startVertex)].XList[startVertexIndex-1]
        y = objectList[pos(startVertex)].YList[startVertexIndex-1]
        z = objectList[pos(startVertex)].ZList[startVertexIndex-1]
        vertex = (x, y, z)
        unsortedVertices[i].append(vertex)

        # Getting the intermediate vertices in case of non-straight edges:
        spaceCurve = int(objectList[pos(currentEdge)].CURVList[currentEdgeIndex-1])
        spaceCurve = objectList[pos(spaceCurve)]
        if(int(spaceCurve.K) != 1):
            newCurve = Curve()
            newCurve.delta = (1/precision)
            newCurve.degree = int(spaceCurve.M)
            newCurve.knotvector = list(spaceCurve.TList)
            newCurve.ctrlpts = [[spaceCurve.XList[i], spaceCurve.YList[i], spaceCurve.ZList[i]] \
                                for i in range(len(spaceCurve.WList))]
            newCurve.weights = list(spaceCurve.WList)
            newCurve.evaluate_rational()
            for j in range(1, len(newCurve.curvepts)-1):
                unsortedVertices[i].append(newCurve.curvepts[j])

        # Getting the End Vertex tuple
        x = objectList[pos(endVertex)].XList[endVertexIndex-1]
        y = objectList[pos(endVertex)].YList[endVertexIndex-1]
        z = objectList[pos(endVertex)].ZList[endVertexIndex-1]
        vertex = (x, y, z)
        unsortedVertices[i].append(vertex)

    # Sorting the vertices according to the formed polygon:
    vertices = []
    vertices += unsortedVertices[0]
    unsortedVertices = unsortedVertices[1:]
    for i in range(len(unsortedVertices)):
        for j in range(len(unsortedVertices)):
            if(unsortedVertices[j][0] == vertices[-1]):
                del unsortedVertices[j][0]
                vertices += unsortedVertices[j]
                del unsortedVertices[j]
                break
            elif(unsortedVertices[j][len(unsortedVertices[j])-1] == vertices[-1]):
                del unsortedVertices[j][len(unsortedVertices[j])-1]
                vertices += list(reversed(unsortedVertices[j]))
                del unsortedVertices[j]
                break
    return vertices

def discretizeSurface(face, objectList, Uparam, Vparam):
    """
    # Function: discretizeSurface.
    # Description: This function generates a list of cloud points based on a specific surface.
    # Parameters: * Entity face = The Python object representing the face that contains the
                  surface for discretization.
                  * List objectList = A list of Entity objects obtained with the IGESImport module.
                  * Int Uparam = The number of discrete intervals desired for the discretization
                  in the parametric U direction of the surface.
                  * Int Vparam = The number of discrete intervals desired for the discretization
                  in the parametric V direction of the surface.
    # Returns: * Tuple = A list containing the points and a list containig the normal vector of
               each point related to the surface.
    """
    currentSurface = objectList[pos(face.SURF)]
    newSurface = Surface()
    newSurface.delta_u = 1/Uparam
    newSurface.delta_v = 1/Vparam
    newSurface.degree_u = int(currentSurface.M1)
    newSurface.degree_v = int(currentSurface.M2)
    newSurface.knotvector_u = list(currentSurface.SList)
    newSurface.knotvector_v = list(currentSurface.TList)
    surfData = open('..\\tmp\\SurfaceData.txt', 'w')
    surfText = ''
    for j in range(len(currentSurface.XList[0])):
        for i in range(len(currentSurface.XList)):
            surfText += (str(currentSurface.XList[i][j] * currentSurface.WList[i][j]) + ',' +
                         str(currentSurface.YList[i][j] * currentSurface.WList[i][j]) + ',' +
                         str(currentSurface.ZList[i][j] * currentSurface.WList[i][j]) + ',' +
                         str(currentSurface.WList[i][j]))
            if i == (len(currentSurface.XList) - 1):
                surfText += '\n'
            else:
                surfText += ';'
    surfData.write(surfText)
    surfData.close()
    newSurface.read_ctrlptsw('..\\tmp\\SurfaceData.txt')
    newSurface.evaluate_rational()
    return list(newSurface.surfpts), list(newSurface.normal_direct)

def generatePcd(cloudPoints, filePath):
    """
    # Function: generatePcd.
    # Description: This function generates a file CloudData.pcd containing all the
    cloud points specified in the cloudPoints list.
    # Parameters: * List cloudPoints = The list of desired points.
                  * Str filePath = A string containing the file path for saving.
    """
    numberOfPoints = 0
    for item in cloudPoints:
        numberOfPoints += len(item)
    pcdText = ('# .PCD v.7 - Point Cloud Data file format\n' +
               'VERSION .7\n' +
               'FIELDS x y z\n' +
               'SIZE 4 4 4\n' +
               'TYPE F F F\n' +
               'COUNT 1 1 1 1\n' +
               'WIDTH ' + str(numberOfPoints) + '\n' +
               'HEIGHT 1\n' +
               'POINTS ' + str(numberOfPoints) + '\n' +
               'DATA ascii\n')
    for item in cloudPoints:
        for point in item:
            pcdText += (str(point[0]) + ' ' +
                        str(point[1]) + ' ' +
                        str(point[2]) + '\n')
    pcdFile = open(filePath, 'w')
    pcdFile.write(pcdText)
    pcdFile.close()

def generateTxt(cloudPoints, filePath):
    """
    # Function: generateTxt.
    # Description: This function generates a file TxtData.txt containing all the
    cloud points specified in the cloudPoints list.
    # Parameters: * List cloudPoints = The list of desired points.
                  * Str filePath = A string containing the file path for saving.
    """
    txtText = ''
    for item in cloudPoints:
        for point in item:
            txtText += (str(point[0]) + ' ' +
                        str(point[1]) + ' ' +
                        str(point[2]) + '\n')
    pcdFile = open(filePath, 'w')
    pcdFile.write(txtText)
    pcdFile.close()

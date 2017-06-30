# Module: DiscretizeModel.py
# Description: This module aims the discretization of CAD Models
# defined in an .IGES and .IGS files.

# Author: Willian Hideak Arita da Silva
# Last edit: June, 26, 2017.

from Discretization.PointInPolygon import pointInPolygon
from Discretization.WindingNumber import windingNumber
from Discretization.DiscreteNurbCurve import Curve
from Discretization.DiscreteNurbSurface import Surface
from Discretization.Utilities import knotvector_normalize
from numpy import array, dot
from numpy.linalg import solve, inv

# Function for getting a correspondent list index using the Sequence Number,
# as defined in an .IGES file.
def pos(i):
    return ((int(i)-1)//2)

# Definition of the dot product between two vectors.
# Returns (u * v), u and v are vectors.
def dotProduct(u, v):
    dot = (u[0]*v[0] + u[1]*v[1] + u[2]*v[2])
    return dot

# Definition of the cross product between two vectors.
# Returns (u x v), u and v are vectors.
def crossProduct(u, v):
    x, y, z = (u[1]*v[2]-u[2]*v[1]), (u[2]*v[0]-u[0]*v[2]), (u[0]*v[1]-u[1]*v[0])
    return (x, y, z)

# Definition of subtraction of vectors.
# Returns (u - v), u and v are vectors.
def subVec(u, v):
    return ((u[0]-v[0]), (u[1]-v[1]), (u[2]-v[2]))

# Definition of multiplication of a vector by a scalar.
# Returns s*v, where s is a scalar and v is a vector.
def scalarVec(s, v):
    newV = [s*i for i in v]
    return (newV[0], newV[1], newV[2])

# Definition of the norm of a vector.
# Returns |v|, where v is a vector in R^3 space.
def normVec(v):
    return ((v[0]**2) + (v[1]**2) + (v[2]**2))**(1/2)

# Definition of the minimum edge. The minimum edge is a group of minimum and maximum
# points that lies in a square region and covers a CAD model face.
def minimumEdge(vertices):
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

# Change of basis:
def changeBasis(vertices, newBaseVector):
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

# Re-change of basis:
def returnBasis(points, newBaseVector):
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

# Function to orthonormalize components i and j of a basis using
# the Gram–Schmidt Process assuming k is already orthogonal to i and j:
def orthonormalizeBasis(basisVector):
    i = basisVector[0]
    j = basisVector[1]
    k = basisVector[2]
    s = ((dotProduct(i, j))/(dotProduct(j, j)))
    proj = scalarVec(s, j)
    newI = subVec(i, proj)
    return [scalarVec((1/normVec(newI)), newI),
            scalarVec((1/normVec(j)), j),
            scalarVec((1/normVec(k)), k)]

# Function to discretize an entire model.
def discretizeModel(objectList, density, precision, Uparam, Vparam, useParametric):
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
        points, normals = discretizeFace(objectList[pos(i)], objectList, density, precision)
        faceSequenceNumbers.append(i)
        faceNormalVectors = normals
        cloudPointsList.append(points)
    # Discretize each non-planar face:
    for i in nonPlanarFacePointers:
        points, normals = discretizeSurface(objectList[pos(i)], objectList, Uparam, Vparam)
        faceSequenceNumbers.append(i)
        faceNormalVectors.append(normals)
        cloudPointsList.append(points)
    return faceSequenceNumbers, faceNormalVectors, cloudPointsList

# Function to discretize a single face. It returns a list of cloud points.
def discretizeFace(face, objectList, density, precision):
    # List to storage all the tuples (x, y, z) due to discretization.
    points = []

    # Collecting all the vertices of the planar face.
    unsortedVertices = []
    currentLoop = objectList[pos(face.LOOPList[0])]
    vertices = discretizeLoop(currentLoop, objectList, precision)

    if (len(vertices) < 3):
        return points

    # Estabilishing three base vectors for the plane:
    a, b, c = vertices[0], vertices[1], vertices[2]
    i = subVec(a, b)
    j = subVec(a, c)
    k = crossProduct(i, j)
    newBasisVector = (i, j, k)

    # Orthogonalizing the basis vector through the Gram-Schmidt process.
    newBasisVector = orthonormalizeBasis(newBasisVector)

    # Changing the coordinates from original basis to the new one.
    newVertices = changeBasis(vertices, newBasisVector)

    # Getting the miminum and maximum edges:
    minEdges, maxEdges = minimumEdge(newVertices)
    zCoord = minEdges[2]

    # Discretizing the model with the 'density' parameter:
    numSpacesX = (maxEdges[0]-minEdges[0])*density
    numSpacesY = (maxEdges[1]-minEdges[1])*density

    # Creating additional points due to discretization:
    for i in range(1, int(numSpacesX)):
        for j in range(1, int(numSpacesY)):
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
    normals = []
    for i in range(len(newPoints)):
        normals.append(newBasisVector)
    return newPoints, normals

# Function to discretize a single Loop. It returns a list of vertices of the loop.
def discretizeLoop(currentLoop, objectList, precision):
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
    return list(newSurface.surfpts)

# Function to generate a .pcd (Point Cloud Data) file:
def generatePcd(cloudPoints):
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
    pcdFile = open('..\\tmp\\CloudData.pcd', 'w')
    pcdFile.write(pcdText)
    pcdFile.close()

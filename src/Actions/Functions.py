"""
# Module: Functions.py
# Description: This module contains some functions that can be called by the application.
These functions are necessary to provide some internal functionality, and can be easily
assigned with the current UI buttons.
# Author: Willian Hideak Arita da Silva.
"""

from OCC.Graphic3d import Graphic3d_ArrayOfPoints
from OCC.AIS import AIS_PointCloud
from OCC.Quantity import Quantity_Color, Quantity_NOC_WHITE
from OCC.Aspect import Aspect_TOM_POINT
from OCC.Prs3d import Prs3d_PointAspect

def cleanCloud(parent):
    """
    # Function: cleanCloud.
    # Description: This function can clean the current pointCloudObject.
    # Parameters: * QMainWindow parent = A reference for the main window object.
    """
    parent.canvas._display.Context.Erase(parent.pointCloudObject.GetHandle(), True)
    parent.pointCloudObject = None

def buildCloud(parent):
    """
    # Function: buildCloud.
    # Description: This function builds a new pointCloudObject and displays it in the local
    context.
    # Parameters: * QMainWindow parent = A reference for the main window object.
    """

    # Crates an array of points for displaying in the point Cloud:
    numberOfPoints = sum(len(points) for points in parent.cloudPointsList)
    pointsArray = Graphic3d_ArrayOfPoints(numberOfPoints)
    for points in parent.cloudPointsList:
        for point in points:
            pointsArray.AddVertex(point[0], point[1], point[2])

    # Adds the array of points in a new unselectable point cloud object:
    pointCloud = AIS_PointCloud()
    pointCloud.SetPoints(pointsArray.GetHandle())
    pointCloud.UnsetSelectionMode()

    # Displays the point cloud in the local context:
    localContext = parent.canvas._display.GetContext().GetObject()
    localContext.Display(pointCloud.GetHandle())

    # Sets a new aspect for displaying the points in the point cloud:
    newAspect = Prs3d_PointAspect(Aspect_TOM_POINT, Quantity_Color(Quantity_NOC_WHITE), 2)
    pointCloud.SetAspect(newAspect.GetHandle())
    parent.canvas._display.Repaint()

    # Updates the main window properties:
    parent.activeCloudFile = 'Pontos Gerados Nesta Sessão'
    parent.pointCloudObject = pointCloud
    parent.pointAspectObject = newAspect

def rebuildCloud(parent):
    """
    # Function: rebuildCloud.
    # Description: This function simply calls the cleanCloud() and the buildCloud() functions.
    # Parameters: * QMainWindow parent = A reference for the main window object.
    """
    cleanCloud(parent)
    buildCloud(parent)

def restoreCloud(parent):
    localContext = parent.canvas._display.GetContext().GetObject()
    localContext.Display(parent.pointCloudObject.GetHandle())
    parent.pointCloudObject.SetAspect(parent.pointAspectObject.GetHandle())
    parent.canvas._display.Repaint()

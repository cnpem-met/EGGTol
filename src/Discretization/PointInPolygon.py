"""
# Module: PointInPolygon.py
Description: This module implements the Even-Odd Rule algorithm to check
if a given point (x, y) lies inside a polygon with a tuple of vertices 'poly'.
# Author: Willian Hideak Arita da Silva.
"""

def pointInPolygon(x, y, poly):
    """
    # Function: pointInPolygon.
    # Description: This function determines if a point is inside a polygon.
    # Parameters: * Float x = The X coordinate of the point.
                  * Float y = The Y coordinate of the point.
                  * List poly = A list of tuples, each tuple being a polygon vertex.
    # Returns: * Boolean result = True if the point lies inside, and False otherwise.
    """

        num = len(poly)
        i = 0
        j = num - 1
        result = False
        # Checking the 'insideness' for each given points:
        for i in range(num):
                if  ((poly[i][1] > y) != (poly[j][1] > y)) and \
                        (x < (poly[j][0] - poly[i][0]) * (y - poly[i][1]) / \
                        (poly[j][1] - poly[i][1]) + poly[i][0]):
                    result = not result
                j = i
        return result

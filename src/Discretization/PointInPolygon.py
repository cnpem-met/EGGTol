# Module: PointInPolygon.py
# Description: This module implements the Even-Odd Rule algorithm to check
# if a given point (x, y) lies inside a polygon with a tuple of vertices 'poly'.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 24, 2017.

def pointInPolygon(x, y, poly):
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

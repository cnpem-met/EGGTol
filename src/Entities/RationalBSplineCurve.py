"""
# Module: RationalBSplineCurve.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

# Class: RationalBSplineCurve
# Type: 126
# Description: This class contains data from Rational B-Spline Curves.

class RationalBSplineCurve(Entity):
    """
    # Class: RationalBSplineCurve.
    # Description: This class contains data from Rational B-Spline Curves.
    """

    # Defining Properties
    def __init__ (self, entityType, PDPointer, parCount, seqNumber, \
                  K, M, PROP1, PROP2, PROP3, PROP4, TList, WList, XList, YList, ZList, \
                  V0, V1, XNORM, YNORM, ZNORM):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str K = Upper index of the sum.
                      * Str M = Degree of basis function.
                      * Str PROP1 = Flag for checking if the curve is planar.
                      * Str PROP2 = Flag for checking if the curve is closed.
                      * Str PROP3 = Flag for checking if it is Rational or Polynomial.
                      * Str PROP4 = Flag for checking if it is periodic.
                      * List TList = List of the Knot Sequence.
                      * List WList = List of weights.
                      * List XList = List control points (coordinate X).
                      * List YList = List control points (coordinate Y).
                      * List ZList = List control points (coordinate Z).
                      * Str V0 = Starting parameter value.
                      * Str V1 = Ending parameter value.
                      * Str XNORM = Unit normal (coordinate X).
                      * Str YNORM = Unit normal (coordinate Y).
                      * Str ZNORM = Unit normal (coordinate Z).
        """

        super().__init__(126, PDPointer, parCount, seqNumber)
        self.K = K
        self.M = M
        self.PROP1 = PROP1
        self.PROP2 = PROP2
        self.PROP3 = PROP3
        self.PROP4 = PROP4
        self.TList = TList
        self.WList = WList
        self.XList = XList
        self.YList = YList
        self.ZList = ZList
        self.V0 = V0
        self.V1 = V1
        self.XNORM = XNORM
        self.YNORM = YNORM
        self.ZNORM = ZNORM

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        out = ('#' + str(int(self.seqNumber)//2+1) + ' Rational B-Spline Curve (IGES 126)', [])
        out[1].append(('* Upper Index of Sum (K): ' + str(self.K), []))
        out[1].append(('* Degree of Basis Function (M): ' + str(self.M), []))
        out[1].append(('* NonPlanar or Planar? (PROP1): ' + str(self.PROP1), []))
        out[1].append(('* Open or Closed Curve? (PROP2): ' + str(self.PROP2), []))
        out[1].append(('* Rational or Polynomial? (PROP3): ' + str(self.PROP3), []))
        out[1].append(('* NonPeriodic or Periodic? (PROP4): ' + str(self.PROP4), []))
        for i in range(int(self.M)+int(self.K)+2):
            out[1].append(('* Knot Sequence (T(' + str(i-int(self.M)) + ')): ' + str(self.TList[i]), []))
        for i in range(int(self.K)+1):
            out[1].append(('* Weight Sequence (W(' + str(i) + ')): ' + str(self.WList[i]), []))
        for i in range(int(self.K)+1):
            out[1].append(('* Control Point (X(' + str(i) + ')): ' + str(self.XList[i]), []))
            out[1].append(('* Control Point (Y(' + str(i) + ')): ' + str(self.YList[i]), []))
            out[1].append(('* Control Point (Z(' + str(i) + ')): ' + str(self.ZList[i]), []))
        out[1].append(('* Starting Parameter Value (V(0)): ' + str(self.V0), []))
        out[1].append(('* Ending Parameter Value (V(1)): ' + str(self.V1), []))
        out[1].append(('* Unit Normal X (XNORM): ' + str(self.XNORM), []))
        out[1].append(('* Unit Normal Y (YNORM): ' + str(self.YNORM), []))
        out[1].append(('* Unit Normal Z (ZNORM): ' + str(self.ZNORM), []))
        return out

    def __str__(self):
        """
        # Method: __str__.
        # Description: Provides information for debug purposes.
        # Returns: * Str out = A string containing the object properties.
        """

        out = 'Rational B-Spline Curve (Type 126)\n'
        out += '* Upper Index of Sum (K): ' + str(self.K) + '\n'
        out += '* Degree of Basis Function (M): ' + str(self.M) + '\n'
        out += '* NonPlanar or Planar? (PROP1): ' + str(self.PROP1) + '\n'
        out += '* Open or Closed Curve? (PROP2): ' + str(self.PROP2) + '\n'
        out += '* Rational or Polynomial? (PROP3): ' + str(self.PROP3) + '\n'
        out += '* NonPeriodic or Periodic? (PROP4): ' + str(self.PROP4) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.M)+int(self.K)+2):
            out += '* Knot Sequence (T(' + str(i-int(self.M)) + ')): ' + str(self.TList[i]) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.K)+1):
            out += '* Weight Sequence (W(' + str(i) + ')): ' + str(self.WList[i]) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.K)+1):
            out += '* Control Point (X(' + str(i) + ')): ' + str(self.XList[i]) + '\n'
            out += '* Control Point (Y(' + str(i) + ')): ' + str(self.YList[i]) + '\n'
            out += '* Control Point (Z(' + str(i) + ')): ' + str(self.ZList[i]) + '\n'
        out += '* -----------------------------------\n'
        out += '* Starting Parameter Value (V(0)): ' + str(self.V0) + '\n'
        out += '* Ending Parameter Value (V(1)): ' + str(self.V1) + '\n'
        out += '* Unit Normal X (XNORM): ' + str(self.XNORM) + '\n'
        out += '* Unit Normal Y (YNORM): ' + str(self.YNORM) + '\n'
        out += '* Unit Normal Z (ZNORM): ' + str(self.ZNORM) + '\n'
        return out

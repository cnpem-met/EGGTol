# Module: RationalBSplineCurve.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

from Entities.Entity import Entity

# Class: RationalBSplineCurve
# Type: 126
# Description: This class contains data from Rational B-Spline Curves.

class RationalBSplineCurve(Entity):

    # Defining Properties
    def __init__ (self, entityType, PDPointer, parCount, seqNumber, \
                  K, M, PROP1, PROP2, PROP3, PROP4, TList, WList, XList, YList, ZList, \
                  V0, V1, XNORM, YNORM, ZNORM):
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
        pass

    def __str__(self):
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

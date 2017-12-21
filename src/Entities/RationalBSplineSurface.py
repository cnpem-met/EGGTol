"""
# Module: RationalBSplineSurface.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

from Entities.Entity import Entity

class RationalBSplineSurface(Entity):
    """
    # Class: RationalBSplineSurface
    # Description: This class contains data from Rational B-Spline Surfaces.
    """

    # Defining Prpoerties
    def __init__(self, entityType, PDPointer, parCount, seqNumber, \
                 K1, K2, M1, M2, PROP1, PROP2, PROP3, PROP4, PROP5, \
                 SList, TList, WList, XList, YList, ZList, U0, U1, V0, V1):
        """
        # Method: __init__.
        # Description: The init method for initializing inherited properties and defining
        new ones.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
                      * Str K1 = Upper index of first sum.
                      * Str K2 = Upper index of second sum.
                      * Str M1 = Degree of first basis functions.
                      * Str M2 = Degree of second basis functions.
                      * Str PROP1 = Flag for checking if the surface is closed in U direction.
                      * Str PROP2 = Flag for checking if the surface is closed in V direction.
                      * Str PROP3 = Flag for checking if it is Rational or Polynomial.
                      * Str PROP4 = Flag for checking if it is periodic in U direction.
                      * Str PROP5 = Flag for checking if it is periodic in V direction.
                      * List SList = List of the first Knot Sequence.
                      * List TList = List of the second Knot Sequence.
                      * List WList = List of weights.
                      * List XList = List control points (coordinate X).
                      * List YList = List control points (coordinate Y).
                      * List ZList = List control points (coordinate Z).
                      * Str U0 = Starting parameter value in U direction.
                      * Str U1 = Ending parameter value in U direction.
                      * Str V0 = Starting parameter value in V direction.
                      * Str V1 = Ending parameter value in V direction.
        """

        super().__init__(128, PDPointer, parCount, seqNumber)
        self.K1 = K1
        self.K2 = K2
        self.M1 = M1
        self.M2 = M2
        self.PROP1 = PROP1
        self.PROP2 = PROP2
        self.PROP3 = PROP3
        self.PROP4 = PROP4
        self.PROP5 = PROP5
        self.SList = SList
        self.TList = TList
        self.WList = WList
        self.XList = XList
        self.YList = YList
        self.ZList = ZList
        self.U0 = U0
        self.U1 = U1
        self.V0 = V0
        self.V1 = V1

    def description(self):
        out = ('(' + str(int(self.seqNumber)//2+1) + ') Superfície BSpline (IGES 128)', [])
        out[1].append(('- Upper Index of First Sum (K1): ' + str(self.K1), []))
        out[1].append(('- Upper index of Second Sum (K2): ' + str(self.K2), []))
        out[1].append(('- Degree of First Basis Functions (M1): ' + str(self.M1), []))
        out[1].append(('- Degree of Second Basis Functions (M2): ' + str(self.M2), []))
        out[1].append(('- Closed in Direction U? (PROP1): ' + str(self.PROP1), []))
        out[1].append(('- Closed in Direction V? (PROP2): ' + str(self.PROP2), []))
        out[1].append(('- Rational or Polynomial? (PROP3): ' + str(self.PROP3), []))
        out[1].append(('- NonPeriodic or Pediodic in U? (PROP4): ' + str(self.PROP4), []))
        out[1].append(('- NonPeriodic or Periodic in V? (PROP5): ' + str(self.PROP5), []))
        for i in range(int(self.M1)+int(self.K1)+2):
            out[1].append(('- First Knot Sequence (S(' + str(i-int(self.M1)) + ')): ' + str(self.SList[i]), []))
        for i in range(int(self.M2)+int(self.K2)+2):
            out[1].append(('- Second Knot Sequence (T(' + str(i-int(self.M2)) + ')): ' + str(self.TList[i]), []))
        for i in range(int(self.K2)+1):
            for j in range(int(self.K1)+1):
                out[1].append(('- Weight Sequence (W(' + str(j) + ', ' + str(i) + ')): ' + str(self.WList[j][i]), []))
        for i in range(int(self.K2)+1):
            for j in range(int(self.K1)+1):
                out[1].append(('- Control Point (X(' + str(j) + ', ' + str(i) + ')): ' + str(self.XList[j][i]), []))
                out[1].append(('- Control Point (Y(' + str(j) + ', ' + str(i) + ')): ' + str(self.YList[j][i]), []))
                out[1].append(('- Control Point (Z(' + str(j) + ', ' + str(i) + ')): ' + str(self.ZList[j][i]), []))
        out[1].append(('- Starting Parameter Value (U(0)): ' + str(self.U0), []))
        out[1].append(('- Ending Parameter Value (U(1)): ' + str(self.U1), []))
        out[1].append(('- Starting Parameter Value (V(0)): ' + str(self.V0), []))
        out[1].append(('- Ending Parameter Value (V(1)): ' + str(self.V1), []))
        return out

    def __str__(self):
        out = 'Rational B-Spline Surface (Type 128)\n'
        out += '* Upper Index of First Sum (K1): ' + str(self.K1) + '\n'
        out += '* Upper index of Second Sum (K2): ' + str(self.K2) + '\n'
        out += '* Degree of First Basis Functions (M1): ' + str(self.M1) + '\n'
        out += '* Degree of Second Basis Functions (M2): ' + str(self.M2) + '\n'
        out += '* Closed in Direction U? (PROP1): ' + str(self.PROP1) + '\n'
        out += '* Closed in Direction V? (PROP2): ' + str(self.PROP2) + '\n'
        out += '* Rational or Polynomial? (PROP3): ' + str(self.PROP3) + '\n'
        out += '* NonPeriodic or Pediodic in U? (PROP4): ' + str(self.PROP4) + '\n'
        out += '* NonPeriodic or Periodic in V? (PROP5): ' + str(self.PROP5) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.M1)+int(self.K1)+2):
            out += '* First Knot Sequence (S(' + str(i-int(self.M1)) + ')): ' + str(self.SList[i]) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.M2)+int(self.K2)+2):
            out += '* Second Knot Sequence (T(' + str(i-int(self.M2)) + ')): ' + str(self.TList[i]) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.K2)+1):
            for j in range(int(self.K1)+1):
                out += '* Weight Sequence (W(' + str(j) + ', ' + str(i) + ')): ' + str(self.WList[j][i]) + '\n'
        out += '* -----------------------------------\n'
        for i in range(int(self.K2)+1):
            for j in range(int(self.K1)+1):
                out += '* Control Point (X(' + str(j) + ', ' + str(i) + ')): ' + str(self.XList[j][i]) + '\n'
                out += '* Control Point (Y(' + str(j) + ', ' + str(i) + ')): ' + str(self.YList[j][i]) + '\n'
                out += '* Control Point (Z(' + str(j) + ', ' + str(i) + ')): ' + str(self.ZList[j][i]) + '\n'
        out += '* -----------------------------------\n'
        out += '* Starting Parameter Value (U(0)): ' + str(self.U0) + '\n'
        out += '* Ending Parameter Value (U(1)): ' + str(self.U1) + '\n'
        out += '* Starting Parameter Value (V(0)): ' + str(self.V0) + '\n'
        out += '* Ending Parameter Value (V(1)): ' + str(self.V1) + '\n'
        return out

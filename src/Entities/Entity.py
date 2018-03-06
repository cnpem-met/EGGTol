"""
# Module: Entity.py
# Description: This module contains classes definitions for creating objects
to store data from IGES Entities, such as points, planes, surfaces and more.
# Author: Willian Hideak Arita da Silva.
"""

class Entity(object):
    """
    # Class: Entity.
    # Description: Base class for all kind of IGES entities. Will be inhirited by
    other specific classes.
    """

    # Static Property
    numEntities = 0

    # Getting global parameters
    def __init__(self, entityType, PDPointer, parCount, seqNumber):
        """
        # Method: __init__.
        # Description: The init method for defining properties.
        # Parameters: * Str entityType = The Entity Type number.
                      * Str PDPointer = The Parameter Data pointer.
                      * Str parCount = The Parameter Line Count number.
                      * Str seqNumber = The Sequence number.
        """

        Entity.numEntities += 1
        self.entityType = entityType
        self.PDPointer = PDPointer
        self.parCount = parCount
        self.seqNumber = seqNumber

    def description(self):
        """
        # Method: description.
        # Description: Provides a tuple of information for being used in a TreeView.
        # Returns: * Tuple out = A tuple containing a string and a list of properties.
        """

        return (('# Unknown IGES Entity', []))

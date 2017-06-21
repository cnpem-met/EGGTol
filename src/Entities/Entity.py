# Module: Entity.py
# Description: This module contains classes definitions for creating objects
# to store data from IGES Entities, such as points, planes, surfaces and more.

# Author: Willian Hideak Arita da Silva.
# Last edit: April, 10, 2017.

# Class: Entity
# Description: Base class for all kind of IGES entities. Will be inhirited by
# other specific classes.

class Entity(object):

    # Static Property
    numEntities = 0

    # Getting global parameters
    def __init__(self, entityType, PDPointer, parCount, seqNumber):
        Entity.numEntities += 1
        self.entityType = entityType
        self.PDPointer = PDPointer
        self.parCount = parCount
        self.seqNumber = seqNumber

    def description(self):
        return (('Unsupported Entity', []))

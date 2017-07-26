"""
# Module: testFile.py
# Description: This is a simple file used for testing purposes. It can list all IGES parameters of
an IGES File, given its location in the loadIGESFile function.
"""

from Import.IGESImport import *
a = loadIGESFile('..\\examples\\Cylinder.igs')
data = getRawData(a)
param = getRawParameters(a)
entities = loadEntities(data, param)

for i in range(len(entities)):
    print(2*i+1, '- ', end='')
    print(entities[i])

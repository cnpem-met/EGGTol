# TestFile

from Import.IGESImport import *
a = loadIGESFile('..\\examples\\BoredCube.igs')
data = getRawData(a)
param = getRawParameters(a)
entities = loadEntities(data, param)

for i in range(len(entities)):
    print(2*i+1, '- ', end='')
    print(entities[i])

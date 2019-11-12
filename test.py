from number.FloatNumber import FloatNumber
from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
from matrix.MyMatrix import MyMatrix
import numpy
import random
import fractions

# ckrawczyk
# mrybarczyk

# print("test")

globalMax = 65536
fabric = NumberFabric()
numberType = NumberType.FLOAT

# number.print()
# number.add(FloatNumber(10, 2))
# print(number.value)

def createMatrix(size, numberType):
    a = [[None for i in range (0,size)] for j in range (0,size)]
    x = [None for i in range (0,size)]
    for i in range (0,size):
        nominator = random.uniform(-globalMax, globalMax - 1)
        number = fabric.createNumberFromType(numberType, nominator, globalMax)
        x[i] = number.value
        for j in range (0,size):
            nominator = random.uniform(-globalMax, globalMax-1)
            number = fabric.createNumberFromType(numberType, nominator, globalMax)
            a[i][j] = number.value
    b = numpy.matmul(a,x)
    return MyMatrix(a, b, x)

m = createMatrix(10, numberType)
size=10
for i in range (0,size):
    print()
    for j in range (0,size):
        print(m.getValueFromPosition(i, j))





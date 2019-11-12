from number.FloatNumber import FloatNumber
from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
import numpy
import random
import fractions

# ckrawczyk
# mrybarczyk

# print("test")


fabric = NumberFabric()
numberType = NumberType.FLOAT

# number.print()
# number.add(FloatNumber(10, 2))
# print(number.value)

def createMatrix(size, numberType):
    mojaMacierz = [[None for i in range(size)] for j in range(size)]
    for i in range (0,size):
        for j in range (0,size):
            nominator = random.uniform(-500, 500)
            denominator = random.uniform(-500, 500)
            number = fabric.createNumberFromType(numberType, nominator, denominator)
            mojaMacierz[i][j] = number.value
    return mojaMacierz

print(createMatrix(10, numberType))





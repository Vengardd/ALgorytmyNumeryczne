# ckrawczyk
# mrybarczyk

from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
from matrix.matrixGenerator import createMatrix, printMatrix
import numpy
import random

size = 10 # z czego size potem będzie w pętli, od 0 do jakiejś tam dużej liczby
maxRandomValue = 65536
minRandomValue = -65536
fabric = NumberFabric()
numberType = NumberType.FLOAT

m = createMatrix(size, numberType)
printMatrix(m, size)





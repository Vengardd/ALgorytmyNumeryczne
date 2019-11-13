# ckrawczyk
# mrybarczyk

from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
from matrix.createMatrix import createMatrix, printMatrix
from time import perf_counter

size = 10 # z czego size potem będzie w pętli, od 0 do jakiejś tam dużej liczby (WAŻNE PRZY TESTACH)
maxRandomValue = 65536
minRandomValue = -65536
fabric = NumberFabric()
numberTypex = NumberType.FLOAT
numberTypey = NumberType.DECIMAL
numberTypez = NumberType.FRACTION

x = createMatrix(size, numberTypex)
y = createMatrix(size, numberTypey)
z = createMatrix(size, numberTypez)


# b = m.__str__
# print(b)

x.gaussNone()
y.gaussPartial()
z.gaussComplete()

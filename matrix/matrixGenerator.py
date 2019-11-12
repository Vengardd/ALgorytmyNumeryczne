from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
from matrix.MyMatrix import MyMatrix
import numpy
import random

size = 10 # z czego size potem będzie w pętli, od 0 do jakiejś tam dużej liczby
maxRandomValue = 65536
minRandomValue = -65536
fabric = NumberFabric()
numberType = NumberType.FLOAT

def createMatrix(size, numberType):
    matrix = [[None for i in range (0,size)] for j in range (0,size)]
    results = [None for i in range (0,size)]
    for i in range (0,size):
        nominator = random.uniform(minRandomValue, maxRandomValue - 1)
        number = fabric.createNumberFromType(numberType, nominator, maxRandomValue)
        results[i] = number.value
        for j in range (0,size):
            nominator = random.uniform(minRandomValue, maxRandomValue-1)
            number = fabric.createNumberFromType(numberType, nominator, maxRandomValue)
            matrix[i][j] = number.value
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
    # https://www.tutorialspoint.com/numpy/numpy_matmul.htm
    vector = numpy.matmul(matrix,results)
    return MyMatrix(matrix, vector, results)

def printMatrix(m, size):
    for i in range(0, size):
        print()
        for j in range(0, size):
            print(m.getValueFromPosition(i, j))
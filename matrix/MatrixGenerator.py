from number.NumberFabric import NumberFabric
from number.NumberType import NumberType
from matrix.MyMatrix import MyMatrix
import numpy
import random


class MatrixGenerator:

    def __init__(self) -> None:
        super().__init__()
        self.maxRandomValue = 65535
        self.minRandomValue = -65536
        self.fabric = NumberFabric()

    def createMatrix(self, size, numberType):
        matrix = [[None for i in range(0, size)] for j in range(0, size)]
        results = [None for i in range(0, size)]
        for i in range(0, size):
            nominator = random.randint(self.minRandomValue, self.maxRandomValue)
            number = self.fabric.createNumberFromType(numberType, nominator, self.maxRandomValue + 1)
            results[i] = number.value
            for j in range(0, size):
                nominator = random.randint(self.minRandomValue, self.maxRandomValue)
                number = self.fabric.createNumberFromType(numberType, nominator, self.maxRandomValue + 1)
                matrix[i][j] = number.value
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html
        # https://www.tutorialspoint.com/numpy/numpy_matmul.htm
        vector = numpy.matmul(matrix, results)
        return MyMatrix(matrix, vector, results)


    def printMatrix(m, size):
        for i in range(0, size):
            for k in range(0, size):
                print(m.matrix[i][k])

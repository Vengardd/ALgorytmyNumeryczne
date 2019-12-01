import datetime

from matrix.MatrixGenerator import MatrixGenerator
from number.NumberType import NumberType

import random


class Test:

    def __init__(self):
        super().__init__()
        self.matrixGenerator = MatrixGenerator()

    def createTests(self, size):
        numberTypes = [NumberType.FLOAT, NumberType.DECIMAL, NumberType.FRACTION]

        numbers = [None for i in range(0, size*size*2)]
        maxRandomValue = 65535
        minRandomValue = -65536
        for i in range(0, 2 * size * size):
            numbers[i] = random.randint(minRandomValue, maxRandomValue)
        for counter, option in enumerate(numberTypes):
            print(option)
            iterNumbers = iter(numbers)
            matrix = self.matrixGenerator.createMatrixFromGivenNumbers(size, option, iterNumbers)
            a = datetime.datetime.now()
            matrix.gaussNone()
            b = datetime.datetime.now()
            delta = b - a
            print("Gauss.NONE" + ", " + option.__str__() + ": " + delta.__str__())
            iterNumbers = iter(numbers)
            matrix = self.matrixGenerator.createMatrixFromGivenNumbers(size, option, iterNumbers)
            a = datetime.datetime.now()
            matrix.gaussPartial()
            b = datetime.datetime.now()
            delta = b - a
            print("Gauss.PARTIAL" + ", " +  option.__str__() + ": " + delta.__str__())
            iterNumbers = iter(numbers)
            matrix = self.matrixGenerator.createMatrixFromGivenNumbers(size, option, iterNumbers)
            a = datetime.datetime.now()
            matrix.gaussComplete()
            b = datetime.datetime.now()
            delta = b - a
            print("Gauss.COMPLETE" + ", " +  option.__str__() + ": " + delta.__str__())


test = Test()
test.createTests(300)

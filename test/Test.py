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
            matrix.gaussNone()
            matrix.printResults()
            iterNumbers = iter(numbers)
            matrix = self.matrixGenerator.createMatrixFromGivenNumbers(size, option, iterNumbers)
            matrix.gaussPartial()
            matrix.printResults()
            iterNumbers = iter(numbers)
            matrix = self.matrixGenerator.createMatrixFromGivenNumbers(size, option, iterNumbers)
            matrix.gaussComplete()
            matrix.printResults()


test = Test()
test.createTests(100)

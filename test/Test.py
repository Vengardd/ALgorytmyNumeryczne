from matrix.MatrixGenerator import MatrixGenerator
from number.NumberType import NumberType


class Test:

    def __init__(self):
        super().__init__()
        self.matrixGenerator = MatrixGenerator()


    def createTests(self, size):
        numberTypes = [NumberType.FLOAT]

        for counter, option in enumerate(numberTypes):
                print(option)
                matrix = self.matrixGenerator.createMatrix(size, option)
                matrix.gaussNone()
                matrix.printResults()
                matrix = self.matrixGenerator.createMatrix(size, option)
                matrix.gaussPartial()
                matrix.printResults()
                matrix = self.matrixGenerator.createMatrix(size, option)
                matrix.gaussComplete()
                matrix.printResults()


test = Test()
test.createTests(10)
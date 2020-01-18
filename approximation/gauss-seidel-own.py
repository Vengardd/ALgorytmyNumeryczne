from collections import namedtuple

import numpy

class Gauss_seidel_own:

    def asd(self, inputMatrix, matrixSolution, xo, tolerance, numberOfIterations):
        ownMatrix = self.createOwnMatrix(inputMatrix)
        return self.gaussSeidelForOwnMatrix(ownMatrix, matrixSolution, xo, tolerance, numberOfIterations)

    def createOwnMatrix(self, inputMatrix):
        ownMatrix = {}
        for i in range(0, len(inputMatrix)):
            for j in range(0, len(inputMatrix[0])):
                if(inputMatrix[i][j] != 0):
                    ownMatrix[(i, j)] = inputMatrix[i][j]
        return ownMatrix

    def gaussSeidelForOwnMatrix(self, ownMatrix, matrixSolution, xo, tolerance, numberOfIterations):
        x = [None] * len(matrixSolution)
        n = len(matrixSolution)
        for k in range(0, numberOfIterations):
            for i in range(0, n):
                firstMultiplier = 1 / ownMatrix.get((i,i))
                secondMultiplier = self.createSecondMultiplier(ownMatrix, i, x, matrixSolution, xo)
                x[i] = firstMultiplier * secondMultiplier
            if abs(numpy.linalg.norm(numpy.subtract(x, xo))) < tolerance:
                return x
            for i in range(0, n):
                xo[i] = x[i]
        return x

    def createSecondMultiplier(self, ownMatrix, actualIteration, x, vector, xo):
        firstComponent = self.createFirstComponent(ownMatrix, actualIteration, x)
        secondComponent = self.createSecondComponent(ownMatrix, actualIteration, len(vector), xo)
        return firstComponent + secondComponent + vector[actualIteration]

    def createFirstComponent(self, inputMatrix, i, x):
        sum = 0
        for j in range(0, i):
            if((i,j) in inputMatrix):
                sum += inputMatrix[(i, j)] * x[j]
        return - sum

    def createSecondComponent(self, inputMatrix, i, n, xo):
        sum = 0
        for j in range(i+1, n):
            if ((i, j) in inputMatrix):
                sum += inputMatrix[(i, j)] * xo[j]
        return - sum


inputMatrix = [[2, 1, 1], [3, 5, 2], [2, 1, 4]]
vector = [5, 15, 8]
xo = [1, 1, 1]

test = Gauss_seidel_own()
print(test.asd(inputMatrix, vector, xo, 0.00001, 30))
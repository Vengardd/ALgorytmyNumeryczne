import numpy as np
from scipy.sparse import csr_matrix

class Gauss_seidel_sparse_matrix:

    def asd(self, inputMatrix, matrixSolution, xo, tolerance, numberOfIterations):
        inputMatrix = csr_matrix(inputMatrix)
        x = [None] * len(matrixSolution)
        n = len(matrixSolution)
        for k in range(0, numberOfIterations):
            for i in range(0, n):
                firstMultiplier = 1 / inputMatrix[i,i]
                secondMultiplier = self.createSecondMultiplier(inputMatrix, i, x, matrixSolution, xo)
                x[i] = firstMultiplier * secondMultiplier
            if abs(np.linalg.norm(np.subtract(x, xo))) < tolerance:
                return x
            for i in range(0, n):
                xo[i] = x[i]
        return x

    def createSecondMultiplier(self, inputMatrix, actualIteration, x, vector, xo):
        firstComponent = self.createFirstComponent(inputMatrix, actualIteration, x)
        secondComponent = self.createSecondComponent(inputMatrix, actualIteration, len(vector), xo)
        return firstComponent + secondComponent + vector[actualIteration]

    def createFirstComponent(self, inputMatrix, i, x):
        sum = 0
        for j in range(0, i):
            sum += inputMatrix[(i, j)] * x[j]
        return - sum

    def createSecondComponent(self, inputMatrix, i, n, xo):
        sum = 0
        for j in range(i+1, n):
            sum += inputMatrix[(i, j)] * xo[j]
        return - sum

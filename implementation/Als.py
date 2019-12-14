# KOD : CEZARY KRAWCZYK
import numpy

from matrix.MyMatrix import MyMatrix


class Als:

    def als(self, input, U, P, lambd):
        for userNumber in range(0, len(input)):
            U = self.forSingleU(input, U, P, lambd, userNumber)
        for productNumber in range(0, len(input[0])):
            P = self.forSingleP(input, U, P, lambd, productNumber)
        return U, P

    def forSingleU(self, input, U, P, lambd, userNumber):
        indexes = self.createIu(input, userNumber)
        Uip = self.createUip(P, indexes)
        vector = self.createVectorFromUip(input, P, userNumber, indexes)
        Au = self.createAu(Uip, len(P), lambd)
        mymatrix = MyMatrix(Au, vector, None)
        mymatrix.gaussPartial()
        U = self.setColumnFromGauss(U, mymatrix.resultsGeneratedInGauss, userNumber)
        return U

    def createIu(self, input, userNumber):
        indexes = []
        for i in range(0, len(input[userNumber])):
            if input[userNumber][i] != 0:
                indexes.append(i)
        return indexes

    def createUip(self, P, indexes):
        uip = []
        for i in range(0, len(P)):
            uip.append([])
        for i in range(0, len(indexes)):
            for j in range(0, len(P)):
                uip[j].append(P[j][indexes[i]])
        return uip

    def createVectorFromUip(self, input, P, userNumber, indexes):
        vector = []
        for i in range(0, len(P)):
            tempValue = 0
            for j in range(0, len(indexes)):
                rating = input[userNumber][indexes[j]]
                tempValue += P[i][indexes[j]] * rating
            vector.append(tempValue)
        return vector

    def createAu(self, Uip, D, lambd):
        UipTransponed = numpy.transpose(Uip)
        return Uip @ UipTransponed + lambd * numpy.identity(D)

    def setColumnFromGauss(self, U, result, userNumber):
        for i in range(0, len(U)):
            U[i][userNumber] = result[i]
        return U

    def forSingleP(self, input, U, P, lambd, productNumber):
        indexes = self.createIp(input, productNumber)
        Piu = self.createUip(U, indexes)
        vector = self.createVectorFromPiu(input, U, productNumber, indexes)
        Au = self.createAu(Piu, len(P), lambd)
        mymatrix = MyMatrix(Au, vector, None)
        mymatrix.gaussPartial()
        P = self.setColumnFromGauss(P, mymatrix.resultsGeneratedInGauss, productNumber)
        return P

    def createIp(self, input, productNumber):
        indexes = []
        for i in range(0, len(input)):
            if input[i][productNumber] != 0:
                indexes.append(i)
        return indexes

    def createVectorFromPiu(self, input, U, productNumber, indexes):
        vector = []
        for i in range(0, len(U)):
            tempValue = 0
            for j in range(0, len(indexes)):
                rating = input[indexes[j]][productNumber]
                tempValue += U[i][indexes[j]] * rating
            vector.append(tempValue)
        return vector

    def createResult(self, U, P):
        R = []
        for i in range(0, len(input)):
            R.append([])
            for j in range(0, len(input[0])):
                transponedU = numpy.transpose(self.getColumn(U, i))
                value = numpy.dot(transponedU, self.getColumn(P, j))
                R[i].append(value)
        return R

    def getColumn(self, matrix, number):
        result = []
        for i in range(0, len(matrix)):
            result.append(matrix[i][number])
        return result

        # P1 P2 P3


input = [[1, 2, 3],  # U1
         [5, 0, 1],  # U2
         [0, 1, 2],  # U3
         [1, 4, 5]]  # U4      n x m

P = [[0.1, 0.2, 0.3],
     [0.4, 0.5, 0.6],
     [0.7, 0.8, 0.9]]  # d x m

U = [[0.12, 0.11, 0.10, 0.1],
     [0.9, 0.8, 0.7, 0.2],
     [0.6, 0.5, 0.4, 0.3]]  # d x n

als = Als()
for i in range(0, 50):
    U, P = als.als(input, U, P, 0.1)
R = als.createResult(U, P)
print(R)

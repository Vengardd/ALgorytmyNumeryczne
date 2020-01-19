import numpy as np


class CSI_domi:

    def __init__(self, points):
        self.points = points
        self.matrix = np.zeros((len(self.points), len(self.points)))
        self.vector = np.zeros(len(self.points))
        self.mVector = None
        self.fill()

    def mV(self, res):
        self.mVector = res

    def fill(self):
        self.matrix[0][0] = 2
        for i in range(1, len(self.matrix)-1):
            self.fillRow(i)
        self.matrix[len(self.matrix) - 1][len(self.matrix) - 1] = 2

    def fillRow(self, row):
        self.matrix[row][row - 1] = self.mi(row)
        self.matrix[row][row] = 2
        self.matrix[row][row + 1] = self.lamb(row)
        self.vector[row] = self.delt(row)

    def delt(self, j):
        p1 = 6 / (self.h(j) + self.h(j + 1))
        p2 = (self.fx(j + 1) - self.fx(j)) / self.h(j + 1)
        p3 = (self.fx(j) - self.fx(j - 1)) / self.h(j)

        return p1 * (p2 - p3)

    def fx(self, j):
        return self.points[j][1]

    def lamb(self, j):
        return self.h(j + 1) / (self.h(j) + self.h(j + 1))

    def mi(self, j):
        return self.h(j) / (self.h(j) + self.h(j + 1))

    def h(self, j):
        return self.points[j][0] - self.points[j - 1][0]

    def getFXfromInterpolate(self, x):
        i = self.getIndexOfX(x)
        diff = x - self.points[i][0]
        value = self.a(i) + (self.b(i) * diff) + (self.c(i) * diff * diff) + (self.d(i) * diff * diff * diff)
        return value

    # Nie jestem tego pewna - Dominika

    def getIndexOfX(self, x):
        if self.points[0][0] < self.points[1][0]:
            for i in range(1, len(self.points)):
                if x <= self.points[i][0]:
                    return i - 1
        else:
            for i in range(1, len(self.points)):
                if x >= self.points[i][0]:
                    return i - 1


    def a(self, j):
        return self.fx(j)


    def b(self, j):
        p1 = (self.fx(j + 1) - self.fx(j)) / self.h(j + 1)
        p2 = (2 * self.mVector[j])
        return p1 - p2 * self.h(j + 1)


    def c(self, j):
        return self.vector[j] / 2


    def d(self, j):
        numerator = self.mVector[j + 1] - self.mVector[j]
        denominator = 6 * self.h(j + 1)
        return numerator / denominator
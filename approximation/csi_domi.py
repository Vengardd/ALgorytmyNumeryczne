import numpy as np


class CSI_domi:

    def __init__(self, points):
        self.points = points
        self.matrix = np.zeros((len(self.points), len(self.points)))
        self.vector = np.zeros(len(self.points))
        self.fill()

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

    #
    # y_points = [24, 25, 23, 20, 16]
    # x_points = [12, 13, 14, 15, 16]


csiPoints = [[12, 24], [13, 25], [14, 23], [15, 20], [16, 16]]
csiObject = CSI_domi(csiPoints)
print(csiObject.matrix)

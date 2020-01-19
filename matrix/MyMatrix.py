import numpy


class MyMatrix:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.size = len(matrix[0])
        self.vector = vector
        self.vector2 = vector
        self.what = matrix
        self.resultsFromFullMatrix = matrix

    def __str__(self) -> str:
        for i in range(0, self.size):
            for k in range(0, self.size):
                print(self.matrix[i][k])
        return ""

    def swapRows(self, x, y):
        temp = self.matrix[x]
        self.matrix[x] = self.matrix[y]
        self.matrix[y] = temp

    def swapColumns(self, x, y):
        temp = [None for i in range(0, self.size)]
        for i in range(len(self.matrix)):
            temp[i] = self.matrix[i][x]
        for i in range(len(self.matrix)):
            self.matrix[i][x] = self.matrix[i][y]
        for i in range(len(self.matrix)):
            self.matrix[i][y] = temp[i]

    # https://users.wpi.edu/~walker/MA2073/HANDOUTS/gaussian_elim.pdf
    # http://www.math-cs.gordon.edu/courses/mat342/handouts/gauss.pdf?fbclid=IwAR3nPc8-mIXlRW0Vt7f78LQFb_22b4jGZ7mag4xHbLanei7Gw9FDmaf9aRE
    def gaussNone(self):
        for i in range(0, self.size-1):
            for j in range(i+1, self.size):
                if self.matrix[i][i] == 0:
                    raise Exception(ZeroDivisionError)
                else:
                    self.matrix[j][i] = self.matrix[j][i] / self.matrix[i][i]
                for k in range(i+1, self.size):
                    self.matrix[j][k] -= (self.matrix[j][i]*self.matrix[i][k])
        for i in range (0, self.size-1):
            for j in range(i+1, self.size):
                self.vector[j] -= (self.matrix[j][i]*self.vector[i])
        for i in range (self.size-1, -1, -1):
            foo = self.vector[i]
            for j in range(i+1, self.size):
                foo -= (self.matrix[i][j] * self.resultsFromFullMatrix[j])
            self.resultsFromFullMatrix[i] = foo / self.matrix[i][i]

    def gaussPartial(self):
        foo = [0 for i in range(0, self.size)]
        pointers = [i for i in range(0, self.size)]
        for i in range(0, self.size):
            for j in range(0, self.size):
                temp = [foo[i], abs(self.matrix[i][j])]
                foo[i] = max(temp)
        for i in range(0, self.size-1):
            maxValue = 0
            for j in range(i, self.size):
                y = abs(self.matrix[pointers[j]][i]/foo[pointers[j]])
                if y > maxValue:
                    maxValue = y
                    t = j
            temp = pointers[i]
            pointers[i] = pointers[t]
            pointers[t] = temp
            for j in range (i+1, self.size):
                self.matrix[pointers[j]][i] = -(self.matrix[pointers[j]][i]) / self.matrix[pointers[i]][i]
                for k in range(i+1, self.size):
                    self.matrix[pointers[j]][k] += (self.matrix[pointers[j]][i]*self.matrix[pointers[i]][k])
        for i in range(0, self.size-1):
            for j in range(i+1, self.size):
                self.vector[pointers[j]] += (self.matrix[pointers[j]][i]*self.vector[pointers[i]])
        for i in range(self.size-1, -1, -1):
            foo = self.vector[pointers[i]]
            for j in range(i+1, self.size):
                foo -= (self.matrix[pointers[i]][j] * self.resultsFromFullMatrix[j])
            self.resultsFromFullMatrix[i] = foo / self.matrix[pointers[i]][i]

    # https://au.mathworks.com/matlabcentral/fileexchange/13451-gauss-elimination-with-complete-pivoting
    def gaussComplete(self):
        n = self.size
        matrix = self.matrix
        columns = [i for i in range(0, n)]
        rows = [i for i in range(0, n)]
        for i in range(0, n - 1):
            maxValue = 0
            for j in range(i, n):
                for k in range(i, n):
                    y = abs(matrix[rows[j]][columns[k]])
                    if y > maxValue:
                        maxValue = y
                        rowindex = j
                        colindex = k
            temp = rows[i]
            rows[i] = rows[rowindex]
            rows[rowindex] = temp
            temp = columns[i]
            columns[i] = columns[colindex]
            columns[colindex] = temp
            for j in range(i + 1, n):
                matrix[rows[j]][columns[i]] /= matrix[rows[i]][columns[i]]
                for k in range(i + 1, n):
                    matrix[rows[j]][columns[k]] -= (matrix[rows[j]][columns[i]] * matrix[rows[i]][columns[k]])
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                self.vector[rows[j]] -= (matrix[rows[j]][columns[i]] * self.vector[rows[i]])
        for i in range(n - 1, -1, -1):
            foo = self.vector[rows[i]]
            for j in range(i + 1, n):
                foo -= (matrix[rows[i]][columns[j]] * self.resultsFromFullMatrix[columns[j]])
            self.resultsFromFullMatrix[columns[i]] = foo / matrix[rows[i]][columns[i]]




class MyMatrix:
    def __init__(self, matrix, vector, results):
        self.matrix = matrix
        self.size = len(matrix[0])
        self.vector = vector
        self.resultsGeneratedIncreateMatrix = results
        self.resultsGeneratedInGauss = [0 for i in range(0, self.size)]

    # def __str__(self):
    #     string = ""
    #     for i in (0, self.size):
    #        for j in (0, self.size):
    #            string += (self.matrix[i][j])
    #     return string
    # to tak średnio chce działać, ale to działa jak toString() z javy

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
            for j in range(0, self.size):
                if self.matrix[i][i] == 0:
                    raise Exception(ZeroDivisionError)
                else:
                    self.matrix[j][i] = -(self.matrix[j][i]) / self.matrix[i][i]
                for k in range(i+1, self.size):
                    self.matrix[j][k] += (self.matrix[j][i]*self.matrix[i][k])
        for i in range (0, self.size-1):
            for j in range(i+1, self.size):
                self.vector[j] += (self.matrix[i][j]*self.vector[i])
        for i in range (self.size-1, -1, -1):
            foo = self.vector[i]
            for j in range(i+1, self.size):
                foo -= (self.matrix[i][j] * self.resultsGeneratedInGauss[j])
            self.resultsGeneratedInGauss[i] = foo / self.matrix[i][i]

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
                foo -= (self.matrix[pointers[i]][j] * self.resultsGeneratedInGauss[j])
            self.resultsGeneratedInGauss[i] = foo / self.matrix[pointers[i]][i]

    # https://au.mathworks.com/matlabcentral/fileexchange/13451-gauss-elimination-with-complete-pivoting
    def gaussComplete(self):
        columns = [i for i in range (0, self.size)]
        rows = [i for i in range (0, self.size)]
        for i in range(0, self.size-1):
            maxValue = 0
            for j in range(i, self.size):
                for k in range(i, self.size):
                    y = abs(self.matrix[rows[j]][columns[k]])
                    if y > maxValue:
                        maxValue = y
                        rowIndex = j
                        columnIndex = k
            self.swapRows(i, rowIndex)
            self.swapColumns(i, columnIndex)
            for j in range(i+1, self.size):
                self.matrix[rows[j]][columns[i]] /= self.matrix[rows[i]][columns[i]]
                for k in range (i+1, self.size):
                    self.matrix[rows[j]][columns[k]] -= (self.matrix[rows[j]][columns[i]] * self.matrix[rows[i]][columns[k]])

        for i in range(0, self.size-1):
            for j in range(i+1, self.size):
                self.vector[rows[j]] += (self.matrix[rows[j]][columns[i]] * self.vector[rows[i]])

        for i in range(self.size-1, -1, -1):
            foo = self.vector[rows[i]]
            for j in range(i+1, self.size):
                foo -= (self.matrix[rows[i]][columns[j]] * self.resultsGeneratedInGauss[columns[j]])
            self.resultsGeneratedInGauss[columns[i]] = foo / self.matrix[rows[i]][columns[i]]


#          for i in range (0, self.size):       ???
#             for j in range(0, i):             ???
#                 self.matrix[i][j] = 0         ???



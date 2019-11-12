class MyMatrix:
    def __init__(self, matrix, vector, results):
        self.matrix = matrix
        self.vector = vector
        self.results = results

    def swapRows(self, x, y):
        temp = self.matrix[x]
        self.matrix[x] = self.matrix[y]
        self.matrix[y] = temp

    def swapColumns(self, x, y):
        temp = []
        for i in range(len(self.matrix)):
            temp.append(self.matrix[i][x])
        for i in range(len(self.matrix)):
            self.matrix[i][x] = self.matrix[i][y]
        for i in range(len(self.matrix)):
            self.matrix[i][y] = temp[i]

    def getValueFromPosition(self, x, y):
       return self.matrix[x][y]
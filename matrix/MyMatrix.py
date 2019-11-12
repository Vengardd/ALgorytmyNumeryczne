class MyMatrix:
    def __init__(self, a, b, x):
        self.a = a
        self.b = b
        self.x = x

    def swapRows(self, x, y):
        temp = self.a[x]
        self.a[x] = self.a[y]
        self.a[y] = temp

    def swapColumns(self, x, y):
        temp = []
        for i in range(len(self.a)):
            temp.append(self.a[i][x])
        for i in range(len(self.a)):
            self.a[i][x] = self.a[i][y]
        for i in range(len(self.a)):
            self.a[i][y] = temp[i]

    def getValueFromPosition(self, x, y):
       return self.a[x][y]
# KOD : DOMINIKA CESARZ

import numpy as np
from numpy import linalg as LA

from implementation.Als import Als
from implementation.parser_domi import Parser


class Implementation:
    p = None
    u = None
    r = None
    rCopy = None

    def __init__(self, lamb, d, iterations, path, category):
        self.lamb = lamb
        self.d = d
        self.parser = Parser(path, category)
        self.als = Als()
        self.i = iterations

    @staticmethod
    def generate(h, w):
        m = np.random.random((h, w))
        return m

    # Ten kawałek: Marta Rybarczyk ###

    def fup(self):
        uArray = np.array(self.u)
        uArrayTransposed = np.transpose(self.u)
        pArray = np.array(self.p)
        multipliedUP = np.matmul(uArrayTransposed, pArray)
        sumRUP = 0
        sumUU = 0
        sumPP = 0
        for u in range(0, len(self.u[0])):
            for p in range(0, len(self.p[0])):
                sumRUP += (self.r[u][p] - multipliedUP[u][p]) ** 2
        for u in range(0, len(self.u)):
            sumUU += LA.norm(uArray[u]) ** 2
        for p in range(0, len(self.p)):
            sumPP += LA.norm(pArray[p]) ** 2
        foo = self.lamb * (sumUU + sumPP)
        fup = sumRUP + foo
        # print(fup)

    def calculatingErrors(self, r):
        sumErrors = 0
        qErrors = 1
        for i in range(0, len(self.rCopy)):
            for j in range(0, len(self.rCopy[0])):
                if (self.rCopy[i][j] != 0):
                    sumErrors += abs(self.rCopy[i][j] - r[i][j])
                    qErrors+=1
        aproxErrors = sumErrors/qErrors
        return aproxErrors

    ##################################

    def do_alg(self):
        self.r, id_list = self.parser.getparsed()
        self.rCopy = [[0 for i in range(0, len(self.r[0]))] for j in range(0, len(self.r))]
        for i in range(0, len(self.r)):
            for j in range(0, len(self.r[0])):
                self.rCopy[i][j] = self.r[i][j]
        p_size = len(self.r[0])
        u_size = len(self.r)

        self.p = self.generate(self.d, p_size)
        self.u = self.generate(self.d, u_size)

        for j in range(0, self.i):
            self.u, self.p = self.als.als(self.r, self.u, self.p, self.lamb)
            self.fup()

        r = self.als.createResult(self.u, self.p)
        aproxErrors = self.calculatingErrors(r)
        print("średnia błędu = ", aproxErrors)
        return r

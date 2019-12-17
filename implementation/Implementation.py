# KOD : DOMINIKA CESARZ

import numpy as np
from numpy import linalg as LA
from implementation.ControlledParser import ControlledParser
from implementation.Als import Als

class Implementation:
    p = None
    u = None
    r = None
    rCopy = None
    fup_r = None

    def __init__(self, lamb, d, iterations, max_p):
        self.lamb = lamb
        self.d = d
        self.parser = ControlledParser()
        self.als = Als()
        self.i = iterations
        self.max_p = max_p

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
        self.fup_r = sumRUP + foo
        # print(fup)

    def calculatingErrors(self, r):
        sumErrors = 0
        qErrors = 1
        for i in range(0, len(self.rCopy)):
            for j in range(0, len(self.rCopy[0])):
                if self.rCopy[i][j] != 0:
                    sumErrors += abs(self.rCopy[i][j] - r[i][j])
                    qErrors += 1
        aproxErrors = sumErrors / qErrors
        return aproxErrors

    ##################################

    def do_alg(self):
        self.parser.parseToNewFile(self.max_p)
        self.r = self.parser.parseFromNewFile()
        self.rCopy = np.copy(self.r)
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

    def zb(self):
        self.parser.parseToNewFile(self.max_p)
        self.r = self.parser.parseFromNewFile()
        p_size = len(self.r[0])
        u_size = len(self.r)
        zbieznosc = []
        foo1 = 0
        foo2 = 0

        self.p = self.generate(self.d, p_size)
        self.u = self.generate(self.d, u_size)

        for j in range(0, self.i):
            self.u, self.p = self.als.als(self.r, self.u, self.p, self.lamb)
            self.fup()
            if j % 2 == 0:
                foo1 = self.fup_r
                if j != 0:
                    zbieznosc.append((foo1 - foo2) / foo1)
            elif j % 2 == 1:
                foo2 = self.fup_r
                zbieznosc.append((foo2 - foo1) / foo2)

        return zbieznosc


i = Implementation(0.1, 5, 10, 500)
r = i.do_alg()
print(r)
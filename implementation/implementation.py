# KOD : DOMINIKA CESARZ

# W importach może wywalać błedy ale wszystko jest ok

import numpy as np
from Als import Als
from parser_domi import Parser


class Implementation:
    p = None
    u = None
    r = None

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

    def do_alg(self):
        self.r, id_list = self.parser.getparsed()
        p_size = len(self.r[0])
        u_size = len(self.r)

        self.p = self.generate(self.d, p_size)
        self.u = self.generate(self.d, u_size)

        for j in range(0, self.i):
            self.u, self.p = self.als.als(self.r, self.u, self.p, self.lamb)

        r = self.als.createResult(self.u, self.p)
        return r


imp = Implementation(0.1, 3, 50, "amazon-meta-small.txt", '|Books[283155]')
print(imp.do_alg())

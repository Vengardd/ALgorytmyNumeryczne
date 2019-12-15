# KOD: Marta Rybarczyk

from datetime import datetime
from implementation.Implementation import Implementation

class Test:
    def test_LD(self, i):
        for lamb in range(1, 10):
            for d in range(1, 6):
                l = lamb / 10
                imp = Implementation(l, d, i, "amazon-meta-small.txt", '|Books[283155]')
                a = datetime.now()
                result = imp.do_alg()
                b = datetime.now()
                delta = b - a
                print("wykonania ALS = ", i, ", d = ", d, ", lambda = ", l, ", czas = ", delta)
                # print(result)
                # print()

    def test_D(self, i):
        for d in range(1, 6):
            imp = Implementation(0.1, d, i, "amazon-meta-small.txt", '|Books[283155]')
            a = datetime.now()
            result = imp.do_alg()
            b = datetime.now()
            delta = b - a
            print("wykonania ALS = ", i, ", d = ", d, ", lambda = 0.1, czas = ", delta)
            # print(result)
            # print()

    def test_L(self, i):
        for lamb in range(1, 10):
            l = lamb / 10
            imp = Implementation(l, 3, i, "amazon-meta-small.txt", '|Books[283155]')
            a = datetime.now()
            result = imp.do_alg()
            b = datetime.now()
            delta = b - a
            print("wykonania ALS = ", i, ", d = 3, lambda = ", l, ", czas = ", delta)
            # print(result)
            # print()
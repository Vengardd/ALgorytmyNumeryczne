# KOD: Marta Rybarczyk

from datetime import datetime
from implementation.Implementation import Implementation

class Test:
    def testing(self, i, d, lamb, max_p):
        for k in lamb:
            for j in d:
                imp = Implementation(k, j, i, max_p)
                a = datetime.now()
                result = imp.do_alg()
                b = datetime.now()
                delta = b - a
                print("wykonania ALS = ", i, ", d = ", j, ", lambda = ", k, ", czas = ", delta)
                # print(result)
                # print()

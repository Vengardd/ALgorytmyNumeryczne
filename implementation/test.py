# KOD: Marta Rybarczyk

from datetime import datetime
from implementation.Implementation import Implementation

class Test:
    def testing(self, i, names, d, lamb, cat):
        for f in names:
            for k in lamb:
                for j in d:
                    imp = Implementation(k, j, i, f, cat)
                    a = datetime.now()
                    result = imp.do_alg()
                    b = datetime.now()
                    delta = b - a
                    print("wykonania ALS = ", i, ", d = ", j, ", lambda = ", k, ", czas = ", delta)
                    # print(result)
                    # print()

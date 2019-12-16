# KOD: Marta Rybarczyk

from datetime import datetime
from implementation.Implementation import Implementation

class Test:
    def testing(self, i, filename, d, lamb, cat, rFile):
        plik = open(rFile, "w",  encoding="utf8")
        for k in lamb:
            for j in d:
                imp = Implementation(k, j, i, filename, cat)
                a = datetime.now()
                r, ae = imp.do_alg()
                b = datetime.now()
                delta = b - a
                plik.write(ae)
                print(ae)
                separator = ' '
                results = separator.join(["wykonania ALS = ", str(i), ", d = ", str(j), ", lambda = ", str(k), ", czas = ", str(delta), "\n\n"])
                plik.write(results)
                print(results)
        plik.close()

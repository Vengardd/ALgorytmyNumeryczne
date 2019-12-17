# KOD: Marta Rybarczyk

from datetime import datetime
from implementation.Implementation import Implementation

class Test:
    def testing(self, i, d, lamb, max_p, filename):
        plik = open(filename, "w", encoding="utf8")
        for k in lamb:
            for j in d:
                imp = Implementation(k, j, i, max_p)
                a = datetime.now()
                result, ae = imp.do_alg()
                b = datetime.now()
                delta = b - a
                print("wykonania ALS = ", i, ", d = ", j, ", lambda = ", k, ", czas = ", delta)
                print(result)
                separator = ' '
                results = separator.join(["wykonania ALS = ", str(i), ", d = ", str(j), ", lambda = ", str(k), ", czas = ", str(delta),"\n\n"])
                plik.write(ae)
                plik.write(results)
        plik.close()

    def testingZB(self, i, d, lamb, max_p, filename):
        plik = open(filename, "w", encoding="utf8")
        for k in lamb:
            for j in d:
                imp = Implementation(k, j, i, max_p)
                result = imp.zb()
                print(result)
                plik.write(str(result))
        plik.close()

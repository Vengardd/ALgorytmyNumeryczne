# KOD: Marta Rybarczyk

from datetime import datetime
from approximation.Parser import parserek
from approximation.Parser import clean
import approximation
import matrix.MyMatrix as mm
import numpy
import approximation.GSown as GSown
import approximation.GS as GS
import approximation.GaussSeidelScipyParse as GSparse

class Test:

    def __init__(self, filename, result, xy1, xy2, tolerance, iterations, name):
        self.result = open(result, 'a', encoding='utf-8')
        self.xy1 = open(xy1, 'a', encoding='utf-8')
        self.xy2 = open(xy2, 'a', encoding='utf-8')
        self.delta = []
        self.array1 = parserek(filename)
        self.array2 = clean(numpy.copy(self.array1).tolist())
        # self.array2 = self.range_clean(self.array1, self.array2)
        self.csi1 = approximation.csi_domi.CSI_domi(self.array1)
        self.csi2 = approximation.csi_domi.CSI_domi(self.array2)
        self.zeros1 = [0 for i in range(0, len(self.csi1.matrix))]
        self.zeros2 = [0 for i in range(0, len(self.csi2.matrix))]
        self.sum = 0
        self.tolerance = tolerance
        self.iterations = iterations
        self.nazwatestu = name

    def gsparse(self):
        # GAUSS-SEIDEL USING SCIPY.SPARSE
        gsparse1 = GSparse.Gauss_seidel_sparse_matrix()
        gsparse2 = GSparse.Gauss_seidel_sparse_matrix()
        a = datetime.now()
        self.csi1.mV(gsparse1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        a = datetime.now()
        self.csi2.mV(gsparse2.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.save()

    def jacobi(self):
        # JACOBI
        a = datetime.now()
        self.csi1.mV(approximation.jacobi.jacobi(self.csi1.matrix, self.csi1.vector, self.zeros1, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        a = datetime.now()
        self.csi2.mV(approximation.jacobi.jacobi(self.csi2.matrix, self.csi2.vector, self.zeros2, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.save()

    def gso(self):
        # GAUSS-SEIDEL OWN SPARSE MATRIX THING
        gso1 = GSown.Gauss_seidel_own()
        gso2 = GSown.Gauss_seidel_own()
        a = datetime.now()
        self.csi1.mV(gso1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        a = datetime.now()
        self.csi2.mV(gso2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.save()

    def gs(self):
        # GAUSS-SEIDEL
        gs1 = GS.GaussSeidel()
        gs2 = GS.GaussSeidel()
        a = datetime.now()
        self.csi1.mV(gs1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        a = datetime.now()
        self.csi2.mV(gs2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, self.tolerance, self.iterations))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.save()

    def pg(self):
        # PARTIAL GAUSS
        pg1 = mm.MyMatrix(self.csi1.matrix, self.zeros1)
        a = datetime.now()
        pg1.gaussPartial()
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csi1.mV(pg1.vector)
        pg2 = mm.MyMatrix(self.csi2.matrix, self.zeros2)
        a = datetime.now()
        pg2.gaussPartial()
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csi2.mV(pg2.vector)
        self.save()

    def save(self):
        self.result.write(self.nazwatestu)
        self.result.write("\n")
        self.result.write(self.delta.__str__())
        self.result.write("\n")
        self.result.write(self.differences().__str__())
        self.result.write("\n")
        self.result.close()
        self.xy1.write(self.csi1.points.__str__())
        self.xy2.write(self.csi2.points.__str__())
        self.xy1.close()
        self.xy2.close()

    def differences(self):
        differenceArrayFromFullAndPartial = [item for item in self.array1 if item not in self.array2]
        suma = 0
        # self.csi1.points.sort()
        # self.csi2.points.sort()
        for i in range(0, len(differenceArrayFromFullAndPartial) - 4):
            x = self.csi1.getFXfromInterpolate(differenceArrayFromFullAndPartial[i][0])
            print(differenceArrayFromFullAndPartial[i][0])
            print(self.csi2.points)
            d = abs(self.csi2.getFXfromInterpolate(differenceArrayFromFullAndPartial[i][0]) - x) / x
            suma += d
        suma /= len(differenceArrayFromFullAndPartial)
        return suma

    def range_clean(self, ref, arr):
        max_x = max(x[0] for x in ref)
        min_x = min(x[0] for x in ref)
        # print(min_x)
        # print(max_x)
        arr = [x for x in arr if min_x <= x[0] <= max_x]
        # print(arr)
        return arr

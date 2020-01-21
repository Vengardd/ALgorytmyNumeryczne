from datetime import datetime
from approximation.Parser import parserek
from approximation.Parser import clean
import approximation
import matrix.MyMatrix as mm
import numpy
import approximation.GSown as GSown
import approximation.GS as GS
import approximation.GaussSeidelScipyParse as GSparse
import approximation.csi_domi
import approximation.jacobi

class Test:

    def __init__(self, filename, result, tolerance, iterations, name):
        self.result = open(result, 'a', encoding='utf-8')
        self.delta = []
        self.fn = filename
        self.array1 = parserek(filename)
        self.array2 = clean(numpy.copy(self.array1).tolist())
        self.csi1 = approximation.csi_domi.CSI_domi(self.array1)
        self.csi2 = approximation.csi_domi.CSI_domi(self.array2)
        self.zeros1 = [0 for i in range(0, len(self.csi1.matrix))]
        self.zeros2 = [0 for i in range(0, len(self.csi2.matrix))]
        self.sum = 0
        self.tolerance = tolerance
        self.iterations = iterations
        self.nazwatestu = name
        self.i = 0

    def gsparse(self):
        # GAUSS-SEIDEL USING SCIPY.SPARSE
        for t in self.tolerance:
            for n in self.iterations:
                gsparse1 = GSparse.Gauss_seidel_sparse_matrix()
                gsparse2 = GSparse.Gauss_seidel_sparse_matrix()
                a = datetime.now()
                self.csi1.mV(gsparse1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                a = datetime.now()
                self.csi2.mV(gsparse2.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                self.save(t, n)

    def jacobi(self):
        # JACOBI
        for t in self.tolerance:
            for n in self.iterations:
                a = datetime.now()
                self.csi1.mV(approximation.jacobi.jacobi(self.csi1.matrix, self.csi1.vector, self.zeros1, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                a = datetime.now()
                self.csi2.mV(approximation.jacobi.jacobi(self.csi2.matrix, self.csi2.vector, self.zeros2, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                self.save(t, n)

    def gso(self):
        # GAUSS-SEIDEL OWN SPARSE MATRIX THING
        for t in self.tolerance:
            for n in self.iterations:
                gso1 = GSown.Gauss_seidel_own()
                gso2 = GSown.Gauss_seidel_own()
                a = datetime.now()
                self.csi1.mV(gso1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                a = datetime.now()
                self.csi2.mV(gso2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                self.save(t, n)

    def gs(self):
        # GAUSS-SEIDEL
        for t in self.tolerance:
            for n in self.iterations:
                gs1 = GS.GaussSeidel()
                gs2 = GS.GaussSeidel()
                a = datetime.now()
                self.csi1.mV(gs1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                a = datetime.now()
                self.csi2.mV(gs2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, t, n))
                b = datetime.now()
                self.delta.append((b - a).__str__())
                self.save(t, n)

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
        self.save(0, 0)

    def save(self, t, n):
        s = self.nazwatestu + " " + self.csi1.matrix.__len__().__str__() + " " + self.fn
        self.result.write(s)
        self.result.write("\n")
        if self.nazwatestu != 'Partial Gauss':
            str = "Liczba iteracji: " + n.__str__() + ", tolerancja: " + t.__str__()
            self.result.write(str)
            self.result.write("\n")
        self.result.write(self.delta.__str__())
        self.result.write("\n")
        self.result.write(self.differences().__str__())
        self.result.write("\n")
        self.result.write("\n")

    def differences(self):
        differenceArrayFromFullAndPartial = [item for item in self.array1 if item not in self.array2]
        suma = 0
        for i in range(0, len(differenceArrayFromFullAndPartial) - 4):
            x = self.csi1.getFXfromInterpolate(differenceArrayFromFullAndPartial[i][0])
            d = abs(self.csi2.getFXfromInterpolate(differenceArrayFromFullAndPartial[i][0]) - x) / x
            suma += d
        suma /= len(differenceArrayFromFullAndPartial)
        return suma

    def range_clean(self, ref, arr):
        max_x = max(x[0] for x in ref)
        min_x = min(x[0] for x in ref)
        arr = [x for x in arr if min_x <= x[0] <= max_x]
        return arr

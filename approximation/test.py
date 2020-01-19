# KOD: Marta Rybarczyk

from datetime import datetime
from approximation.Parser import parserek
from approximation.Parser import clean
import approximation
import matrix.MyMatrix as mm
import numpy
import approximation.GSown as GSown
import approximation.GS as GS

class Test:

    def __init__(self, filename, result):
        self.data = filename
        self.result = result
        self.delta = []
        self.csivalues = []
        self.array1 = parserek(self.data)
        self.array2 = clean(numpy.copy(self.array1).tolist())
        self.array2 = self.range_clean(self.array1, self.array2)
        self.csi1 = approximation.csi_domi.CSI_domi(self.array1)
        self.csi2 = approximation.csi_domi.CSI_domi(self.array2)
        self.zeros1 = [0 for i in range(0, len(self.csi1.matrix))]
        self.zeros2 = [0 for i in range(0, len(self.csi2.matrix))]
        self.sum = 0

    def jacobi(self):
        # JACOBI
        a = datetime.now()
        self.csi1.mV(approximation.jacobi.jacobi(self.csi1.matrix, self.csi1.vector, self.zeros1, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi1.getFXfromInterpolate(-1))
        a = datetime.now()
        self.csi2.mV(approximation.jacobi.jacobi(self.csi2.matrix, self.csi2.vector, self.zeros2, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi2.getFXfromInterpolate(-1))
        print(self.delta)
        print(self.csivalues)

    def gso(self):
        # GAUSS-SEIDEL OWN SPARSE MATRIX THING
        gso1 = GSown.Gauss_seidel_own()
        gso2 = GSown.Gauss_seidel_own()
        a = datetime.now()
        self.csi1.mV(gso1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi1.getFXfromInterpolate(-1))
        a = datetime.now()
        self.csi2.mV(gso2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi2.getFXfromInterpolate(-1))
        print(self.delta)
        print(self.csivalues)

    def gs(self):
        # GAUSS-SEIDEL
        gs1 = GS.GaussSeidel()
        gs2 = GS.GaussSeidel()
        a = datetime.now()
        self.csi1.mV(gs1.asd(self.csi1.matrix, self.csi1.vector, self.zeros1, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi1.getFXfromInterpolate(-1))
        a = datetime.now()
        self.csi2.mV(gs2.asd(self.csi2.matrix, self.csi2.vector, self.zeros2, 0.00001, 1000))
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csivalues.append(self.csi2.getFXfromInterpolate(-1))
        print(self.delta)
        print(self.csivalues)

    def pg(self):
        # PARTIAL GAUSS
        pg1 = mm.MyMatrix(self.csi1.matrix, self.zeros1)
        a = datetime.now()
        pg1.gaussPartial()
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csi1.mV(pg1.vector)
        self.csivalues.append(self.csi1.getFXfromInterpolate(-1))
        pg2 = mm.MyMatrix(self.csi2.matrix, self.zeros2)
        a = datetime.now()
        pg2.gaussPartial()
        b = datetime.now()
        self.delta.append((b - a).__str__())
        self.csi2.mV(pg2.vector)
        self.csivalues.append(self.csi2.getFXfromInterpolate(-1))
        print(self.delta)
        print(self.csivalues)

    def save(self):
        plik = open(self.result, 'w', encoding='utf-8')
        plik.close()

    def differences(self):
        array = []
        suma = 0
        for i in range (1, len(self.csi1.points), 2):
            array.append(self.csi1.points[i])
        for i in range (0, len(array)):
            print(self.csi2.getFXfromInterpolate(array[i][0]))
            print(self.csi1.getFXfromInterpolate(array[i][0]))

    def range_clean(self, ref, arr):
        max_x = max(x[0] for x in ref)
        min_x = min(x[0] for x in ref)
        print(min_x)
        print(max_x)
        arr = [x for x in arr if min_x <= x[0] <= max_x]
        print(arr)
        return arr

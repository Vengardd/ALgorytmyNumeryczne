# KOD: Marta Rybarczyk

from implementation.test import Test

filename50 = "amazon-meta-50.txt"
filename300 = "amazon-meta-300.txt"
filename1800 = "amazon-meta-1800.txt"
names = [filename50, filename300, filename1800]
d = [1, 2, 3, 4, 5]
lamb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
t = Test()
t.testing(5, names, d, lamb)
t.testing(50, names, d, lamb)
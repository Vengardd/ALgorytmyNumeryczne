# KOD: Marta Rybarczyk

from implementation.test import Test

cat = '|Books[283155]'
filename50 = "amazon-meta-50.txt"
filename300 = "amazon-meta-300.txt"
filename1100 = "amazon-meta-1100.txt"
names = [filename50, filename300, filename1100]
d = [1, 2, 3, 4, 5]
lamb = [0.05, 0.1, 0.2]
t = Test()
t.testing(5, names, d, lamb, cat)
t.testing(50, names, d, lamb, cat)
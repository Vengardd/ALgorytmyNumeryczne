# KOD: Marta Rybarczyk

import winsound
from implementation.test import Test

frequency = 1500
duration = 1000

test1 = "test50.txt"
test2 = "smiec.txt"
test22 = "smiec2.txt"
test222 = "smiec3.txt"
test3 = "test1100.txt"

cat = '|Books[283155]'
filename50 = "amazon-meta-50.txt"
filename300 = "amazon-meta-300.txt"
filename1100 = "amazon-meta-1100.txt"
d = [3, 6, 9, 12, 15]
d2 = [3]
lamb = [0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.5]
lamb2 = [0.1]

t = Test()

# Testy pełne
t.testing(20, filename50, d, lamb2, cat, test3)
print("ok")
# t.testing(5, filename50, d, lamb, cat, test22)
# print("ok")
# t.testing(5, filename300, d, lamb, cat, test22)
# print("ok")
# t.testing(5, filename1100, d, lamb, cat, test222)
# print("ok")

# winsound.Beep(frequency, duration)


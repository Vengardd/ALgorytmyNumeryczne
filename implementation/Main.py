# KOD: Marta Rybarczyk
# 50/300/1100
from implementation.test import Test

d1 = [1, 2, 3, 4, 5]
d2 = [6, 12, 18, 24, 30]
d3 = [3]
lamb1 = [0.001, 0.01, 0.1, 0.5, 1]
lamb3 = [0.1]

t = Test()

t.testing(5, d3, lamb3, 50, "test-iteracje-5.txt")
t.testing(20, d3, lamb3, 50, "test-iteracje-20.txt")

t.testing(20, d3, lamb1, 50, "test-stale-d.txt")
t.testing(20, d1, lamb3, 50, "test-stala-lambda.txt")
t.testing(20, d2, lamb3, 50, "test-stala-lambda-2.txt")

t.testing(20, d3, lamb3, 50, "test-czas-50.txt")
t.testing(20, d3, lamb3, 300, "test-czas-300.txt")
t.testing(20, d3, lamb3, 1100, "test-czas-1100.txt")

t.testingZB(50, d3, lamb3, 50, "test-zbieznosc.txt")

# a - input matrix
# b - matrix solution
# t - Tolerance
# IT - max number of iterations
# xo - initial (or one of next) guess (zera?)
import math


def jacobi(a, b, xo, t, IT):
    n = len(b)
    x = [None] * n
    for k in range(0, IT):
        for i in range(0, n):
            x[i] = (1/(a[i][i]))*(getsum(n, i, xo, a, b) + b[i])
        if abs(getnorm(x)-getnorm(xo)) < t:
            return x
        for i in range(0, n):
            xo[i] = x[i]
    return x


def getsum(n, i, xo, a, b):
    sum = 0
    for j in range(0, n):
        if j != i:
            sum += -a[i][j]*xo[j]
    return sum


def getnorm(v):
    sum = 0
    for j in v:
        sum += j*j
    return math.sqrt(sum)

# x_1=2/5
# x_2=(-1)/10
# x_3=3/2

# aa = [[2, 1, 1], [3, 5, 2], [2, 1, 4]]
# bb = [5, 15, 8]
# xo = [1, 1, 1]

aa = [[2, 3, 0, 0], [2, 10, 2, 0], [0, 2, 8, 5], [0, 0, 3, 4]]
bb = [2, 4, 5, 3]

guess1 = jacobi(aa, bb, [0, 0, 0, 0], 0.00001, 1000)
# guess2 = jacobi(aa, bb, guess1, 0.001, 10)
# guess3 = jacobi(aa, bb, guess2, 0.001, 10)

print(guess1)
# print(guess2)
# print(guess3)

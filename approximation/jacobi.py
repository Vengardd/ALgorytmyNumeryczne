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


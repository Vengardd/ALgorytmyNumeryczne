import approximation.test as test

a = test.Test('256_gorzysto.csv', 'result.txt')
# b = test.Test('256_gorzysto.csv', 'result.txt')
# c = test.Test('256_gorzysto.csv', 'result.txt')
# d = test.Test('256_gorzysto.csv', 'result.txt')
a.jacobi()
# b.gs()
# c.gso()
# d.pg()
a.differences()
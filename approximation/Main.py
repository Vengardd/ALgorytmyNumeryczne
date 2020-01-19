import approximation.test as test

names = ['Jacobi', 'Gauss-Seidel', 'Gauss-Seidel own sparse', 'Gauss-Seidel scipy.sparse', 'Partial Gauss']
a = test.Test('256_gorzysto.csv', 'result.txt', 'a1.txt', 'a2.txt', 0.00001, 1000, names[0])
b = test.Test('256_gorzysto.csv', 'result.txt', 'b1.txt', 'b2.txt', 0.00001, 1000, names[1])
c = test.Test('256_gorzysto.csv', 'result.txt', 'c1.txt', 'c2.txt', 0.00001, 1000, names[2])
d = test.Test('256_gorzysto.csv', 'result.txt', 'd1.txt', 'd2.txt', 0.00001, 1000, names[4])
e = test.Test('256_gorzysto.csv', 'result.txt', 'e1.txt', 'e2.txt', 0.00001, 1000, names[3])
a.jacobi()
b.gs()
c.gso()
d.pg()
e.gsparse()
a.differences()
b.differences()
c.differences()
d.differences()
e.differences()
import random
import numpy
from numpy import linalg as LA

# PARSER ########################################################

findingCustomer = 'cutomer: '
findingId = 'Id:   '
findingRates = 'rating: '
findingCategory = '|Books[283155]|Subjects[1000]|Religion & Spirituality[22]|Earth-Based Religions[12472]|Wicca[12484]' # lub jakieś inne; potem można ewentualnie zmienić na wklejanie do inputu
userArray = []
size = 0
plik = open("amazon-meta-small.txt", "r", encoding="utf8")

for line in plik:
    n = line.find(findingCategory)
    n += len(findingCategory)
    if (n != len(findingCategory)-1):
        size += 1
    else:
        pass

plik.seek(0)
lineCounter = 0
for line in plik:
    lineCounter += 1
    a = line.find(findingCategory)
    a += len(findingCategory)
    if (a != len(findingCategory)-1):
        for line in plik:
            b = line.find(findingCustomer)
            b += len(findingCustomer)
            if (b != len(findingCustomer)-1):
                user = ""
                while True:
                    if (line[b+1] == " "):
                        break
                    else:
                        user += line[b]
                    b+=1
                userArray.append(user)
            else:
                n = line.find(findingId)
                if (n != -1):
                    break
                else:
                    pass
        plik.seek(0)
        for foo in range(0, lineCounter):
            plik.readline()
            foo += 1
    else:
        pass

seen = set()
cleanUserArray = []
for item in userArray:
    if item not in seen:
        seen.add(item)
        cleanUserArray.append(item)

# kolumny = users, rzędy = products
ratingsArray = [[0 for i in range (0, len(cleanUserArray))] for i in range (0, size)]

plik.seek(0)

rate = 0
x = 0
y = 0
lineCounter = 0

for line in plik:
    lineCounter += 1
    a = line.find(findingCategory)
    a += len(findingCategory)
    if (a != len(findingCategory)-1):
        for line in plik:
            b = line.find(findingCustomer)
            b += len(findingCustomer)
            if (b != len(findingCustomer) - 1):
                user = ""
                while True:
                    if (line[b + 1] == " "):
                        break
                    else:
                        user += line[b]
                    b += 1
                y = int(cleanUserArray.index(user))
                c = line.find(findingRates)
                c += len(findingRates)
                if (c != len(findingRates) - 1):
                    rate = int(line[c])
                    ratingsArray[x][y] = rate
                else:
                    pass
            else:
                n = line.find(findingId)
                if (n != -1):
                    break
                else:
                    pass
        x += 1
        plik.seek(0)
        for foo in range(0, lineCounter):
            plik.readline()
            foo += 1
    else:
        pass

plik.close()

# f(U, P) #######################################################

lambdaFactor = 0.1
d = 5

uArray = [[random.random() for i in range (0, len(cleanUserArray))] for j in range (0, d)] # dxu
pArray = [[random.random() for i in range (0, size)] for j in range (0, d)] # dxp

uArrayTransposed = numpy.transpose(uArray)
pArray = numpy.array(pArray)

multipliedUP = numpy.matmul(uArrayTransposed, pArray)

sumRUP = 0
sumUU = 0
sumPP = 0
fup = 0
foo = 0

for u in range(0, len(cleanUserArray)):
    for p in range(0, size):
        sumRUP += (ratingsArray[p][u] - multipliedUP[u][p])**2
        sumUU += LA.norm(uArrayTransposed[u])**2
        sumPP += LA.norm(pArray[p])**2
        foo = lambdaFactor * (sumUU + sumPP)
        fup = sumRUP + foo

print(fup)

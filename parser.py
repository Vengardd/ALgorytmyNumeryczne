findingCustomer = 'cutomer: '
findingId = 'Id:   '
findingRates = 'rating: '
userArray = []
plik = open("amazon-meta-small.txt", "r", encoding="utf8")
plik.readline()
plik.read(13)
k=""
while True:
    n = plik.read(1)
    if (n == "\n"):
        break
    else:
        k += n

size = int(k)
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
        pass

seen = set()
cleanUserArray = []
for item in userArray:
    if item not in seen:
        seen.add(item)
        cleanUserArray.append(item)

# kolumny = users, rzędy = products
ratingsArray = [[0 for i in range (0, len(cleanUserArray))] for i in range (0, size)]
plik.close()
plik = open("amazon-meta-small.txt", "r")
rate = 0
x = 0
y = 0
lineCounter = 0
for line in plik:
    lineCounter += 1
    a = line.find(findingId)
    a += len(findingId)
    if (a != len(findingId)-1):
        xx = ""
        while True:
            if (line[a] == "\n"):
                break
            else:
                xx += line[a]
            a += 1
        x = int(xx)
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
        plik.seek(0)
        for foo in range(0, lineCounter):
            plik.readline()
            foo += 1
    else:
        pass

plik.close()
print(ratingsArray)

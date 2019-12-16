# KOD : DOMINIKA CESARZ

import re

import numpy as np


class Parser:
    findingCustomer = 'cutomer: +([A-Z0-9]*)'
    findingId = 'Id: +([0-9]+$)'
    findingRates = 'rating: +([0-9]+)'

    out = [[]]
    id_array = []
    user_array = []
    ratings = []

    size = 0
    lineCounter = 0

    flagId = False
    flagCategory = False
    flagRollback = False

    id = -1
    rating = -1
    customer = None

    def __init__(self, filename, cat):
        self.plik = open(filename, "r", encoding="utf8")
        self.findingCategory = cat

    def append(self, out_temp, id_temp, ratings_temp, user_array_temp, id_array_temp):
        indexproduct = id_array_temp.index(id_temp)
        while len(out_temp) != len(user_array_temp):
            out_temp.append([0])
        for subarray in out_temp:
            while len(subarray) != len(id_array_temp):
                subarray.append(0)
        for i, user in enumerate(user_array_temp, 0):
            for j in ratings_temp:
                if j[0] == user:
                    out_temp[i][indexproduct] = j[1]
        return out_temp

    def getparsed(self):
        for line in self.plik:
            m = re.match(self.findingId, line)
            if m is not None and not self.flagId:
                if self.flagRollback:
                    if not self.ratings:
                        self.id_array.remove(self.id)
                    else:
                        self.out = self.append(self.out, self.id, self.ratings, self.user_array, self.id_array)
                    self.ratings = []
                    self.flagRollback = False
                self.id = int(m.group(1))
                self.flagId = True
                self.flagCategory = False
            elif self.flagId:
                m = re.search(self.findingCategory, line)
                if m is not None and self.id != -1:
                    self.id_array.append(self.id)
                    self.flagCategory = True
                    self.flagId = False
            elif self.flagCategory:
                m = re.search(self.findingRates, line)
                if m is not None:
                    rating = int(m.group(1))
                    m = re.search(self.findingCustomer, line)
                    if m is not None:
                        customer = m.group(1)
                        self.ratings.append([customer, rating])
                        if customer not in self.user_array:
                            self.user_array.append(customer)
                    self.flagRollback = True
        self.out = np.asarray(self.out)
        self.plik.close()
        self.out = np.delete(self.out, 0, 1)
        return self.out, self.id_array

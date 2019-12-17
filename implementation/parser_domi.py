# KOD : DOMINIKA CESARZ

import re
from operator import itemgetter

import numpy as np


class Parser:
    findingCustomer = 'cutomer: +([A-Z0-9]*)'
    findingId = 'Id: +([0-9]+$)'
    findingRates = 'rating: +([0-9]+)'

    out = [[]]
    id_array = []
    user_array = []
    ratings = []
    ratings_all = []

    size = 0
    lineCounter = 0

    flagId = False
    flagCategory = False
    # flagRollback = False

    id = -1
    rating = -1
    customer = None

    def __init__(self, filename, cat, user_min, user_max):
        self.plik = open(filename, "r", encoding="utf8")
        self.findingCategory = cat
        self.user_min = user_min
        self.user_max = user_max

    # def append(self, out_temp, id_temp, ratings_temp, user_array_temp, id_array_temp):
    #     indexproduct = id_array_temp.index(id_temp)
    #     while len(out_temp) != len(user_array_temp):
    #         out_temp.append([0])
    #     for subarray in out_temp:
    #         while len(subarray) != len(id_array_temp):
    #             subarray.append(0)
    #     for i, user in enumerate(user_array_temp, 0):
    #         for j in ratings_temp:
    #             if j[0] == user:
    #                 out_temp[i][indexproduct] = j[1]
    #     return out_temp

    def optimize(self, ratings_list, user_list, user_min, user_max):
        l = len(user_list)
        for i in range(0, l):
            user_list[i].append(0)
            for j in ratings_list:
                if user_list[i][0] == j[1]:
                    user_list[i][1] += 1
        user_list = sorted(user_list, key=itemgetter(1))
        for i in range(user_min, user_max):
            temp_user = user_list[-i:-1]
            lr = len(ratings_list)
            users_list_new = []
            id_list_new = []
            new_rating_list = []
            for j in range(0, lr):
                for k in range(0, i):
                    if ratings_list[j][1] == temp_user[k][0]:
                        new_rating_list.append(ratings_list[j])
                        if ratings_list[j][1] not in users_list_new:
                            users_list_new.append(ratings_list[j][1])
                        if ratings_list[j][0] not in id_list_new:
                            id_list_new.append(ratings_list[j][0])
            if len(users_list_new) <= len(id_list_new):
                return new_rating_list, users_list_new, id_list_new
        return -1

    # ten kod jest tak brzydki ze nie moge

    def create_r(self, ratings_list, ul, idl):
        h = len(ul)
        w = len(idl)
        out_temp = np.zeros((h, w))
        for i in ul:
            for j in idl:
                for r in ratings_list:
                    if r[0] == j and r[1] == i:
                        out_temp[i][j] = r[2]
        return out_temp

    def getparsed(self):
        for line in self.plik:
            m = re.match(self.findingId, line)
            if m is not None:
                # if self.flagRollback:
                #     # if not self.ratings:
                #     #     self.id_array.remove(self.id)
                #     # # else:
                #     # #     self.out = self.append(self.out, self.id, self.ratings, self.user_array, self.id_array)
                #     self.ratings = []
                #     self.flagRollback = False
                self.id = int(m.group(1))
                print(self.id)
                self.flagId = True
                self.flagCategory = False
            elif self.flagId:
                m = re.search(self.findingCategory, line)
                if m is not None and self.id != -1:
                    # self.id_array.append(self.id)
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
                        self.ratings_all.append([self.id, customer, rating])
                        if customer not in self.user_array:
                            self.user_array.append(customer)
                    # self.flagRollback = True
        self.plik.close()
        print(self.ratings_all)
        r, u, p = self.optimize(self.ratings_all, self.user_array, self.user_min, self.user_max)
        if r != -1:
            self.out = self.create_r(r, u, p)
            self.out = np.asarray(self.out)
            return self.out
        else:
            return -1


p = Parser('amazon-meta-1100.txt', 'Books[283155]', 10, 100)
r = p.getparsed()
print(r)
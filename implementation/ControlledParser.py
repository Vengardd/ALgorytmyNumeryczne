import csv
import re
import numpy as np
from implementation.RatingDto import RatingDto


class ControlledParser:

    def parse(self):
        self.parseToNewFile()
        self.parseFromNewFile()

    def parseToNewFile(self, maxProducts):
        s = 0
        id = 0
        list = []
        valid_group = False
        reviews_count = 0
        for line in open('amazon-meta.txt', encoding="utf8"):
            match_id = re.search('Id:   (\d+)', line)
            if match_id != None:
                id = match_id.group(1)
                continue
            match_group = re.search('group:[ ]+[A-z]+', line)
            if match_group != None:
                if match_group.group() == 'group: Book':
                    valid_group = True
                else:
                    valid_group = False
            if valid_group:
                match_reviews_count = re.search('total:[ ]+([0-9]+)', line)
                if match_reviews_count != None:
                    reviews_count = int(match_reviews_count.group(1))
            match_customer = re.search('cutomer:[ ]+([A-Za-z]+[\d@]+[\w@]*)', line)
            match_rating = re.search('rating:[ ]+([0-9])', line)
            # if match_reviews_count != None and int(match_reviews_count.group(1)) > 20 :
            #     print(match_reviews_count.group(1))
            #     s+=1
            # if s>20:
            #     break
            if match_customer != None and valid_group:
                if reviews_count > 20:
                    list.append([id, match_customer.group(1), match_rating.group(1)])
                    s += 1
            else:
                continue
            if s > maxProducts:
                break
        with open('testBook.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list)

    def parseFromNewFile(self):
        with open('testbook.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            usersCount = {}
            productsCount = {}
            allUserCount = 0
            allProductCount = 0
            ratingDtos = []
            for row in csv_reader:
                ratingDtos.append(RatingDto(row[1], row[0], row[2]))
                if row[0] in productsCount:
                    productsCount[row[0]] = productsCount[row[0]] + 1
                else:
                    productsCount[row[0]] = 1
                    allProductCount += 1
                if row[1] in usersCount:
                    usersCount[row[1]] = usersCount[row[1]] + 1
                else:
                    usersCount[row[1]] = 1
                    allUserCount += 1
            sortedProducts = sorted(productsCount, key=productsCount.get, reverse=True)
            sortedUsers = sorted(usersCount, key=usersCount.get, reverse=True)

            matrix = []
            for i in range(0, allUserCount):
                matrix.append([])
                for j in range(0, allProductCount):
                    matrix[i].append(0)

            for dto in ratingDtos:
                productIndex = sortedProducts.index(dto.product)
                userIndex = sortedUsers.index(dto.user)
                matrix[userIndex][productIndex] = dto.rating
            matrix = np.asfarray(matrix, float)
            return matrix

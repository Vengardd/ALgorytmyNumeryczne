# https://google-developers.appspot.com/maps/documentation/javascript/examples/elevation-paths?fbclid=IwAR1aoYmvwJlAaSxU77leHBUJAdb-VT_cSkVr2Z3G6A5VsSEip3aA9qWFZtg
import geopy.distance
import re

def parserek(filename):
    tablica = []
    plik = open(filename, 'r', encoding='utf-8')
    for line in plik:
        tablica.append(re.split(",", line))
    coords_1 = [0 for i in range (0, len(tablica))]
    coords_2 = [0 for i in range (0, len(tablica))]
    elevation = [0 for i in range (0, len(tablica))]
    for i in range(0, len(tablica)):
        coords_1[i] = float(tablica[i][0])
        coords_2[i] = float(tablica[i][1])
        elevation[i] = float(tablica[i][2].rstrip())
    kolejnatablica = [0 for i in range (0, len(coords_2))]
    for i in range(0, len(coords_1)):
        kolejnatablica[i] = abs(geopy.distance.distance((coords_1[0], coords_2[0]), ((coords_1[i], coords_2[i]))).km)
    ostatnia = [[0 for i in range(0, 2)] for j in range(0, len(elevation))]
    for i in range(0, len(elevation)):
        ostatnia[i][0] = kolejnatablica[i]
        ostatnia[i][1] = elevation[i]
    plik.close()
    return ostatnia

def clean(arrayToCopyFrom):
    cleaned = []
    for i in range(1, len(arrayToCopyFrom) - 3):
        if i % 2 == 0:
            cleaned.append(arrayToCopyFrom[i])
    return cleaned
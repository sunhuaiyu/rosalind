# rosalind_ba8b

import numpy as np
from scipy.spatial.distance import euclidean

def dist_point_centers(data_point, centers):
    all_dist = [euclidean(data_point, i) for i in centers]
    return min(all_dist)

def squared_error_distortion(data, centers):
    all_dist_squared = [dist_point_centers(p, centers) ** 2 for p in data]
    return round(np.mean(all_dist_squared), 3)

f = open('rosalind_ba8b.txt')
k, m = [int(i) for i in f.readline().rstrip().split()]

centers = []
line = f.readline().rstrip().split()
while line[0][0] != '-':
    centers.append(np.array(line, float))
    line = f.readline().rstrip().split()

data = []
line = f.readline().rstrip().split()
while line:
    data.append(np.array(line, float))
    line = f.readline().rstrip().split()

print(squared_error_distortion(data, centers))
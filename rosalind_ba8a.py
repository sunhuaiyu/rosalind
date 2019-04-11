# rosalind_ba8a

import numpy as np
from scipy.spatial.distance import euclidean

def dist_point_centers(data_point, centers):
    all_dist = [euclidean(data_point, i) for i in centers]
    return min(all_dist)

def max_distance_point(data, centers):
    all_dist = [dist_point_centers(p, centers) for p in data]
    return np.argmax(all_dist)

def farthest_first(data, k):
    i = 0 #np.random.randint(k)
    centers = [data[i]]
    while len(centers) < k:
        data_point = data[max_distance_point(data, centers)]        
        centers.append(data_point)
    return centers

f = open('rosalind_ba8a.txt')
k, m = [int(i) for i in f.readline().rstrip().split()]
data = np.fromfile(f, sep=' ').reshape(-1, m)

result = '\n'.join([' '.join([str(round(i, 1)) for i in row]) 
                for row in farthest_first(data, k)])
print(result)
open('rosalind_ba8a_sub.txt', 'wt').write(result)
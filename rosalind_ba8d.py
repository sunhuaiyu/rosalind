# rosalind_ba8d
import numpy as np
from scipy.spatial.distance import cdist

def hidden_matrix(data, centers, b):
    m = np.exp(- b * cdist(centers, data))
    return m / m.sum(0)

def soft_kmeans(data, k, beta):
    centers = data[:k]
    for i in range(100):
        hm = hidden_matrix(data, centers, beta)
        centers = (hm.dot(data).T / hm.sum(1)).T
    return centers

f = open('rosalind_ba8d.txt')
k, m = [int(i) for i in f.readline().rstrip().split()]
beta = float(f.readline().rstrip())
data = np.fromfile(f, sep=' ').reshape(-1, m)

result = '\n'.join([' '.join([str(round(i, 3)) for i in row]) 
                for row in soft_kmeans(data, k, beta)])
print(result)
open('rosalind_ba8d_sub.txt', 'wt').write(result)
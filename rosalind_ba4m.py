#rosalind_ba4m
'''
Turnpike Problem: Given all pairwise distances between points on a line segment, 
reconstruct the positions of those points.

Given: A collection of integers L.
Return: A set A such that ∆A = L
'''

from collections import Counter
result = []    

def place(L, X, width):
    if L == []:
        result.append(sorted(X))
        return
    
    y = max(L)

    diff_y_X = [abs(y - i) for i in X]
    if Counter(diff_y_X) == (Counter(diff_y_X) & Counter(L)):
        X.append(y)
        for i in diff_y_X:
            L.remove(i)
        place(L, X, width)
        X.remove(y)
        for i in diff_y_X:
            L.append(i)
    
    diff_w_y_X = [abs(width - y - i) for i in X]
    if Counter(diff_w_y_X) == (Counter(diff_w_y_X) & Counter(L)):
        X.append(width - y)
        for i in diff_w_y_X:
            L.remove(i)
        place(L, X, width)
        X.remove(width - y)
        for i in diff_w_y_X:
            L.append(i)
    
    return
        

def partial_digest(L):
    width = max(L)
    L.remove(width)
    X = [0, width]
    place(L, X, width)
    return


L = [int(i) for i in open('rosalind_ba4m.txt').readline().split()]
partial_digest([i for i in L if i > 0])

open('rosalind_ba4m_sub.txt', 'wt').write(' '.join([str(i) for i in result[0]]))



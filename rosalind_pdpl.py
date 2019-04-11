#rosalind_pdpl
'''
Given: A multiset L containing comb(n, 2) positive integers for some positive integer n.
Return: A set X containing n nonnegative integers such that ΔX = L.
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


L = [int(i) for i in open('rosalind_pdpl.txt').readline().split()]
partial_digest(L)

open('rosalind_pdpl_sub.txt', 'wt').write(' '.join([str(i) for i in result[0]]))



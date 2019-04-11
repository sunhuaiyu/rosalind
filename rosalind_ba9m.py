#rosalind_ba9m
'''
Implement BetterBWMatching
Given: A string BWT(Text), followed by a collection of strings Patterns.
Return: A list of integers, where the i-th integer corresponds to the 
number of substring matches of the i-th member of Patterns in Text.
'''

import numpy as np

def first_occurence(last_column):
    return dict(zip(*np.unique(sorted(last_column), return_index=True)))

# alternatively; for DNA string
def first_occurence(last_column):
    first_column = sorted(last_column)
    return {i:first_column.index(i) for i in '$ACGT'}

def count(c, i, last_column):
    return last_column[:i].count(c)

def betterBWTmatching(last_column, pattern):
    top = 0
    bottom = len(last_column) - 1
    firsts = first_occurence(last_column)

    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in last_column[top:bottom+1]:
                top = firsts[symbol] + count(symbol, top, last_column)
                bottom = firsts[symbol] + count(symbol, bottom+1, last_column) - 1
            else:
                return 0
        else:
            return bottom - top + 1

   
f = open('rosalind_ba9m.txt')
s = f.readline().rstrip()
patterns = f.readline().rstrip().split()

result = ' '.join([str(betterBWTmatching(s, p)) for p in patterns])

print(result)
open('rosalind_ba9m_sub.txt', 'wt').write(result)


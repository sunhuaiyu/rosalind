#rosalind_ba9n
'''
Multiple Pattern Matching Problem:
Find all occurrences of a collection of patterns in a text.

Given: A string Text and a collection of strings Patterns.
Return: All starting positions in Text where a string from Patterns appears as a substring.
'''
#Use a new version of Python regex
import regex as re

f = open('rosalind_ba9n.txt')
s = f.readline().rstrip()
patterns = '|'.join(f.read().rstrip().split())

result = [m.start() for m in re.finditer(patterns, s, overlapped=True)]
open('rosalind_ba9n_sub.txt', 'wt').write(('{} '*len(result)).format(*result))


''' 
# I used this naive pattern matching to solve the problem, thus did not actually solve it.
  
def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

f = open('rosalind_ba9n.txt')
s = f.readline().rstrip()
patterns = [i.rstrip() for i in f.readlines()]

result = []
for i in suffix_array(s):
    for p in patterns:
        if s[i:][:len(p)] == p:
            result.append(str(i))

open('rosalind_ba9n_sub.txt', 'wt').write(' '.join(result))
'''


import numpy as np

def partial_suffix_array(s, k):
    '''partial suffix array without indices'''
    return sorted(range(0, len(s), k), key=lambda i: s[i:])

def first_occurence(last_column):
    return dict(zip(*np.unique(sorted(last_column), return_index=True)))

def count(symbol, i, last_column):
    return last_column[:i].count(symbol)

def checkpoint_array(last_column, k):
    a = {i:[] for i in '$ACGT'}
    for i in range(k, len(last_column), k):
        for c in '$ACGT':
            a[c].append(last_column[:i].count(c))
    return a

def bwt(t):
    '''BWT transformation; return last column.'''
    return ''.join([j[-1] for j in sorted([t[i:] + t[:i] for i in range(len(t))])])

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


f = open('rosalind_ba9n.txt')
s = f.readline().rstrip()
patterns = f.read().rstrip().split()

result = ' '.join([str(betterBWTmatching(bwt(s), p)) for p in patterns])

print(result)
open('rosalind_ba9n_sub.txt', 'wt').write(result)


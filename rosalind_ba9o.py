#rosalind_ba9o
'''
Multiple Approximate Pattern Matching Problem:
Find all approximate occurrences of a collection of patterns in a text.

Given: A string Text, a collection of strings Patterns, and an integer d.

Return: All positions in Text where a string from Patterns appears as a 
substring with at most d mismatches.

'''
#Use a new version of Python regex
import regex as re

f = open('rosalind_ba9o.txt')
s = f.readline().rstrip()
patterns = f.readline().rstrip().split()
d = f.readline().rstrip()
patterns = ['(' + i + ')' + '{s<=' + d + '}' for i in patterns]

result = []

for p in patterns:
    result += [m.start() for m in re.finditer(p, s, overlapped=True)]

result = sorted(result)
open('rosalind_ba9o_sub.txt', 'wt').write(('{} '*len(result)).format(*result))


#rosalind_ba9b
'''
Implement TrieMatching

Given: A string Text and a collection of strings Patterns.

Return: All starting positions in Text where a string from Patterns appears 
as a substring.

'''
#Use a new version of Python regex
import regex as re

f = open('rosalind_ba9b.txt')
s = f.readline().rstrip()
patterns = '|'.join(f.read().rstrip().split())

result = [m.start() for m in re.finditer(patterns, s, overlapped=True)]
open('rosalind_ba9b_sub.txt', 'wt').write(('{} '*len(result)).format(*result))


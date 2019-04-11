# rosalind_ba1l
'''
Convert a DNA string to a number.
Given: A DNA string Pattern.
Return: PatternToNumber(Pattern).
'''

d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

f = open('rosalind_ba1l.txt')
s = f.readline().rstrip()

s = s[::-1]
n = 0
for i in range(len(s)):
    n += d[s[i]] * 4 ** i
print(n)




def permutation_to_lexicographic_ix(p):
    """
    Return the lexicographic index of the permutation `p` among all
    permutations of its elements. `p` must be a sequence and all elements
    of `p` must be distinct.
    """
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result

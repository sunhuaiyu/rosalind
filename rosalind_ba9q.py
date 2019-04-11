#rosalind_ba9q

def partial_suffix_array2(s, k):
    '''partial suffix array without indices'''
    return sorted(range(0, len(s), k), key=lambda i: s[i:])

def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def partial_suffix_array(s, k):
    return [(i, a) for i, a in enumerate(suffix_array(s)) if a % k == 0]
    
f = open('rosalind_ba9q.txt')
s = f.readline().rstrip()
k = int(f.readline().rstrip())

result = '\n'.join([str(i)[1:-1].replace(' ', '') for i in partial_suffix_array(s, k)])
open('rosalind_ba9q_sub.txt', 'wt').write(result)
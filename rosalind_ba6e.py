#rosalind_ba6e
from collections import defaultdict

def revc2(sequence):
    '''translate ACGT to TGCA based on ASCII code; return reversed sequence'''
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]


f = open('rosalind_ba6e.txt')

k = int(f.readline().rstrip())
s1 = f.readline().rstrip()
n1 = len(s1)
s2 = f.readline().rstrip()
n2 = len(s2)

'''
s1_kmers = dict()
for i in range(n1 - k + 1):
    s1_kmers[s1[i:i+k]] = i
 
result = set()   
for i in range(n2 - k + 1):
    s2kmer = s2[i:i+k]
    s2kmer_revc = revc2(s2kmer)
    if s2kmer in s1_kmers:
        result.add(str((s1_kmers[s2kmer], i)))
    if s2kmer_revc in s1_kmers:
        result.add(str((s1_kmers[revc2(s2kmer)], i)))
'''
s1_kmers = defaultdict(list)
for i in range(n1 - k + 1):
    s1_kmers[s1[i:i+k]].append(i)
 
result = set()   
for i in range(n2 - k + 1):
    s2kmer = s2[i:i+k]
    for j in s1_kmers[s2kmer] + s1_kmers[revc2(s2kmer)]:
        result.add(str((j, i)))

result = '\n'.join(result)
print(result)
open('rosalind_ba6e_sub.txt', 'wt').write(result)


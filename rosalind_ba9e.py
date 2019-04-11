#rosalind_ba9e
def revc2(sequence):
    '''translate ACGT to TGCA based on ASCII code; return reversed sequence'''
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]

def shared_kmers(k, s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    s1_kmers = dict()
    for i in range(n1 - k + 1):
        s1_kmers[s1[i:i+k]] = i
 
    result = set()   
    for i in range(n2 - k + 1):
        s2kmer = s2[i:i+k]
        if s2kmer in s1_kmers:
            result.add(s1_kmers[s2kmer])

    return list(result)

f = open('rosalind_ba9e.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()

k = min(len(s), len(t))
shared = shared_kmers(k, s, t) 
while shared == []:
    k -= 1
    shared = shared_kmers(k, s, t)

i = shared[0]
print(s[i:i+k])

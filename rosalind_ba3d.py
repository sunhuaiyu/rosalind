#rosalind_ba3d

def revc2(sequence):
    '''translate ACGT to TGCA based on ASCII code; return reversed sequence'''
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]

def all_kmers(seq, k): 
	'''return the k-mer composition of a string'''
	return [seq[i:i+k] for i in range(len(seq) - k + 1)]

f = open('rosalind_ba3d.txt')
k = int(f.readline().rstrip())
s = f.readline().rstrip()

d = dict()
for i in all_kmers(s, k):
    a, b = i[:-1], i[1:]
    if a in d.keys():
        d[a].add(b)
    else:
        d[a] = {b}

result = []
for i in sorted(d.keys()):
    result.append(str(i) + ' -> ' + ','.join(sorted(list(d[i]))))

result = '\n'.join(result)
print(result)
open('rosalind_ba3d_sub.txt', 'wt').write(result)


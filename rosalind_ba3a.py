# rosalind_ba3a
# all k-mers

f = open('rosalind_ba3a.txt')
k = int(f.readline().rstrip())
seq = f.readline().rstrip()


result = [seq[i:i+k] for i in range(len(seq) - k + 1)]

open('rosalind_ba3a_sub.txt', 'wt').write('\n'.join(result))




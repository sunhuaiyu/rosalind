#rosalind_ba3l

f = open('rosalind_ba3l.txt')
k, d = [int(i) for i in f.readline().rstrip().split()]
reads = [i.rstrip() for i in f]

seq = [i[0] for i in reads] + [i[-1] for i in reads[-2 * k - d + 1:]]
open('rosalind_ba3l_sub.txt', 'wt').write(''.join(seq))
    

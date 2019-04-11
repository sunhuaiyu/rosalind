# rosalind_ba11a

from itertools import combinations

mass_aa = {71: 'A', 103: 'C', 129: 'E', 115: 'D', 57: 'G', 147: 'F', 
 113: 'I', 137: 'H', 128: 'K', 131: 'M', 114: 'N', 97: 'P', 87: 'S', 
 156: 'R', 101: 'T', 186: 'W', 99: 'V', 163: 'Y', 4: 'X', 5: 'Z'}


spec = sorted([int(i) for i in 
              open('rosalind_ba11a.txt').readline().rstrip().split()] 
              + [0])
n = len(spec)

result = []
for i in range(n):
    for j in range(i+1, n):
        d = spec[j] - spec[i]
        if (spec[j] - spec[i]) in mass_aa.keys():
            result.append(str(spec[i]) + '->' + str(spec[j]) + ':' + mass_aa[d])

print('\n'.join(result))
open('rosalind_ba11a_sub.txt', 'wt').write('\n'.join(result))




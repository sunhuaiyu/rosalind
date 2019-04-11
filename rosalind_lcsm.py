# Huaiyu Sun
# LCSM

from multiprocessing import Pool

def substring(sequence):
    a = set()
    for length in range(1, len(sequence) + 1):
        for i in range(len(sequence)-length+1):
            a.add(sequence[i:i+length])
    return a

frame = dict()
sequence = ''
for l in open('rosalind_lcsm.txt'):
    line = l.rstrip()       
    if line[0] == '>': 
        name = line 
        frame[name] = ''        
    else:
        frame[name] += line
        
p = Pool(16)
common_substring = reduce(lambda x, y: x & y, p.map(substring, frame.values()))
common_substring = list(common_substring)
common_substring.sort(key=len)

open('rosalind_lcsm_ans.txt', 'wt').write(common_substring[-1])

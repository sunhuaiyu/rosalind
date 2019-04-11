# sun.huaiyu
# 1d

f = open('rosalind_1d.txt')
genome = f.readline().rstrip()
k, L, t = map(int, f.readline().split())
f.close()

kmers = dict()
for i in range(len(genome) - k):
    motif = genome[i:i+k]
    if motif in kmers:
        kmers[motif].append(i)
    else:
        kmers[motif] = [i]

kmers = {i:kmers[i] for i in kmers.keys() if len(kmers[i]) >= t}

lumps = set()
for i in kmers.keys():
    print i, kmers[i]
    for j in range(len(kmers[i]) - t + 1):
        window =  kmers[i][j:j + t]
        print window
        if (window[-1] - window[0] + 1) <= L:
            lumps.add(i)  

f = open('rosalind_1d_ans.txt', 'wt')
f.write(' '.join(lumps))
f.close()


# sun.huaiyu
# SUBS
def motif_search(sequence, motif):
    index_found = []
    n = len(motif)
    for i in range(len(sequence)):
        if sequence[i:i+n] == motif:
            index_found.append(i + 1)
    return index_found

f = open('rosalind_subs.txt')
seq = f.readline().rstrip()
m = f.readline().rstrip()

indices = motif_search(seq, m)
for i in indices:
    print i,

# sun.huaiyu
# MPRT
import re, urllib

uniprot = 'http://www.uniprot.org/uniprot/'

proteins = []
for i in open('rosalind_mprt.txt'):
    proteins.append(i.rstrip())

motif = 'N[^P][ST][^P]'
answer = open('rosalind_mprt_ans.txt', 'wt')
for id in proteins:
    sequence = ''
    for ln in urllib.urlopen(uniprot + id + '.fasta'):
        line = ln.rstrip()       
        if line[0] != '>': 
            sequence += line
    if re.search(motif, sequence) != None:
        answer.write(id + '\n')
        for i in range(len(sequence)):
            if re.match(motif, sequence[i:]):
                answer.write(str(i + 1) + ' ')
        answer.write('\n')
answer.close()

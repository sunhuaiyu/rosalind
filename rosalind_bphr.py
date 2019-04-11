#rosalind_bphr

from Bio import SeqIO
import numpy as np

f = open('rosalind_bphr.txt')
header = f.readline().rstrip()
q = int(header)

fq = SeqIO.parse(f, 'fastq')
m = np.array([i.letter_annotations['phred_quality'] for i in fq])

print(sum(m.mean(0) < q))




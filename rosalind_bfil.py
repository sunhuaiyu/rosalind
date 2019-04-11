#rosalind_bfil

from Bio import SeqIO
import numpy as np

f = open('rosalind_bfil.txt')
header = f.readline().rstrip()
q = int(header)

m = [i for i in SeqIO.parse(f, 'fastq')]

for i in range(len(m)):
    while m[i].letter_annotations['phred_quality'][0] < q:
        m[i] = m[i][1:]
    while m[i].letter_annotations['phred_quality'][-1] < q:
        m[i] = m[i][:-1]

SeqIO.write(m, open('rosalind_bfil_sub.txt', 'wt'), 'fastq')

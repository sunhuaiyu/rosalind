#rosalind_filt

from Bio import SeqIO

f = open('rosalind_filt.txt')

header = f.readline().rstrip().split()
n, p = int(header[0]), int(header[1])

fq = SeqIO.parse(f, 'fastq')

k = sum([sum([j >= n for j in i.letter_annotations['phred_quality']]) >= len(i) * p/100
               for i in fq])
print(k)



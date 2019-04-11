# sun.huaiyu
# gbk

from Bio import SeqIO

f = open('rosalind_tfsq.txt')
record = SeqIO.parse(f, 'fastq')
c = open('rosalind_tfsq_ans.txt', 'wt')
count = SeqIO.write(record, c, 'fasta')
c.close()
f.close()
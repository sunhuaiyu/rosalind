# sun.huaiyu
# gbk

from Bio import Entrez, SeqIO
Entrez.email = 'hsun@salk.edu'

f = open('rosalind_frmt.txt')
ids = f.readline().split()

handle = Entrez.efetch(db='nucleotide', id=[', '.join(ids)], rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))

shortest = sorted(records, key=lambda x: len(x.seq))[0]
f = open('rosalind_frmt_ans.txt', 'wt')
f.write(shortest.format('fasta'))
f.close()

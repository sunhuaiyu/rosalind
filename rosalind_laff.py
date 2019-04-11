#rosalind_laff

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO

# pairwise2 would be too slow for the length of sequences
matrix = MatrixInfo.blosum62
s, t = [i.seq for i in SeqIO.parse('rosalind_laff.txt', 'fasta')]
aln = pairwise2.align.localds(s, t, matrix, -11, -1, one_alignment_only=1)
a, b, score, i, j = aln[0]
open('rosalind_laff_sub.txt', 'wt').write('\n'.join([str(int(score)), 
                      a[i:j].replace('-', ''), b[i:j].replace('-', '')]))
# too slow


### use linux server with EMBOSS pairwise alignment programs installed
from Bio import SeqIO
from Bio.Emboss.Applications import NeedleCommandline
from Bio import AlignIO 

seqfiles = []
for i in SeqIO.parse('rosalind_laff.txt', 'fasta'):
    seq_file = i.id + '.txt'
    SeqIO.write(i, seq_file, 'fasta')
    seqfiles.append(seq_file)

needle_cline = NeedleCommandline(asequence=seqfiles[0], bsequence=seqfiles[1],
                                 gapopen=11, gapextend=1, outfile="needle.txt")
needle_cline()

aln = AlignIO.read('needle.txt', "emboss")
a, b = [str(i.seq) for i in aln]

# need to find the score in needle output file 'needle.txt'
for ln in open('needle.txt'):
    if 'Score' in ln:
        print(ln)
        score = int(float(ln.rstrip().split()[-1]))
        break

open('rosalind_laff_sub.txt', 'wt').write('\n'.join([str(int(score)), 
                      a.replace('-', ''), b.replace('-', '')]))

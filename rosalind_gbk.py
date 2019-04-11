# sun.huaiyu
# gbk

from Bio import Entrez
Entrez.email = 'hsun@salk.edu'

f = open('rosalind_gbk.txt')
organism = f.readline().rstrip()
pdat1 = f.readline().rstrip()
pdat2 = f.readline().rstrip()

handle = Entrez.esearch(db='nucleotide', 
     term='"' + organism + '"[Organism] AND ("' + pdat1 + 
          '"[PDAT] : "' + pdat2 + '"[PDAT])' )
record = Entrez.read(handle)
print record['Count']

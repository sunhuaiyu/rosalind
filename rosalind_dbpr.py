# sun.huaiyu
# DBPR
import urllib

uniprot = 'http://www.uniprot.org/uniprot/'

f = open('rosalind_dbpr.txt')
id = f.readline().rstrip()
f.close()

p = []
for ln in urllib.urlopen(uniprot + id + '.txt'):
    line = ln.rstrip().split('   ')
    if line[0] == 'DR':
        go = line[1].split('; ')
        if go[0] == 'GO' and go[2][:2] == 'P:':      
            p.append(go[2][2:])

f = open('rosalind_dbpr_ans.txt', 'wt')
f.write('\n'.join(p))
f.close()

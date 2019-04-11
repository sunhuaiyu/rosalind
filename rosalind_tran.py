# rosalind_tran
# transition/transversion

s1 = ''' '''
s2 = ''' '''

s1 = s1.replace('\n', '')
s2 = s2.replace('\n', '')

transitions = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]
transversions = [('A', 'T'), ('T', 'A'), ('A', 'C'), ('C', 'A'), 
                 ('G', 'C'), ('C', 'G'), ('G', 'T'), ('T', 'G')]

ts = 0
tv = 0
for pair in zip(s1, s2):
    if pair in transitions:
        ts += 1
    elif pair in transversions:
        tv += 1

print(ts/tv)

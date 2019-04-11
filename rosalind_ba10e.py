# rosalind_ba10e
'''
Profile HMM Problem

Given: A threshold θ, followed by an alphabet Σ, followed by a multiple alignment 
Alignment whose strings are formed from Σ.

Return: The transition and emission probabilities of the profile HMM HMM(Alignment, θ).
'''
import numpy as np
from pandas import DataFrame
from io import StringIO

def hmm_build(alphabet, aln, threshold):
    '''given alphabet, multiple alignment aln, and insertion threshold,
    return the profile HMM transition and emission matrix.'''
    
    aln_cols = list(zip(*(aln)))
    m, n = len(aln), len(aln_cols)       # m sequences, n columns

    # indices of columns where '-' count is below threshold
    match_cols = [i for i in range(n) if aln_cols[i].count('-') / m < threshold]

    # state names
    k = len(match_cols)   # k states
    states_ = [('M'+ str(i), 'D' + str(i), 'I' + str(i)) for i in range(1, k + 1)]
    states = ['S', 'I0'] + [i for j in states_ for i in j] + ['E']

    # building matrices
    transitions = DataFrame(data=0.0, columns=states, index=states)
    emissions = DataFrame(data=0.0, columns=alphabet, index=states) 

    for seq in aln:  # iterate through each sequence
        state_ix = 0
        last_state = 'S'
        for i in range(n):
            if i in match_cols:
                state_ix += 1
                if seq[i] != '-':
                    current_state = 'M' + str(state_ix)
                    emissions.loc[current_state, seq[i]] += 1
                else:
                    current_state = 'D' + str(state_ix)
                
                transitions.loc[last_state, current_state] += 1
                last_state = current_state
            
            elif seq[i] != '-':
                current_state = 'I' + str(state_ix)
                transitions.loc[last_state, current_state] += 1
                emissions.loc[current_state, seq[i]] += 1
                last_state = current_state
                            
        transitions.loc[last_state, 'E'] += 1

    # normalize rows
    transitions = transitions.div(transitions.sum(1) + 1e-10, axis=0).round(3)
    emissions = emissions.div(emissions.sum(1) + 1e-10, axis=0).round(3)

    return transitions, emissions

f = open('rosalind_ba10e.txt')
T = float(f.readline().rstrip())   #threshold
_ = f.readline()
alphabet = f.readline().rstrip().split()
_ = f.readline()

alignment = f.read().rstrip().split()    

A, B = hmm_build(alphabet, alignment, T)

#format output string   
f = StringIO()
A.to_csv(f, sep='\t', float_format='%g')
f.write('--------\n')
B.to_csv(f, sep='\t', float_format='%g')

open('rosalind_ba10e_sub.txt', 'wt').write(f.getvalue().rstrip())


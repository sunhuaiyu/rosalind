# rosalind_ba10g
'''
Sequence Alignment with Profile HMM Problem (apply Viterbi to find the max-scored path):
Given: A string Text, a multiple alignment Alignment, a threshold θ, and a pseudocount σ.
Return: An optimal hidden path emitting Text in HMM(Alignment,θ,σ).

Note: protein sequence != typical HMM observation sequence.
'''
import numpy as np
from numpy import log, argmax
from pandas import DataFrame
from io import StringIO


def hmm_build(alphabet, aln, threshold, sigma):
    '''Given alphabet, multiple alignment aln, insertion threshold and pseudocount sigma,
    return the profile HMM transition and emission matrix.'''
    
    aln_cols = list(zip(*(aln)))
    m, n = len(aln), len(aln_cols)       # m sequences, n columns

    # indices of columns where '-' count is below threshold
    match_cols = [i for i in range(n) if aln_cols[i].count('-') / m < threshold]

    # state names
    k = len(match_cols)   # there k M-states
    states_ = [('M'+ str(i), 'D' + str(i), 'I' + str(i)) for i in range(1, k + 1)]
    states = ['S', 'I0'] + [i for j in states_ for i in j] + ['E']
    
    # building matrices
    transitions = DataFrame(data=0.0, index=states, columns=states)
    emissions   = DataFrame(data=0.0, index=states, columns=alphabet) 

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

    # scale rows to [0, 1]
    transitions = transitions.div(transitions.sum(1) + 1e-10, axis=0).round(3)
    emissions = emissions.div(emissions.sum(1) + 1e-10, axis=0).round(3)
    
    #add pseudocounts
    transitions.iloc[:2, 1:4] += sigma
    transitions.iloc[-4:-1, -2:] += sigma
    for i in range(k):
        transitions.iloc[i*3-1:i*3+2, i*3+1:i*3+4] += sigma
        emissions.iloc[i*3+1:i*3+3, :] += sigma
    emissions.iloc[-2, :] += sigma
    
    # scale again
    transitions = transitions.div(transitions.sum(1) + 1e-10, axis=0) + 1e-100
    emissions = emissions.div(emissions.sum(1) + 1e-10, axis=0)  + 1e-100

    return transitions, emissions, states, k


def hmm_align(protein, hmm_T, hmm_E, states, k_matches):
    '''Given a protein sequence and a profile HMM model, 
    return the most likely hidden path. Largely based on Pevzner's YouTube.'''
    m = len(states)
    n = len(protein)     # n residues in protein

    # initialize Viterbi graph with each node contains [score, predecessor]
    V = {(i, j): [-np.inf, ''] for i in states for j in range(n+1)}
    
    # column 0, all Ds
    V['D1', 0] = [ log(hmm_T.loc['S', 'D1']), ('S', 0) ]
    
    for j in range(2, k_matches+1):
        V['D'+str(j), 0] = [ V['D'+str(j-1), 0][0] + 
            log(hmm_T.loc['D'+str(j-1), 'D'+str(j)]),  ('D' + str(j-1), 0) ]  
    
    # top 2 rows, I0, M1 of the remaining columns
    V['I0', 1] = [ log(hmm_T.loc['S', 'I0']) + log(hmm_E.loc['I0', protein[0]]), 
                  ('S', 0) ]
    V['M1', 1] = [ log(hmm_T.loc['S', 'M1']) + log(hmm_E.loc['M1', protein[0]]), 
                  ('S', 0) ]
    
    for i in range(2, n+1):
        V['I0', i] = [ V['I0', i-1][0] + log(hmm_T.loc['I0', 'I0']) +
                        log(hmm_E.loc['I0', protein[i-1]]), ('I0', i-1) ]

        V['M1', i] = [ V['I0', i-1][0] + log(hmm_T.loc['I0', 'M1']) +
                        log(hmm_E.loc['M1', protein[i-1]]), ('I0', i-1) ]
                       
        V['D1', i] = [ V['I0', i][0] + log(hmm_T.loc['I0', 'D1']) +
                        log(hmm_E.loc['D1', protein[i-1]]), ('I0', i) ]
    
    # main recurrence    
    for i in range(1, n+1):
        for j in range(2, k_matches+1):
            prev_states = 'M{} I{} D{}'.format(j-1, j-1, j-1).split()

            edges = [V[s, i-1][0] + log(hmm_T.loc[s, 'I'+str(j-1)]) for s in prev_states]
            V['I'+str(j-1), i] =[ max(edges) + log(hmm_E.loc['I'+str(j-1), protein[i-1]]),                               
                (prev_states[argmax(edges)], i-1) ]
            
            edges = [V[s, i-1][0] + log(hmm_T.loc[s, 'M'+str(j)]) for s in prev_states]                                              
            V['M'+str(j), i] = [ max(edges) + log(hmm_E.loc['M'+str(j), protein[i-1]]), 
                (prev_states[argmax(edges)], i-1) ]                     
            
            edges = [V[s, i][0] + log(hmm_T.loc[s, 'D'+str(j)]) for s in prev_states]            
            V['D'+str(j), i] = [ max(edges), (prev_states[argmax(edges)], i) ]
    
    # the last row (I{k_matches})
    for i in range(1, n+1):
        prev_states = 'M{} I{} D{}'.format(k_matches, k_matches, k_matches).split()
        
        edges = [V[s, i-1][0] + log(hmm_T.loc[s, 'I'+str(j)]) for s in prev_states]
        V['I'+str(j), i] = [ max(edges) + log(hmm_E.loc['I'+str(j), protein[i-1]]), 
            (prev_states[argmax(edges)], i-1) ]
    
    # End node
    node = (prev_states[argmax([V[s, n][0] + log(hmm_T.loc[s, 'E']) 
            for s in prev_states])], n)

    # path reconstruction
    path = []
    while node[0] != 'S':
        path.append(node[0])
        node = V[node][1]
    return ' '.join(path[::-1])
    

f = open('rosalind_ba10g.txt').read().split('--------')
protein = f[0].rstrip()
T, S = [float(i) for i in f[1].split()]   #threshold, pseudocount
alphabet = f[2].rstrip().split()
alignment = f[3].rstrip().split()    

result = hmm_align(protein, *(hmm_build(alphabet, alignment, T, S)))
print(result)
open('rosalind_ba10g_sub.txt', 'wt').write(result)


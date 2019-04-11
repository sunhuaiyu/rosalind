# viterbi wiki
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print(line)
    opt = []
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
    
    print('The steps of states are ' + ' '.join(list(map(str, opt))) + 
           ' with highest probability of %s' % max_prob)
    return opt
    
def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

#Sweet implementation of Viterbi in Python
import numpy as np

'''
N: number of hidden states
'''
class Decoder(object):
    def __init__(self, initialProb, transProb, obsProb):
        self.N = initialProb.shape[0]
        self.initialProb = initialProb
        self.transProb = transProb
        self.obsProb = obsProb
        assert self.initialProb.shape == (self.N, 1)
        assert self.transProb.shape == (self.N, self.N)
        assert self.obsProb.shape[0] == self.N
        
    def Obs(self, obs):
        return self.obsProb[:, obs, None]

    def Decode(self, obs):
        trellis = np.zeros((self.N, len(obs)))
        backpt = np.ones((self.N, len(obs)), 'int32') * -1
                
        # initialization
        trellis[:, 0] = np.squeeze(self.initialProb * self.Obs(obs[0]))
                
        for t in range(1, len(obs)):
            trellis[:, t] = (trellis[:, t-1, None].dot(self.Obs(obs[t]).T) * self.transProb).max(0)
            backpt[:, t] = (np.tile(trellis[:, t-1, None], [1, self.N]) * self.transProb).argmax(0)
        # termination
        tokens = [trellis[:, -1].argmax()]
        for i in range(len(obs)-1, 0, -1):
            tokens.append(backpt[tokens[-1], i])
        return tokens[::-1]






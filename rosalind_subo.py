# code copied from online; Matthew Burch (cryptc)

def SuboptimalLocalAlignment(dna1, dna2, maxMismatches_d=3, minRepeatSize=32, maxRepeatSize=40):
    large = dna1 if len(dna1) > len(dna2) else dna2
    mk1, mk2 = 0, 0
    for i in range(len(large)-minRepeatSize+1):
        for j in range(maxRepeatSize-minRepeatSize+1):
            kmer = large[i:i+minRepeatSize+j]
            k1 = ApproximatePatternMatching(kmer, dna1, maxMismatches_d, True)
            k2 = ApproximatePatternMatching(kmer, dna2, maxMismatches_d, True)
            mk1, mk2 = max(mk1, len(k1)), max(mk2, len(k2))
    return (mk1, mk2)

def ApproximatePatternMatching(dnaPattern, dnaText, maxMismatches_d, resultAsArray=False):
    patternLength = len(dnaPattern)
    solutionIndexes = []
    for i in range(len(dnaText)-patternLength+1):
        dna1 = dnaText[i : i+patternLength]
        hammingDistance = HammingDistance(dna1, dnaPattern)
        if hammingDistance <= maxMismatches_d:
            solutionIndexes.append(i)
    if resultAsArray:
        return solutionIndexes
    else:
        return ' '.join([str(i) for i in solutionIndexes])

def HammingDistance(dna1, dna2):
    distance = sum(1 for i, j in zip(dna1, dna2) if i != j)
    return distance
    


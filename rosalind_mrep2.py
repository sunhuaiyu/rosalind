# rosalind_mrep
# non Graph solution

def max_repeats_half(seq, t=20):
    n = len(seq)
    collection = set()
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            k = 0
            while j+k < n and seq[i+k] == seq[j+k]:
                k += 1
            if k >= t:
                collection.add(seq[i:i+k])
            j += 1
        i += 1  
    return collection


def max_repeats(seq, t=20):
    '''scan through seq to find maximum repeats'''
    n = len(seq)
    collection = set()
    i = 0
    while i < n - 1:
        j = i + 1
        while j < n:
            if i > 0 and seq[i-1]==seq[j-1]:
                j += 1 
                continue
            k = 0
            while j+k < n and seq[i+k] == seq[j+k]:
                k += 1
            if k >= t:
                collection.add(seq[i:i+k])
            j += 1
        i += 1
    return collection

result = '\n'.join(max_repeats(s))
# result = '\n'.join(max_repeats_half(s) & {i[::-1] for i in max_repeats_half(s[::-1])})

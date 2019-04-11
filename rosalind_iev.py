# sun.huaiyu
# IEV

p_dict = {0: 1.0, 1: 1.0, 2: 1.0, 3: 0.75, 4: 0.5, 5: 0}

dataset = open('rosalind_iev.txt').readline().rstrip().split()

dataset = [int(i) for i in dataset]

expected = sum([p_dict[i] * dataset[i] * 2 for i in range(6)])

print expected

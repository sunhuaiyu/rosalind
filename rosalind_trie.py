#rosalind_trie
def prefix(s):
	return [s[:i] for i in range(1, len(s) + 1)]        

all_prefix = set()
for line in open('rosalind_trie.txt'):
	s = line.rstrip()
	for p in prefix(s):
		all_prefix.add(p)

all_prefix = sorted(list(all_prefix))

prefix_dict = dict()
tried = []

end_node = 2
for kmer in all_prefix:
	if len(kmer) == 1:
		begin_node = 1
	else:
		begin_node = prefix_dict[kmer[:-1]][1] 
	prefix_dict[kmer] = (begin_node, end_node)
	tried.append(str(begin_node) + ' ' + str(end_node) + ' ' + kmer[-1])
	end_node += 1

result = '\n'.join(tried)
print(result)
open('rosalind_trie_sub.txt', 'wt').write(result)

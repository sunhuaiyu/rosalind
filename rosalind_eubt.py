#rosalind_eubt
'''
Given: A collection of species names representing n taxa.

Return: A list containing all unrooted binary trees whose leaves are these n taxa. 
Trees should be given in Newick format, with one tree on each line; the order of 
the trees is unimportant.
'''

'''main code for tree construction copied from Stackoverflow'''
# A very simple representation for Nodes. Leaves are anything which is not a Node.
class Node(object):
  def __init__(self, left, right):
    self.left = left
    self.right = right

  def __repr__(self):
    return '(%s, %s)' % (self.left, self.right)

# Given a tree and a label, yields every possible augmentation of the tree by
# adding a new node with the label as a child "above" some existing Node or Leaf.
def add_leaf(tree, label):
  yield Node(label, tree)
  if isinstance(tree, Node):
    for left in add_leaf(tree.left, label):
      yield Node(left, tree.right)
    for right in add_leaf(tree.right, label):
      yield Node(tree.left, right)

# Given a list of labels, yield each rooted, unordered full binary tree with
# the specified labels.
def enum_unordered(labels):
  if len(labels) == 1:
    yield labels[0]
  else:
    for tree in enum_unordered(labels[1:]):
      for new_tree in add_leaf(tree, labels[0]):
        yield new_tree


c = open('rosalind_eubt.txt').read().rstrip().split()
result = ['(' + str(i) + ')' + c[0] + ';' for i in enum_unordered(c[1:])]
open('rosalind_eubt_sub.txt', 'wt').write('\n'.join(result))

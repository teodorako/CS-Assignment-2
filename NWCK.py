#NWCK - Distances in Trees by Teodora Kovacevic 

from Bio import Phylo
from io import StringIO

dataset = """(cat)dog;
dog cat

(dog,cat);
dog cat"""


trees = dataset.rstrip().split('\n\n')
distances = []

for tree in trees:
    tree_line, node1, node2 = tree.split()
    tree = Phylo.read(StringIO(tree_line), 'newick')
    last_common = tree.common_ancestor(node1, node2)
    distances.append(len(last_common.get_path(node1)) + len(last_common.get_path(node2)))


result = ''
for distance in distances:
    result += str(distance) +' '
print(result)

#NKEW - Newick Format with Edge Weights by Teodora Kovacevic

from Bio import Phylo
from io import StringIO

dataset = """(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant"""


trees = dataset.split("\n\n")
distances = []

for tree in trees:
    tree_line, nodes = tree.split("\n")
    node1, node2 = nodes.split(" ")
    tree = Phylo.read(StringIO(tree_line), "newick")
    distance_str = str(int(tree.distance(node1, node2)))
    distances.append(distance_str)

result = " ".join(distances)
print(result)

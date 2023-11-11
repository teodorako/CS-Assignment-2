#LONG - Genome Assembly as Shortest Superstring by Teodora Kovacevic

import re
import networkx as nx

dataset = ">Rosalind_56ATTAGACCTG>Rosalind_57CCTGCCGGAA>Rosalind_58AGACCTGCCG>Rosalind_59GCCGGAATAC"
sequences = re.findall(r'[ATGC]+', dataset)
names = re.findall(r'Rosalind_[0-9]+',dataset)


G = nx.Graph()
G.add_nodes_from(sequences)


for seq1 in sequences:
    for seq2 in sequences:
        for k in range(len(seq1) // 2, len(seq1)):
            suffix = seq1[-k:]
            prefix = seq2[:k]
            if suffix == prefix:
                G.add_edge(seq1,seq2)

edges = nx.eulerian_path(G)
list_edges = []
for edge in edges:
    list_edges.append(edge[0])
    list_edges.append(edge[1])

result = list_edges[0]

for i in range(1, len(list_edges)):
    for j in range(len(list_edges[i]), -1, -1):
        if list_edges[i - 1].endswith(list_edges[i][:j]):
            result += list_edges[i][j:]
            break

print(str(result))







# === imports =================================================================
from tqdm import tqdm as tqdm
from pprint import pprint as pprint
import matplotlib.pyplot as plt
import networkx as nx
import netgraph

# === functions =================================================================

login_success = [ line.strip() for line in open( "0079_keylog.txt" ) ] 

# === test1 =================================================================

# generating pairs
pair_counts = {}
for seq in login_success:
	for pair in [ seq[1:], seq[:2] ]:
		if pair not in pair_counts.keys():
			pair_counts[pair] = 1
		elif pair in pair_counts.keys():
			pair_counts[pair] += 1

network = list() # weight, source, target

for pair in pair_counts.keys():
	network.append( [
		pair_counts[ pair ],
		pair[0],
		pair[1],
	] )

G = nx.DiGraph()

for edge in network:
	# G.add_edge( edge[1], edge[-1], weight=edge[0] )
	G.add_edge( edge[1], edge[-1] )


pos = nx.spring_layout( G )

nx.draw( G, with_labels=True )

# pos = nx.layout.spring_layout( G )
# plot_instance = netgraph.InteractiveGraph(graph, node_positions=pos)
# node_positions = plot_instance.node_positions

plt.show()
# plt.savefig("filename.png")

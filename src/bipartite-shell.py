import networkx as nx
import matplotlib.pyplot as plt

options_3 = {
 'with_labels': False,
 'node_color': 'grey',
 'node_size': 10,
 'linewidths': 0,
 'width': 0.1,
 'alpha': 0.3
}

G = nx.complete_bipartite_graph(25, 26)
nx.draw_shell(G, nlist = [range(0,25), range(25,51)], **options_3)

plt.savefig("img/bipartite-shell.png", format = "PNG")
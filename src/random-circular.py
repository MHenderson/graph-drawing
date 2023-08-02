import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(0)

options_2 = {
 'with_labels': False,
 'node_color': 'grey',
 'node_size': 10,
 'linewidths': 0,
 'width': 0.1,
}

G = nx.barabasi_albert_graph(100, 3)
nx.draw_circular(G, **options_2)

plt.savefig("img/random-circular.png", format = "PNG")
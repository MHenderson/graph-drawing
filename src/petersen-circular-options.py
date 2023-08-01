import networkx as nx
import matplotlib.pyplot as plt

options = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 200,
 'width': 3,
}

G = nx.petersen_graph()

nx.draw_circular(G, **options)

plt.savefig("img/petersen-circular-options.png", format = "PNG")
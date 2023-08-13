import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

options = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 200,
 'width': 3
}

G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)

nx.draw(G, G_layout, **options)

plt.savefig("img/petersen-shell.png", format = "PNG")
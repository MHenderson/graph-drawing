import networkx as nx
import matplotlib.pyplot as plt

options = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 200,
 'width': 3,
}

G = nx.petersen_graph()

plt.subplot(221)
nx.draw_circular(G, **options)

plt.subplot(222)
G_layout = nx.shell_layout(G, nlist = [range(5, 10), range(5)], rotate = 0.)
nx.draw(G, G_layout, **options)

plt.subplot(223)
nx.draw_spectral(G, **options)

plt.subplot(224)
nx.draw_spring(G, **options)

plt.savefig("img/petersen-various.png", format = "PNG")
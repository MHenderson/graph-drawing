import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

options = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 200,
 'width': 3,
}

nx.draw_shell(G, nlist = [range(5, 10), range(5)], **options)

plt.savefig("img/petersen-shell.png", format = "PNG")
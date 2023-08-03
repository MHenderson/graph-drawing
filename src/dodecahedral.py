import networkx as nx
import matplotlib.pyplot as plt

options_1 = {
 'with_labels': False,
 'node_color': 'black',
 'node_size': 50,
 'width': 1,
}

G = nx.dodecahedral_graph()
nx.draw_shell(G, nlist = [[2,3,4,5,6], [8,1,0,19,18,17,16,15,14,7], [9,10,11,12,13]], **options_1)

plt.savefig("img/dodecahedral.png", format = "PNG")
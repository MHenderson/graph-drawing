import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

nx.draw_circular(G, with_labels = False, node_color = 'black')

plt.savefig("img/petersen-circular-black.png", format = "PNG")
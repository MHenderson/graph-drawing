import networkx as nx
import matplotlib.pyplot as plt

G = nx.petersen_graph()

nx.draw(G, nx.circular_layout(G))

plt.savefig("img/petersen-circular.png", format = "PNG")
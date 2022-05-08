import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io

mat = scipy.io.loadmat('network-disruption/Reddit.mat')

NODES = 556

adj = mat["Reddit"]["a"][0][0] #adjacency matrix
s = mat["Reddit"]["recent_innate_opinions"][0][0] #innate opinion vector
print(s)

#make graph

g = nx.Graph()

for i in range(NODES):
    g.add_node(i)

for i in range(NODES):
    for j in range(NODES):
        if adj[(i,j)] == 1:
            g.add_edge(i,j)

# visualize graph

pos = nx.spring_layout(g, seed=95622)
nx.draw_networkx(g, pos,
    node_size=20,
    with_labels=False,
    node_color=list(np.log(s)),
    cmap=plt.get_cmap("bwr"),
    edge_color="#aaa",
    width=0.5)

ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()

#print(s)



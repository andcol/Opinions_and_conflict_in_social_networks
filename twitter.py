import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

NODES = 548

opinions = [0 for _ in range(NODES)]

with open("network-disruption/preprocess-twitter/opinion_twitter.txt", "r") as table:
    for row in table:
        data = row.split()
        node = int(data[0])-1
        opinion = float(data[2])
        opinions[node] = (2*opinion) - 1 #shift from [0,1] to [-1,1]

adj = np.zeros((NODES, NODES)) #adjacency matrix
deg = np.zeros((NODES, NODES)) #degree matrix

with open("network-disruption/preprocess-twitter/edges_twitter.txt", "r") as table:
    for row in table:
        data = row.split()
        source = int(data[0])-1
        target = int(data[1])-1
        adj[source, target] = 1
        deg[source, source] += 1 #count only in the outgoing direction to avoid duplicates

z = np.array(opinions) #expressed opinion vector at equilibrium
lap = np.subtract(deg, adj) #laplacian
id = np.identity(NODES)

s = np.matmul(np.add(lap, id), z) #innate opinion vector

smin = np.min(s)
smax = np.max(s)

#make graph

g = nx.Graph()

for i in range(NODES):
    g.add_node(i)

for i in range(NODES):
    for j in range(NODES):
        if adj[i, j] != 0:
            g.add_edge(i, j)

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



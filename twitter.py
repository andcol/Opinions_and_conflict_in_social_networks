import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

NODES = 548


#import the data

print("Loading data...")
#get expressed opinions
opinions = [0 for _ in range(NODES)]
with open("network-disruption/preprocess-twitter/opinion_twitter.txt", "r") as table:
    for row in table:
        data = row.split()
        node = int(data[0])-1
        opinion = float(data[2])
        opinions[node] = (2*opinion) - 1 #shift from [0,1] to [-1,1]

z = np.array(opinions) #expressed opinion vector at equilibrium

#get adjacency and degree matrices
adj = np.zeros((NODES, NODES)) #adjacency matrix
deg = np.zeros((NODES, NODES)) #degree matrix
with open("network-disruption/preprocess-twitter/edges_twitter.txt", "r") as table:
    for row in table:
        data = row.split()
        source = int(data[0])-1
        target = int(data[1])-1
        adj[source, target] = 1
        deg[source, source] += 1 #count only in the outgoing direction to avoid duplicates

#compute the innate opinion vector s = (lap - id)z
lap = np.subtract(deg, adj) #laplacian
id = np.identity(NODES)
s = np.matmul(np.add(lap, id), z)

for i in range(NODES): #clamp to [-1,1]
    s[i] = max(-1, min(1, s[i]))


#make graph

print("Building graph...")
g = nx.Graph()

for i in range(NODES): #V = {0,1,...,548-1}
    g.add_node(i)

for i in range(NODES):
    for j in range(NODES):
        if adj[i, j] == 1:  #convert from adjacency matrix
            g.add_edge(i, j)


# visualize graph
print("Visualizing graph...")

pos = nx.spring_layout(g, seed=95622) #position nodes according to Fruchterman-Reingold force-directed algorithm

#actual drawing
nx.draw_networkx_nodes(g, pos,
    node_size=20,
    node_color=list(s),
    cmap=plt.get_cmap("bwr"),
    edgecolors='#aaa',
    linewidths=0.4
    )
nx.draw_networkx_edges(g, pos,
    edge_color="#aaa",
    alpha=0.4,
    width=0.5
    )

#invoke matplotlib
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()


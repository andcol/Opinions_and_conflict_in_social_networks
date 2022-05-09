import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import scipy.io

NODES = 556


#import the data

print("Loading data...")
mat = scipy.io.loadmat('network-disruption/Reddit.mat')
adj = mat["Reddit"]["a"][0][0] #adjacency matrix
s = mat["Reddit"]["recent_innate_opinions"][0][0] #innate opinion vector


#make graph

print("Building graph...")
g = nx.Graph()

for i in range(NODES): # V = {0,1,...,556-1}
    g.add_node(i) 

for i in range(NODES):
    for j in range(NODES):
        if adj[(i,j)] == 1: #convert from adjacency matrix
            g.add_edge(i,j)


#visualize graph

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
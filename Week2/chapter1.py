#%%
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # Create graph
G.add_nodes_from([1, 2, 3, 4, 5]) # Create nodes
G.add_edges_from([(1,2), (3, 4), (3, 5)]) # Connect nodes with edges

print(G.nodes()) # Get list of nodes

#%%
# Function to get all neighbors of a node
def neighbs(node):
    for nb in G.neighbors(node):
        print("Neighbor of " + str(node) + ": " + str(nb))

#%%
# Get neighbors for all nodes
for n in G.nodes:
    neighbs(n)

#%%
# Get all edges
for u, v in G.edges:
    print(u, v)

#%% 
# Create a Directed Graph
D = nx.DiGraph()
# Adding edges without adding nodes creates those nodes
D.add_edge(1, 2)
D.add_edge(2, 1)
D.add_edges_from([(2,3), (3,4)])
# Get lists of nodes and edges 
print(D.nodes)
print(D.edges)
# Get number of nodes and edges
print("D # Nodes: " + str(D.number_of_nodes()))
print("D # Edges: " + str(D.number_of_edges()))


#%%
# Neighbors - Gets all edges linking to & from in a directed graph
for n in D.neighbors(2):
    print("Neighbor of 2: " + str(n))
# Predecessors - Gets edges linking *to* the node
for p in D.predecessors(2):
    print("Predecessor of 2: " + str(p))
# Successors - Gets edges linking *from* the node
for s in D.successors(2):
    print("Successor of 2: " + str(s))

#%%
# Generating different network types
# Bipartite - Nodes of one group only link to nodes of another
B = nx.complete_bipartite_graph(4, 5)
# Cycle - A circuit (starts/ends on same node) - Doesn't repeat nodes
C = nx.cycle_graph(4)
# Path - Sequence of nodes
P = nx.path_graph(5)
# Star - One center node connects to all other outer nodes
S = nx.star_graph(6)

#%%
# Display graphs
nx.draw_networkx(B)

#%%
nx.draw_networkx(C)
#%%
nx.draw_networkx(P)
#%%
nx.draw_networkx(S)

#%%
nx.density(S)

#%%

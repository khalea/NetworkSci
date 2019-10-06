# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # NetworkX Recap
# 
# You can use NetworkX to construct and draw graphs that are undirected or directed, with weighted or unweighted edges. An array of functions to analyze graphs is available. This tutorial takes you through a few basic examples and exercises.
# 
# Note that many exercises are followed by a block with some `assert` statements. These assertions may be preceded by some setup code. Please don't change anything in these blocks.
# 
# ## Official documentation
# 
# http://networkx.github.io/documentation/latest/
# 
# ## Other useful tutorials
# 
# http://networkx.github.io/documentation/latest/tutorial/tutorial.html
# 
# http://jponnela.com/web_documents/networkx.pdf
#%% [markdown]
# # Directed graphs
# 
# Building on our discussion from last week - directed graphs are definined in very similar ways to undirected graphs, however, with consideration being given for the weights associated with the edges. 

#%%
import networkx as nx

D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels=True)

#%% [markdown]
# # <font color='red'>EXERCISE 1</font>
# 
# The directed analogs to neighbors are predecessors ("in-neighbors") and successors ("out-neighbors").
# 
# If you run the cell below without changing anything - instead of seeing the neighbors, you will see <dict_keyiterator object at (some address)>
# 
# There is an easy way to fix this, if you think back to the tutorial we had last week. Regardless of whether you use that method, alter the print statements so that they correctly print the neighbors of the specified nodes. 
# 
# **Also note that due to a quirk in the "dict-of-dicts" structure, the `neighbors` method is a synonym for 'successors'. Don't accidentally use it.**

#%%
print('Successors to 3:', list(D.successors(3)))

print('Predecessors to 2:', list(D.predecessors(2)))

print('neighbors to 3:', list(D.neighbors(3)))

#%% [markdown]
# # <font color='red'>EXERCISE 2</font>
# 
# Write a function `get_bidirectional_edges` that takes a directed graph as an argument. The function should return a list of 2-tuples, one such tuple for each pair of nodes with incident edges in both directions. Return only one such tuple per pair of edges, e.g. if there are links in both directions between 3 and 2, don't return `(2, 3)` and `(3, 2)`.
# 
# Hint: You can intersect two lists like this:
# ```
# set(list1).intersection(set(list2))
# ```
# The intersection of two sets is the collection of elements present in both sets. Set intersection is not required for this; don't worry if you don't end up needing it.

#%%
def get_bidirectional_edges(DG):
    
    duonoodes = []
    graphNodes = DG.nodes

    for node in graphNodes:

        # Only check nodes that have in/outdegree > 0
        if (DG.in_degree(node) > 0) and (DG.out_degree(node) > 0):
            innode = DG.predecessors(node)
            outnode = DG.successors(node)
            # Check predecessors and successors for duplicate nodes
            for i in innode:
                if i in outnode:
                    duonoodes.append((node, i))
    return duonoodes
            


#%%
D = nx.DiGraph()
D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])
bde = get_bidirectional_edges(D)
assert len(bde) == 2
assert (2, 3) in bde or (3, 2) in bde
assert (4, 6) in bde or (6, 4) in bde

#%% [markdown]
# # Paths
# 
# The following are all examples of the functionality networkx supports regarding path. Follow along with the cells, and if there is anything that seems unclear - look up the documentation for it, it's good practice! 

#%%
D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,2),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])

nx.draw(D, with_labels="True")

print( nx.has_path(D, 1, 6) )

print( nx.shortest_path(D, 1, 6) )


#%%
print( nx.has_path(D,6,1) )


#%%
# This will raise an error
print( nx.shortest_path(D, 6, 1) )


#%%
# A simple path is one that does not pass through any node more than once

# this is an iterator
all_paths = nx.all_simple_paths(D, 1, 5)  

print(list(all_paths))

print(nx.shortest_path(D, 1, 5))


#%%
# this is an iterator object
all_shortest_paths = nx.all_shortest_paths(D, 1, 6)  

list(all_shortest_paths)


#%%
nx.average_shortest_path_length(D)


#%%
nx.is_strongly_connected(D)


#%%
nx.is_weakly_connected(D)


#%%
# This will raise an error
nx.is_connected(D)


#%%
G = nx.Graph()

G.add_nodes_from([1,2,3,4])

G.add_edges_from([(1,2),(2,3),(1,3),(1,4)])

nx.draw(G, with_labels="True")


#%%
nx.is_connected(G)


#%%
# Diameter is necessarily greater than or equal to APL

print(nx.average_shortest_path_length(G))

print(nx.diameter(G))


#%%
G.remove_edge(1,4)
nx.is_connected(G)


#%%
# This will raise an error; diameter not defined for disconnected network

nx.diameter(G)

#%% [markdown]
# # <font color='red'>EXERCISE 3</font>

#%%
D = nx.DiGraph()

D.add_edges_from([(1,2),(2,3),(3,4),(3,5),(4,5),(4,6),(5,6),(6,4),(4,2)])
nx.draw(D, with_labels="True")

#%% [markdown]
# Start with the directed graph above and create an undirected version of the graph. Name this graph `G`. Do not hard-code the edges -- instead, devise an automatic way to do the conversion. Draw the graph.

#%%
G = nx.Graph()
for node in D.nodes():
    for nei in list(D.neighbors(node)):
        G.add_edge(node, nei)
nx.draw(G, with_labels="True")


#%%

''' READ ME !!!
I changed edges_iter() because I kept getting the errors
- 'DiGraph' object has no attribute 'edges_iter'"
- 'Graph' object has no attribute 'edges_iter'
because that method was replaced with edges() in NetworkX version 2.
I'm running version 2.3 locally.
Read here: https://networkx.github.io/documentation/stable/release/release_2.0.html

'''

assert not G.is_directed()
assert set(D.nodes()) == set(G.nodes())
for edge in D.edges():
    assert G.has_edge(*edge)
for a, b in G.edges():
    assert D.has_edge(a, b) or D.has_edge(b, a)

#%% [markdown]
# # <font color='red'>EXERCISE 3.1</font>
#%% [markdown]
# Answer the following questions about `G`, the converted graph from the previous question, by printing the results to the appropriate NetworkX statements:
# * Is this graph connected?
# * What is its average shortest path length (APL)?
# * diameter?

#%%
# Connected?
print(nx.is_connected(G))
# APL? - Shortest path between nodes
print(nx.average_shortest_path_length(G))
# Diameter? - Longest path between nodes
print(nx.diameter(G))

#%% [markdown]
# # <font color='red'>EXERCISE 3.2</font>
#%% [markdown]
# How many simple paths exist between nodes 1 and 5 in the graph `G` from 9.1? Answer with an appropriate NetworkX statement.

#%%
# Simple paths between 1 and 5
simPaths = nx.all_simple_paths(G, 1, 5)
print(list(simPaths))

#%% [markdown]
# # <font color='red'>EXERCISE 4</font>
#%% [markdown]
# Write a function `attack_network_edges` that takes two arguments: a graph and an integer N. In the function, make a copy of the input graph, and then remove N edges at random from the copy. Return the "attacked" copy.
# 
# Note: Be careful not to modify the original graph `G` in your function.

#%%
import random

def attack_network_edges(G, n):
    N = G.copy()
    v = list(N.nodes)
    
    i = 0
    while i < n:
        # Pick random node
        node = random.choice(v)
        # Remove node from remaining pool
        v.remove(node)
        # Remove node from graph
        N.remove_node(node)
        i+=1
    return N
        
# Examples
# attack_network_edges(G, 2)
# attack_network_edges(G, 5)

#%% [markdown]
# # <font color='red'>EXERCISE 4.1</font>
#%% [markdown]
# Run `attack_network_edges` on graph `G` from 9.1 ten times, removing 2 edges each time. For each run, keep track of whether or not the resulting attacked graph is connected. What proportion of the time did the attack disconnect the network? Either have a print statement which outputs your answer, or write your answer as a comment at the bottom of your code. 

#%%

# Percentage of disconnects varies (as I'm sure you could imagine), 
# so run it multiple times if you'd like :)

# Disconnect tracker
dc = 0
k = 0
while k < 10:
    # Store the resulting 'attacked' graph
    Q = attack_network_edges(G, 2)
    print("Remaining nodes: ", list(Q.nodes))
    # Check if connected
    connected = nx.is_connected(Q)
    print("Connected?:", connected)
    # Update disconnects
    if connected == False:
        dc +=1
    k += 1

# Percentage of disconnects
print(dc/10)



#%%

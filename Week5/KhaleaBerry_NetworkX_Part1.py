# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
from IPython import get_ipython

#%% [markdown]
# # NetworkX Intro
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
# # The `import` statement
# 
# Recall that `import` statements go at the top of your code, telling Python to load an external module. In this case we want to load NetworkX, but give it a short alias `nx` since we'll have to type it repeatedly, hence the `as` statement.
# 
# Also recall that lines starting with the `%` character are not Python code, they are "magic" directives for Jupyter notebook. The `%matplotlib inline` magic tells Jupyter Notebook to draw graphics inline i.e. in the notebook. This magic should be used right after the import statement.

#%%
import networkx as nx
get_ipython().run_line_magic('matplotlib', 'inline')

#%% [markdown]
# # Creating and drawing undirected graphs

#%%
# a "plain" graph is undirected
G = nx.Graph()

# give each a node a 'name', which is an integer in this case.
G.add_node('a')

# the add_nodes_from method allows adding nodes from a sequence, in this case a list
nodes_to_add = ['b', 'c', 'd']
G.add_nodes_from(nodes_to_add)

# add edge from 'a' to 'b'
# since this graph is undirected, the order doesn't matter here
G.add_edge('a', 'b')

# just like add_nodes_from, we can add edges from a sequence
# edges should be specified as 2-tuples
edges_to_add = [('b', 'c'), ('a', 'c')]
G.add_edges_from(edges_to_add)

# draw the graph
nx.draw(G, with_labels=True)

#%% [markdown]
# # Graph methods
# 
# The graph object has some properties and methods giving data about the whole graph.

#%%
# List all of the nodes
G.nodes()


#%%
# List all of the edges
G.edges()

#%% [markdown]
# Note that the return types of both `G.nodes()` and `G.edges()` match the types we used when entering the graph data above, i.e. a list of nodes, and a list of tuples for edges.
# 
# We can get the number of nodes and edges in a graph using the `number_of_` methods. These methods are *much* more efficient than using `len(G.nodes())` or `len(G.edges())`.

#%%
G.number_of_nodes()


#%%
G.number_of_edges()

#%% [markdown]
# Some graph methods take and edge or node as an argument. These provide the graph properties of the given edge or node.

#%%
# list of neighbors of node 'b'
G.neighbors('b')

#%% [markdown]
# # <font color='red'>EXERCISE 1</font>
# 
# Using this adjacency matrix, create the corresponding graph and name it `G`. Then print out the number of edges and the list of edges and draw the graph.
# 
# |       | a | b | c | d |
# |-------|---|---|---|---|
# | **a** |   |   |   |   |
# | **b** | 1 |   |   |   |
# | **c** | 1 | 1 |   |   |
# | **d** | 0 | 0 | 1 |   |

#%%
G = nx.Graph()
mgNodes = ['a', 'b', 'c', 'd']
mgEdges = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd')]
G.add_nodes_from(mgNodes)
G.add_edges_from(mgEdges)
nx.draw(G, with_labels="True")


#%%
assert G.number_of_nodes() == 4
assert G.number_of_edges() == 4

#%% [markdown]
# # Node and edge membership
# 
# To check if a node is present in a graph, you can use the `has_node()` method:

#%%
G.has_node('a')


#%%
G.has_node('x')

#%% [markdown]
# # <font color='red'>EXERCISE 2</font>
# Using the `.neighbors()` method, write a function named `edge_exists` that takes three arguments, a graph and two node names, and returns a boolean (True or False) for whether or not there is an edge between those two nodes. It should handle the case when one of the nodes does not exist.

#%%
def edge_exists(graph1, node1, node2):
    if (graph1.has_edge(node1, node2)):
        return True
    else:
        return False


#%%
G = nx.Graph()
G.add_edges_from([('a', 'b'), ('a', 'c')])

assert edge_exists(G, 'a', 'b')
assert edge_exists(G, 'b', 'a')
assert not edge_exists(G, 'b', 'c')
assert not edge_exists(G, 'c', 'b')
# handling non-existent nodes
assert not edge_exists(G, 'a', 'd')
assert not edge_exists(G, 'd', 'a')
assert not edge_exists(G, 'd', 'e')

#%% [markdown]
# NetworkX does have a method for doing this task of testing edge membership:

#%%
G.has_edge('a', 'b')


#%%
G.has_edge('a', 'd')

#%% [markdown]
# ### Syntactic sugar
# Under the hood, a NetworkX graph is actually a dict of dicts. This means the following works for checking node membership:

#%%
'a' in G


#%%
'x' in G

#%% [markdown]
# # A note on naming conventions
# 
# Usually in Python, variables are named in `snake_case`, i.e. lowercase with underscores separating words. Classes are conventionally named in `CamelCase`, i.e. with the first letter of each word capitalized.
# 
# Obviously NetworkX doesn't use this convention, often using single capital letters for the names of graphs. This is an example of convention leaking from the world of discrete mathematics. Since most of the documentation you will find online uses this convention, we will follow it as well.
#%% [markdown]
# # Looping over graph elements
# 
# Since graphs can be large, we need to be a bit careful about how we loop over their elements. Returning lists every time can be memory-intensive, so we prefer to use iterators when we loop. The following object is an iterator for the nodes in the graph.

#%%
G.nodes()

#%% [markdown]
# nodes_iter() --> nodes()
# This does not print out all of the keys all at once; this is the behavior we want -- we want to get them one at a time, as we need them in the loop:

#%%
for node in G.nodes():
    print(node)

#%% [markdown]
# There exists an analogous iterator for edges:
# edges_iter() ----> edges()

#%%
for edge in G.edges():
    print(edge)

#%% [markdown]
# Syntactic sugar: recall that we use the `in` operator to check for membership because a NetworkX graph is a type of dict. This means the following shorthand also works to loop over the node names:

#%%
for node in G:
    print(node)

#%% [markdown]
# # <font color='red'>EXERCISE 3</font>
# Often in the context of trees, a node with degree 1 is called a *leaf*. Write a function named `get_leaves` that takes a graph as an argument, loops through the nodes, and returns a list of nodes with degree 1.
# 
# Note: remember not to use `G.nodes()` with a `for..in` loop, use `G.nodes_iter()` or just `G` instead.

#%%


def get_leaves(Gph):
    
    leaves = []
    for n in Gph.nodes():
        # print("Degree of Node " + str(n) + ": " +  str(G.degree(n)))
        if (Gph.degree(n) == 1):
            leaves.append(n)
    return leaves



#%%
G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
assert set(get_leaves(G)) == {'c', 'b'}

#%% [markdown]
# # Node names
# 
# The node names don't have to be single characters -- they can be strings or integers or any immutable object, and the types can be mixed. The example below uses strings and integers for names.

#%%
G = nx.Graph()

G.add_nodes_from(['cat','dog','virus',13])

G.add_edge('cat','virus')

# specify a list of colors for the nodes; can be a single color as well.

nx.draw(G, with_labels=True)

#%% [markdown]
# ## Optional aside: how to draw a graph with offset labels
# 
# `nx.draw()` by default computes a spring layout, but explicitly calling `spring_layout` only returns the node positions in the layout:

#%%
nx.spring_layout(G)

#%% [markdown]
# We can use these positions, offset them a bit, and get positions for the labels.

#%%
# when manually drawing, we need pyplot
import matplotlib.pyplot as plt

plt.axis('off')

pos = nx.spring_layout(G)

nodes = nx.draw_networkx_nodes(G,pos)
edges = nx.draw_networkx_edges(G,pos)

# offset the y coordinates (in the 1 position) slightly
for k in pos.keys():
    pos[k][1] -= 0.1

labels = nx.draw_networkx_labels(G, pos)

#%% [markdown]
# # Adjacency lists
# 
# One way to represent a graph, in addition to an adjacency matrix, is an adjacency list. This is most useful for unweighted graphs, directed or undirected. In an adjacency list, each line contains some number of node names. The first node name is the "source" and each other node name on the line is a "target". For instance, given the following adjacency list:
# ```
# a d e
# b c
# c
# d
# e
# ```
# the edges are as follows:
# ```
# (a, d)
# (a, e)
# (b, c)
# ```
# The nodes on their own line exist so that we are sure to include any singleton nodes. Note that if our graph is undirected, we only need to specify one direction for each edge. Importantly, whether the graph is directed or undirected is often not contained in the file itself -- you have to infer it. This is one limitation of the format.
# 
# In this directory, there is a file called `friends.adjlist`. You can look at it in the "Files" pane, but here are the contents:

#%%
get_ipython().run_line_magic('cat', 'friends.adjlist')

#%% [markdown]
# In NetworkX's adjacency list format, a line beginning with a hash '`#`' is ignored as a comment.
#%% [markdown]
# # <font color='red'>EXERCISE 4</font>
# 
# Now that you're experts in parsing delimited text files, parse the `friends.adjlist` adjacency list in this directory and create the corresponding undirected graph. Name this graph `SG` for "social graph" and draw it. Make sure your code ignores lines starting with a hashmark.
# 
# Hint: you probably want to use the string method `.startswith()` to help.

#%%
ppl = []

# Build a list of lists containing each line
# Where the 0th index is the node and the following are its neighbors
for line in open('friends.adjlist'):
    if (not (line.startswith('#'))):
        ppl.append(line.strip().split(' '))
# print(ppl)

# Create the graph 
SG = nx.Graph()
# Add nodes
for i in ppl:
    SG.add_node(i[0])


# Add adjacencies/edges
for j in ppl: # Look at "rows" (j is a row)
    for k in j: # Look at connections in that row (k is an item in a row)
        if (k != j[0]): # j[0] is the column header/node in question
            SG.add_edge(j[0], k)
# SG.edges()

nx.draw(SG, with_labels="True")


#%%
assert 'Shelly' in SG
assert SG.number_of_edges() == 9
assert SG.number_of_nodes() == 8

#%% [markdown]
# # Aside: comprehensions
# 
# Often we have one sequence of values and we want to generate a new sequence by applying an operation to each item in the first. List comprehensions and generator expressions are compact ways to do this.
# 
# List comprehensions are specified inside square brackets, and immediately produce a list of the result.

#%%
items = ['spider', 'y', 'banana']
[item.upper() for item in items]

#%% [markdown]
# In the context of NetworkX, this is often used to do something with the node or edge lists:

#%%
[node.upper() for node in SG]

#%% [markdown]
# Generator expressions are slightly different as they are evaluated 'lazily.' These are specified using round braces, and if they are beiing expressed as a function argument, they can be specified without any braces. These are most often used in the context of aggregations:

#%%
g = (len(item) for item in items)
list(g)


#%%
max(len(item) for item in items)


#%%
sorted(item.upper() for item in items)

#%% [markdown]
# ## <font color='red'>EXERCISE 5</font>
# 
# Assign the list `[3, 9, 12, 15]` to a variable. Use a list comprehension to store the square of each of these numbers in a variable named `squares`.

#%%

# TODO
nums = [3, 9, 12, 15]
squares = [x * x for x in nums]
squares

#%%
assert squares == [9, 81, 144, 225]

#%% [markdown]
# ## Node degree
# 
# In this section, we will learn by doing. We're going to reuse the SG graph from exercise 1.4.

#%%
SG = nx.read_adjlist('friends.adjlist')

#%% [markdown]
# # <font color='red'>EXERCISE 6.1</font>
# 
# Using the `SG` graph, generate a list of tuples with each tuple containing: (person name, the number of people he/she is friends with). Name this list `degree_tuples` and print it.
# 
# **Bonus**: Do this with a list comprehension.

#%%
degree_tuples = []

# Regular for loop
'''
for node in SG.nodes():
    degree_tuples.append((node, SG.degree(node)))
degree_tuples '''
# nx.draw(SG, with_labels="True")

# List comprehension - Generates a list of tuples
degree_tuples = [(str(node), str(SG.degree(node))) for node in SG.nodes()]
degree_tuples


#%% [markdown]
# # <font color='red'>EXERCISE 6.2</font>
#%% [markdown]
# Recall the `dict` constructor. When we used it along with `zip`, we saw that it makes a dict from a list of key-value 2-tuples. Make a dict from the `degree_tuples`, name it `degree`, and print it.

#%%

# this makes a list of tuples for some reason?
# degree = zip(degree_tuples)

# Node name
degName = [i[0] for i in degree_tuples]
degName
# Degree as a number
actualDeg = [i[1] for i in degree_tuples]
actualDeg

degree = zip(degName, actualDeg)
for i in degree:
    print(i)

#%% [markdown]
# If you completed the previous exercise, notice that the output is the same (modulo order) as the following:

#%%
SG.degree()

#%% [markdown]
# We can use the node name as an argument to the `degree` function in order to get the node degree

#%%
SG.degree('Alice')

#%% [markdown]
# # Removing nodes and edges

#%%
SG = nx.read_adjlist('friends.adjlist')

# if you want to make a copy, use the copy() method
# instead of direct assignment like G1 = G2.
# this has to do with mutability
SG2 = SG.copy()  

SG2.remove_node('Alice')

nx.draw(SG2, with_labels=True)


#%%
SG2.remove_edge('Claire', 'Frank')
nx.draw(SG2, with_labels=True)

#%% [markdown]
# NetworkX will raise an error if you try to remove a single nonexistent node or edge.

#%%
# Alice has already been removed
SG2.remove_node('Alice')


#%%
# This edge does not exist
SG2.remove_edge('Frank', 'Bob')

#%% [markdown]
# Just as you can add a sequence of nodes and edges, you can also remove whole sequences at a time. Note that removing nodes also removes all edges incident on that node.

#%%
SG3 = SG.copy()

nx.draw(SG3, with_labels=True)


#%%
banned_users = ['Shelly', 'George']
SG3.remove_nodes_from(banned_users)

nx.draw(SG3, with_labels=True, node_color='lightgreen')

#%% [markdown]
# But note that bulk removing nodes or edges will not raise errors if you try to remove nonexistent elements.

#%%
# Neither Chelsea nor Sarah are in the graph
banned_users = ['Chelsea', 'Sarah']
SG3.remove_nodes_from(banned_users)

# Alice and Dennis are not friends
unfriend_requests = [('Alice', 'Bob'), ('Alice', 'Dennis')]
SG3.remove_edges_from(unfriend_requests)

nx.draw(SG3, with_labels=True, node_color='lightblue', font_size=20, node_size=500)

#%% [markdown]
# ## Aside: Python's `random` module
# 
# Given a list, `random.choice()` returns a single random element from the list. In order to use this function, you must first import the `random` module:

#%%
import random

#%% [markdown]
# Try executing the following block a few times. Note: you can use Ctrl + Enter (maybe different on a mac?) to execute the block without moving to the next one.

#%%
random.choice(SG.nodes())

#%% [markdown]
# If you want to select more than one item, use `random.sample()`:

#%%
random.sample(SG.nodes(), 3)

#%% [markdown]
# The `random.random()` function returns a float between 0 and 1. This is useful for probabilistically choosing something. For instance, the sentence "there is a 60% chance of rain" translates to "the probability of rain is 0.6" which roughly translates into the following block. Execute it a few times.

#%%
if random.random() < .6:
    weather = 'rain'
else:
    weather = 'sun'
print(weather)

#%% [markdown]
# # <font color='red'>EXERCISE 7</font>
# 
# In case you haven't noticed, you can read an adjacency list into a graph using `nx.read_adjlist`. Read the `'friends.adjlist'` adjacency list we've been using into a graph object. For every node in the graph, if that node has any incident edges, with probability 0.5 delete one random edge incident on that node.

#%%
# Run this cell and the following cell (in that order) a few 
# Times for different results :)
# You can run the next cell repeatedly
# Until there are no connected nodes

P = nx.read_adjlist('friends.adjlist')
nx.draw(P, with_labels="True")
print("Initial Graph")


#%%
edges = []

for n in P.nodes():
    if (P.degree(n) > 1) and (random.random() >= .5):
        # List of edges connected to node n
        edges = list(P.edges(n))
        # Edge tuple (node1, node2)
        remove = random.choice(edges)
        # Remove the edge
        P.remove_edge(remove[0], remove[1])
    print(n, edges)

print("Final")
nx.draw(P, with_labels="True")

#%%

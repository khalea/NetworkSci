# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
import networkx as nx
import matplotlib as mpl

#%%
# Make graph
G = nx.read_edgelist('/Users/khalea/Desktop/Fall19/NetworkSci/Week12/facebook_combined.txt.gz')
#%%
# Total number of nodes
totalNodes = len(G.nodes())
print(totalNodes)
#%%
# What proportion of nodes have a degree of 10 or higher?

# Number of nodes with degree >= 10
count = 0 
# Counting nodes with degree >= 10
for node in G.nodes():
    if G.degree(node) >= 10:
        count += 1

print(count, 'nodes have degree greater than 10')

proportion = count / totalNodes
print('The proportion of nodes with degree greater than 10 is', proportion)


# %%
# What proportion of nodes have a degree of 100 or higher?

# Number of nodes with degree >= 100
count = 0 
# Counting nodes with degree >= 100
for node in G.nodes():
    if G.degree(node) >= 100:
        count += 1

print(count, 'nodes have degree greater than 100')

proportion = count / totalNodes
print('The proportion of nodes with degree greater than 100 is', proportion)

# %%
# Find the maximum degree in the network
degrees = [G.degree(n) for n in G.nodes]
print(max(degrees))


# %%
import numpy as np

# Sort degrees in ascending order
degrees = sorted(degrees)
# print(degrees)

np.quantile(degrees, [.95])


# %%
# Sort nodes by degree and pick the max
s = sorted(G.nodes, key=G.degree, reverse=True)
print('Node', s[0], 'has degree', G.degree(s[0]))

# %%
# Maximum number of pairs of nodes
pairs = (totalNodes * (totalNodes-1)) / 2
print(pairs)

# %%
import random

picks = 0
sumSP = 0

while picks < 1000:
    # Pick a random pair of nodes
    pair = random.sample(G.nodes(), 2)
    # print(pair)
    picks += 1
    # Find path length
    spLen = nx.shortest_path_length(G, pair[0], pair[1])
    sumSP += spLen

avgSP = sumSP/1000
print('Avg shortest path from the sample:', avgSP)



# %%

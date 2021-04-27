# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Week7'))
	print(os.getcwd())
except:
	pass
#%%
from IPython import get_ipython

#%% [markdown]
# Histograms and distributions
# ====
# 
# Often when we want to get a sense of some data we use summary statistics like mean, median, mode, max, min, and maybe standard deviation. A generalization of these quantities is to look at the entire distribution, and a graphical way to do that is with the [Histogram](https://en.wikipedia.org/wiki/Histogram).
# 
#%% [markdown]
# # Python's `statistics` module
# 
# Python's standard library contains the `statistics` module, which has functions for common summary statistics on 1-d arrays (lists) of numerical data:

#%%
vec = [1] * 1 + [2] * 2 + [3] * 3 + [4] * 4 + [5] * 5
vec


#%%
import statistics
statistics.mean(vec)


#%%
statistics.median(vec)


#%%
statistics.mode(vec)


#%%
statistics.stdev(vec)

#%% [markdown]
# # Discrete random variables: dice
# 
# Rolling a die of N sides can be thought of as randomly choosing a number between 1 and N (inclusive, oddly). We can simulate a die roll using Python's `random` module:

#%%
import random
random.randint(1, 6)

#%% [markdown]
# Execute the above block a few times. Each execution displays the outcome for that die roll.
#%% [markdown]
# # <font color='red'>EXERCISE 1</font>
# 
# Roll a six-sided die 100 times, recording the outcome for each roll in a list. Print the mean, median, and mode of the resulting outcome distribution. Try this a few times.

#%%
ints = []
i = 0

while (i < 100):
    num = random.randint(1, 6)
    ints.append(num)
    i += 1

mean = statistics.mean(ints)
median = statistics.median(ints)
mode = 0 
try:
    mode = statistics.mode(ints)
except: print("No unique mode")

print("Mean:",  mean, "Median:", median,
"Mode:", mode)



#%% [markdown]
# # <font color='red'>EXERCISE 2</font>
# 
# In many dice games, the player rolls two dice and the outcome is taken to be the sum of the two dice values. Simulate 100 rolls of two six-sided dice; for each roll record the sum of the two dice.  Print the mean, median, and mode of the resulting outcome distribution. Try this a few times.

#%%
sums = []
thisSum = 0
i = 0


while i < 100:
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    thisSum = n1 + n2
    sums.append(thisSum)
    i += 1

mean = statistics.mean(sums)
median = statistics.median(sums)
mode = 0 
try:
    mode = statistics.mode(sums)
except: print("No unique mode")

print("Mean:",  mean, "Median:", median,
"Mode:", mode)



#%% [markdown]
# # <font color='red'>EXERCISE 3</font>
# Write a function `roll_dice()` that takes two arguments in this order: the number of rolls and the number of sides. This function should return a dict with the keys being the possible outcomes for the die, and the values being the number of times that outcome came up, e.g. for 10 sides and 50 rolls, I might get
# ```
# {
#    1: 5,
#    2: 7,
#    ...
#    10: 4,
# }
# ```
# Ensure that all possible outcomes have a corresponding key even if there were no such events recorded.

#%%
n = {1:1, 2:67 }

print(n.values())
print(type(n.values()))
#sum(n.values())

#%%
def roll_dice(rolls, sides):

    stats = {}
    for i in range(1, sides+1):
        stats[i] = 0

    # Iterator
    i = 0
    while i < rolls:
        # Generate random number
        num = random.randint(1, sides)
        # Update frequency
        stats[num] = stats[num] + 1
        i += 1 
    print(stats)
    return stats

roll_dice(30, 15)



#%%
die_rolls = roll_dice(5, 9)
assert isinstance(die_rolls, dict)
assert len(die_rolls) == 9
die_rolls = roll_dice(20, 9)
assert len(die_rolls) == 9
assert sum(die_rolls.values()) == 20

#%% [markdown]
# # Drawing a histogram
# 
# We can draw a very basic (admittedly ugly) histogram using `matplotlib`:

#%%
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

die_rolls = roll_dice(100, 6)

fig, ax = plt.subplots()

ax.bar(die_rolls.keys(), die_rolls.values())

#%% [markdown]
# With a little bit of tweaking, we can make it slightly better:

#%%
def histogram(counts):
    X = [k - 0.4 for k in counts.keys()]
    Y = counts.values()
    fig, ax = plt.subplots()
    ax.bar(X, Y, alpha=0.5)
    
    lower = min(X) - 0.2
    upper = max(X) + 1
    ax.set_xlim([lower, upper])


#%%
histogram(roll_dice(100, 6))

#%% [markdown]
# # <font color='red'>EXERCISE 4</font>
# 
# Write a function `roll_two_dice()` that takes two arguments in this order: the number of rolls and the number of sides. For each iteration, roll two dice with given number of sides and take their sum as the outcome.
# 
# This function should return a dict with the keys being the possible outcomes, and the values being the number of times that outcome occurred, e.g. for 10 sides and 100 rolls, I might get
# ```
# {
#    1: 5,
#    2: 7,
#    ...
#    20: 4,
# }
# ```
# Ensure that all possible outcomes have a corresponding key even if there were zero such events recorded, and that there are no keys for impossible outcomes (e.g. 1 for two six-sided dice).

#%%

# Note: Can't get a sum of 1 when you roll 2 die,
# So the length of the distribution should be 2*sides - 1
# So for 9 sides * 2 rolls = 18 - 1 possibilities

def roll_two_dice(rolls, sides):
    
    d = {}
    # Add possible values
    for j in range(2, (2 * sides) + 1):
        d[j] = 0
    # Generate results
    for i in range(1, rolls+1):
        n1 = random.randint(1, sides)
        n2 = random.randint(1, sides)
        sum = n1 + n2
        if sum not in d.keys():
            d[sum] = 1
        else:
            d[sum] += 1
    return d
        
roll_two_dice(3, 4)

#%%
die_rolls = roll_two_dice(5, 9)
assert isinstance(die_rolls, dict)
assert len(die_rolls) == 17

die_rolls = roll_two_dice(20, 9)
assert len(die_rolls) == 17
assert sum(die_rolls.values()) == 20

#%% [markdown]
# # <font color='red'>EXERCISE 5</font>
#%% [markdown]
# Use the above `histogram()` function to compare the distributions of `roll_dice` and `roll_two_dice` for 500 rolls of 6-sided dice. Try each a few times. What do you notice is consistently different about these two distributions? Draw each histogram and answer the question in text.

#%%
histogram(roll_dice(500, 6))
histogram(roll_two_dice(500, 6))

'''
The shapes of both histograms tend to be the same (relative to the roll-function)

Rolling one die yields a graph that's mostly straight across, or equally distributed
across every possible value

Rolling two dice frequently yields a graph that is somewhat normalized/bell shaped,
with the resulting values lying mostly in the center
'''

#%% [markdown]
# # Node degree distributions
#%% [markdown]
# Recall the NetworkX command to create an Erdos-Renyi random graph:
# ```
# G = nx.erdos_renyi_graph(N, p)
# ```

#%%
import networkx as nx
G = nx.erdos_renyi_graph(12, 0.2)
nx.draw(G, with_labels=True)

#%% [markdown]
# Also recall the `degree()` method which can give the degree for a specific node...

#%%
G.degree(5)

#%% [markdown]
# ...or can return a dict containing the node degrees for every node in the graph:

#%%
G.degree()

#%% [markdown]
# If we want to examine the distribution of node degrees, we don't care about the node names, only the node degrees:

#%%
# list(G.degree().values())
# This doesn't work

# This instead
x = dict(G.degree()) 
x.values()

#%% [markdown]
# We can treat each degree as if it were the outcome of a discrete random variable, like a die roll.
#%% [markdown]
# # <font color='red'>EXERCISE 6</font>
#%% [markdown]
# First, create an ER random graph with $N=100$ and $p=0.1$ and name it `G`. Then use the `histogram()` function to draw a histogram of the node degrees for the graph `G`. Don't worry about filling in "missing" values.
# 
# Also print the mean, median, and mode of the node degree distribution. Execute this a few times.
# 
# **Note:** while `histogram(G.degree())` does draw a plot, that plot is not a histogram. Doing so will result in zero credit for this exercise.

#%%
G = nx.erdos_renyi_graph(100, 0.1)

# Map possible degree values against their frequency for histogram
deg = {}
for node in G:
    if G.degree(node) not in deg:
        deg[G.degree(node)] = 1
    else:
        deg[G.degree(node)] = deg[G.degree(node)] + 1
print(deg)
histogram(deg)

# Raw values
rv = [G.degree(node) for node in G]
# print(rv)
# Summary Stats
mean = statistics.mean(rv)
median = statistics.median(rv)
mode = 0 
try:
    mode = statistics.mode(rv)
except: print("No unique mode")

print("Mean:",  mean, "Median:", median,
"Mode:", mode)


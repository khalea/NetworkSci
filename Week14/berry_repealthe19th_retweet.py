# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

#%%
import gzip
import json

import networkx as nx

#%%
# This could take a few seconds to run.
tweets = []
for line in gzip.open('repealthe19th.jsonl.gz', 'rt'):
    if line:
        tweet = json.loads(line)
        tweets.append(tweet)

#%%
# Question 1 - Find Proportion of Tweets That are RTs
# print(tweets[0]['retweeted_status'])

total = len(tweets)
count = 0

for i in tweets:
    if 'retweeted_status' in i:
        count += 1
rts = round(count/total, 3)

print('There are', count, 'retweets')
print('There are', total, 'total tweets')
print('The proportion of tweets that are RTs is', rts)

#%%
# Questions 2, 3 - Create RT network 
G = nx.DiGraph()

for t in tweets:
    if 'retweeted_status' in t:
        # Original Tweeter
        origUser = t['retweeted_status']['user_screen_name']
        # Retweeter
        rtUser = t['user_screen_name']
        # Ignore self RTs
        if origUser != rtUser:
            # Add edge to graph
            G.add_edge(origUser, rtUser)

# How many nodes and edges are in the RT network?
print('There are', len(G.nodes), 'nodes/users in the RT network')
print('There are', len(G.edges), 'edges/rts in the RT network')

#%%
# Questions 4, 5, 6, 7 - Highest out-degree & in-degree

topSortedOut = sorted(G.nodes, key=G.out_degree, reverse=True)[0]
topSortedIn = sorted(G.nodes(), key=G.in_degree, reverse=True)[0]

print('The user with the highest out-degree is', topSortedOut, 'with', G.out_degree(topSortedOut), 'retweets *from* other users')
print('The user with the highest in-degree is', topSortedIn, 'with', G.in_degree(topSortedIn), 'retweets *of* other users')

secondTopOut = sorted(G.nodes, key=G.out_degree, reverse=True)[1]
print('The user with the SECOND highest out-degree is', secondTopOut, 'with', G.out_degree(secondTopOut), 'retweets *from* other users')


# %%
# Question 8 - Proportion of nodes with zero out-degree, round to 3 decimals

sortedOut = sorted(G.nodes, key=G.out_degree, reverse=True)

zero = 0
nwSize = len(G.nodes)

for u in sortedOut:
    if G.out_degree(u) == 0:
        zero += 1

prop = zero/nwSize
print('The proportion of nodes with 0 out-degree is', round(prop, 3))

# %% [markdown]
# Question 9 -  What could this proportion indicate about this particular network?
The proportion is pretty high, so it would seem that most nodes in this retweet network are not being retweeted. There appear to be a small number of hub nodes that are being retweeted frequently.

# Question 10
C. The user hasn't been retweeted by anyone

# Question 11
Weakly connected

#%% 
# Question 12 - Proportion of nodes in its largest weakly connected component

# Get biggest weakly connected component
maxWeakComp = max(nx.weakly_connected_components(G), key=len)
# Number of items in the component
num = len(list(maxWeakComp))
# Proportion
prop = num/len(G.nodes)
print('The proportion of nodes in the largest weakly connected component is', round(prop, 3))




# %% 
# Question 14 - Most retweeted tweet

# Create dictionary
rtDict = {}

for t in tweets:
    
    # Add all tweet IDs to the dictionary
    tweetID = t['id_str']
    if tweetID not in rtDict.keys():
        rtDict[tweetID] = 1
        # Check if its a retweet & add the original tweet ID to the dictionary
        if 'retweeted_status' in t:
            original = t['retweeted_status']
            # Check if the ID of the original tweet is in rtDict
            if original['id_str'] in rtDict.keys():
                rtDict[original['id_str']] = rtDict[original['id_str']] + 1
            else:
                rtDict[original['id_str']] = 1
    
    else:
        rtDict[tweetID] = rtDict[tweetID] + 1
        
# Find the key/ID with highest RTs
for key, value in rtDict.items():
    if value == max(rtDict.values()):
        print('The most RT\'d user in this set is', key, 'with', value, 'retweets')



# %%
list(sorted(list(nx.strongly_connected_components(G)), key=len, reverse=False))

# %%
sorted(list(nx.weakly_connected_components(G)), key=len, reverse=False)

# %%

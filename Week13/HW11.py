# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Homework 11: Twitter Retweet & Mention networks
# 
# In this assignment, you are to use the Twitter API to do a search for tweets containing a hashtag, then produce retweet and mention networks of the conversation. You are encouraged to reuse code from past tutorials to help you with these exercises.
# 
# The parts of this assignment build on themselves -- you *really* don't want to get stuck early on here. Please get started early and don't be afraid to ask for help.
# 
# ## A note about notebook cells
# 
# Beneath each exercise description there is a single code cell. This is not to suggest that you should do all your work in a single cell. Please create as many as you need via the "Insert" menu in the notebook menu bar.
# 
# Another thing worth noting (as I mentioned in class) the Twitter API is rate limited, so it's worth making your API call in a seperate cell from the code you write to manipulate the result. That will avoid having the API call repeat every time you run the cell as you're debugging. 
# %% [markdown]
# # Exercise: Retweet network
# 
# Here we want to produce a **directed** graph of users **retweeting** each others' tweets.
# 
# (Note - please read this overview of the assignment before diving in - it might be helpful to have a firm idea of each required step before you start) 
# 
# * 1.) Do a search for a hashtag of your choosing, and retrieve at least 1000 tweets. Show that you have at least 1000 tweets.
# 
# * 2.) For each tweet, if the tweet is a retweet, add an edge **from the *retweeted* user to the *retweeting* user**.
# 
# * 3.) Remove selfloop edges and then also subsequently remove singleton nodes. We didn't remove singletons in the tutorial or last assignment, but you should do it here. Your graph should only contain nodes retweeting/retweeted by at least one other user.
# 
# * 4.) Show how many nodes and edges are in this network.
# 
# * 5.) Show the screen name of the user with:
#   * highest in-degree
#   * highest out-degree
#    
#   Also provide each of these degree values.
# 
# * 6.) Draw this network
# 
# * 6.1.) (Extra Credit!) Draw network two more times - first with nodes sized according to in-degree, and then with nodes sized according to out-degree
# 
# * 7.) In the context of Twitter and Twitter users, what does it mean for a user to be a hub with high retweet in-degree? What does it mean for a user to have high retweet out-degree?
# 
# * 8.) What proportion of the nodes in this network are *sinks* (i.e. nodes with zero out-degree)?
# 
# * 8.1) What does it mean for a user to be a sink in this network?
# 
# * 9.) What proportion of the nodes in this network are *sources* (i.e. nodes with zero in-degree)? 
# 
# * 9.1) What does it mean for a user to be a source in this network?
# 
# * 10.) (Extra Credit!) What proportion of the nodes in this network are in its largest weakly-connected component?
# 
# If the network doesn't have very many edges, (use your best judgement) try again but with more tweets, e.g. 2000 instead of 1000 - or a different hashtag. 

#%% 
from IPython import get_ipython
# get_ipython().system('pip install twython')
from twython import Twython

#%%
# Authorization - Keys & Tokens
API_KEY = 'zeo1urAXgj7fTvbmWXCiHDNJU'
API_SECRET_KEY = 'J0FMLysanth3ZmRBvJzejDN6evSZltXuO2pumXUibUdv5JduPp'

twitter = Twython(API_KEY, API_SECRET_KEY)

authentication_tokens = twitter.get_authentication_tokens()
print(authentication_tokens['auth_url'])


#%%
# Authorization - Verifier PIN
VERIFIER = '3279101'

twitter = Twython(API_KEY, API_SECRET_KEY,
                  authentication_tokens['oauth_token'],
                  authentication_tokens['oauth_token_secret'])

authorized_tokens = twitter.get_authorized_tokens(VERIFIER)

#%%
# Authorization - 'Permanent' Tokens 
twitter = Twython(API_KEY, API_SECRET_KEY,
                  authorized_tokens['oauth_token'],
                  authorized_tokens['oauth_token_secret'])

twitter.verify_credentials()


# %% [markdown]
# ## Exericse 1. Do a search for a hashtag of your choosing, and retrieve at least 1000 tweets. Show that you have at least 1000 tweets. 

# %%
import itertools

maxTweets = 1000

cursor = twitter.cursor(twitter.search, q='#Watchmen', count=100, result_type='mixed')
tweets = list(itertools.islice(cursor, maxTweets))
len(tweets)

#%%
# Create Graph
import networkx as nx
G = nx.DiGraph()

# %% [markdown]
# ## 2. For each tweet, if the tweet is a retweet, add an edge **from the *retweeted* user to the *retweeting* user**.

for t in tweets:
    if 'retweeted_status' in t:
        # Retweeter & Author
        rt = t['retweeted_status']
        author = rt['user']['screen_name']
        retweeter = t['user']['screen_name']
        # Add to graph
        G.add_edge(author, retweeter)


print('Total nodes in graph G:', len(G.nodes))
print('Total edges in graph G:', len(G.edges))

# %% [markdown]
# ## 3. Remove selfloop edges and then also subsequently remove singleton nodes. We didn't remove singletons in the tutorial, but you should do it here. Your graph should only contain nodes retweeting/retweeted by at least one other user.
# 

# Create copy of G
C = G.copy()

# Remove self loops
for e in G.edges():
    # Remove self-loops
    if e[0] == e[1]:
        C.remove_edge(e[0], e[1])
        print('Removed SELF LOOP', e)

# Remove singleton nodes 
for n in G.nodes():
    if (len(G.out_edges(n)) == 0) and (len(G.in_edges(n)) == 0):
        print('Removed node', n)
        C.remove_node(n)

# pos = nx.spring_layout(C, k=1)    
# nx.draw(C)


# %% [markdown]
# ## 4. Show how many nodes and edges are in this network.
# 
print('Total nodes in graph C:', len(C.nodes))
print('Total edges in graph C:', len(C.edges))


# %% [markdown]
# ## 5. Show the screen name of the user with:
#   * highest in-degree
#   * highest out-degree
#    
#   Also provide each of these degree values - print this information out in a easily readable format - as demonstrated in the tutorial. 
# 

# %%
from operator import itemgetter
maxIn = sorted(C.in_degree(), key=itemgetter(1), reverse=True)[0]
maxOut = sorted(C.out_degree(), key=itemgetter(1), reverse=True)[0]

print('Maximum In-Degree user is', maxIn[0], 'with degree', maxIn[1])
print('Maximum Out-Degree user is', maxOut[0], 'with degree', maxOut[1])

# %% [markdown]
# ## 6. Draw this network
nx.draw_spring(C)


# %% [markdown]
# ## 6.1 (Extra credit!) 
# 
# Draw the network two more times - first with nodes sized by in-degree, and then with nodes sized by out-degree. 

# %%
# Nodes sized by in-degree


# %%
# Nodes sized by in-degree

# %% [markdown]
# ## 7. In the context of Twitter and Twitter users, what does it mean for a user to be a hub with high retweet in-degree? What does it mean for a user to have high retweet out-degree?
# 
# %% [markdown]
# If a user has a high retweet in-degree, it means that they are retweeting quite frequently. Since edges are directed from the tweet author to the retweeter, the in-degree indicates the number of unique individuals that they have retweeted.
# 
# If a user has a high retweet out-degree, then they are someone who gets retweeted quite a bit, and may be influential in some way or another.  
# %% [markdown]
# ## 8. What proportion of the nodes in this network are *sinks* (i.e. nodes with zero out-degree)? 
#  

# %%
total = len(C.nodes)
zeroOut = 0

for i in C.nodes:
    if C.out_degree(i) == 0:
        zeroOut += 1

print((zeroOut/total), 'nodes are *sinks*')

# %% [markdown]
# ## 8.1 What does it mean for a user to be a sink in this network? 
# %% [markdown]
# Users in this network are sinks if they do not get retweeted by other users.
# %% [markdown]
# ## 9. What proportion of the nodes in this network are *sources* (i.e. nodes with zero in-degree)? 

# %%
total = len(C.nodes)
zeroIn = 0

for i in C.nodes:
    if C.in_degree(i) == 0:
        zero += 1

print((zeroIn/total), 'nodes are *sources*')

# %% [markdown]
# ## 9.1 What does it mean for a user to be a source in this network?
# %% [markdown]
# If a user in this network is a source, it indicates that they do not do not retweet others.
# %% [markdown]
# ## 10. (Extra Credit!)  What proportion of the nodes in this network are in its largest weakly-connected component?

# %%



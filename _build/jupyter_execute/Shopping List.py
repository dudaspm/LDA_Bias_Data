#!/usr/bin/env python
# coding: utf-8

# # Let's create a shopping list!

# ## First, let's just create a list

# In[1]:


shoppingList = []


# Let's create a function to add new items to my shopping list.

# In[2]:


def addToShoppingList(itemToAdd):
    shoppingList.append(itemToAdd)


# Walking around my kitchen I notice we are missing milk.

# In[3]:


addToShoppingList("milk")


# We have 3 eggs left (always want 6 on hand).

# In[4]:


numberOfEggs = 3
if (numberOfEggs < 6): addToShoppingList("eggs")


# I want to make spaghetti for dinner (need sauce, spaghetti, and bread).

# In[5]:


spaghettiRecipe = ["sauce","spaghetti","bread"]
for ingredient in spaghettiRecipe:
    addToShoppingList(ingredient)


# Let's see what we have so far.

# In[6]:


print( shoppingList )


# Not the easiest to read. Let's try this another way:

# In[7]:


for item in shoppingList:
    print( item )


# ## Second, let's add some prices

# So I want to keep an eye on my budget, so I note all the prices.

# First, I will set all prices to 0.

# In[8]:


shoppingPrices = {}
for item in shoppingList:
    shoppingPrices[item] = 0
print( shoppingPrices )


# Now I will manually add prices for each item.

# In[9]:


shoppingPrices['spaghetti'] = .99
shoppingPrices['eggs'] = 1.99
shoppingPrices['sauce'] = 2.15
shoppingPrices['milk'] = 2.85
shoppingPrices['bread'] = 1.49


# In[10]:


print( shoppingPrices )


# Also, I don't want to manually put in values. 
# 
# For this example, I will just use random values. Let's see an example of how to do this:

# In[11]:


# first, import the random library
import random
# to create a random integer, use randint and the range (lowest values, highest values (-1))
print( random.randint(1,21) )
# now make this into a decimal price
# example for eggs, let's assume the price can go from 1.50 to 2.50 (NOTE the 251)
print( random.randint(150,251)/100 )


# why are we only getting two options (1 or 2)? 
# 
# We need a decimal! So let's type-cast using float().

# In[12]:


print( random.randint(150,251)/float(100) )
print( random.randint(150,251)/float(100) )
print( random.randint(150,251)/float(100) )
print( random.randint(150,251)/float(100) )


# Let's define are ranges:
# -  Spaghetti (.75 - 1.00)
# -  Eggs (1.50 - 2.50)
# -  Sauce (2.00 - 3.00)
# -  Milk (2.50 - 4.00)
# -  Bread (1.25 - 1.75)

# In[13]:


def createRandomPrice(item):
    if (item=="spaghetti"): return random.randint(75,100)/float(100)
    if (item=="eggs"): return random.randint(150,250)/float(100)
    if (item=="sauce"): return random.randint(200,300)/float(100)
    if (item=="milk"): return random.randint(250,400)/float(100)
    if (item=="bread"): return random.randint(125,175)/float(100)


# ## Third, some serious code here

# Idea!! I will go to multiple stores to get the best prices!
# 
# Here is what I need:
# 
# We will need a list of stores (Wegmans, Wal-Mart, Giant, Trader Joes).
# 
# For each store, we will need a list of the stores and our shopping list.
# 
# Let's start with our store names:

# In[14]:


storeNames = ["Wegmans","Wal-Mart","Giant","Trader Joes"]


# In[15]:


for storeName in storeNames:
    print( storeName )


# OK, let's test this:

# In[16]:


for item in shoppingList:
    print( item, createRandomPrice( item ) )


# This is what we want in the end. For each store, we have a price for each item.

# | food | Wegmans | Wal-Mart | Giant | Trader Joes |
# |------|------|------|------|------|
# | spaghetti |  x.xx  |  x.xx |  x.xx  | x.xx |
# | eggs |  x.xx  |  x.xx |  x.xx  |  x.xx |
# | sauce |  x.xx  |  x.xx |  x.xx  |  x.xx |
# | milk |  x.xx  |  x.xx |  x.xx  |  x.xx |
# | bread |  x.xx  |  x.xx |  x.xx  |  x.xx |

# First, we need a Dictionary for each item and for each item another Dictionary for the store/prices.

# In[17]:


shoppingPricesByStores = {}
for item in shoppingList:
    shoppingPricesByStores[item] = {}
print( shoppingPricesByStores )


# Now for each item, we set both the store name and the random price. 

# In[18]:


for item in shoppingPricesByStores:
    shoppingPricesByStores[item] = {}
    for storeName in storeNames:
        shoppingPricesByStores[item][storeName] = createRandomPrice(item)
print( shoppingPricesByStores )


# Finally, we need to sort. We use a sorting function (sorted). 
# 
# Let's try first with just sorted (shoppingPricesByStores[item]).

# In[19]:


print( sorted( shoppingPricesByStores ) )


# Hmm... not what we are looking for. We want to sort based on prices per store.

# In[20]:


for item in shoppingPricesByStores:
    print( item )
    print( sorted( shoppingPricesByStores[item] ) )


# This is sorting based on the name of the store; we need to sort based on the amount.

# There is actually a function we can use, called items(), which as it sounds, gives us all items in our dictionary.

# In[21]:


shoppingPricesByStores.items()


# So let's try using that. 

# In[22]:


for item in shoppingPricesByStores:
    print( item )
    print( shoppingPricesByStores[item] )
    print( sorted( shoppingPricesByStores[item].items() ) )


# First, I will define a function (I will explain this more in a second). 
# 
# Also, I marked a couple of print statements to showcase what is going on. 
# 
# All this function does is take tuple and returns the second item in the tuple. 
# 
# REMEMBER, computer talk here.. 1 = 2, because it starts at 0, 1, 2,...

# In[23]:


def comparePrices (itemToSort):
    print( "#From comparePrices function#" )
    print( itemToSort )
    print( "At the store "+itemToSort[0]+" the price is "+str( itemToSort[1] ) )
    print( "#End comparePrices function#" )
    return itemToSort[1]


# We can add a "key" that tells the sorting function, which value to sort on. 
# 
# So reading this in more non-technical speak:
# 
# 1.  For each item in dictionary called shoppingPricesByStores
# 2.  Print item name
# 3.  Then sort by the pair (storeName and price)
# 4.  Use the function comparePrices to tell sorting to sort by the price. 

# In[24]:


for item in shoppingPricesByStores:
    print( "####################In for loop####################" )
    print( item )
    print( sorted(shoppingPricesByStores[item].items(), key=comparePrices) )
    print( "####################Out for loop####################" )


# We can short-hand this a bit by using lambda.
# 
# Lambda is like a micro-function. We use it once and that's it.

# In[25]:


for item in shoppingPricesByStores:
    print( item )
    print( sorted(shoppingPricesByStores[item].items(), key=lambda storeAmount: storeAmount[1] ) ) # Python 3
    #print( sorted(shoppingPricesByStores[item].items(), key=lambda (store,amount): (amount)) ) # Python 2


# Let's print this out a bit neater.

# In[26]:


for item in shoppingPricesByStores:
    print( item )
    #for key, value in sorted(shoppingPricesByStores[item].items(), key=lambda (store,amount): (amount)): # Python 2
    for key, value in sorted(shoppingPricesByStores[item].items(), key=lambda storeAmount: storeAmount[1] ): # Python 3
        print( "%s: %s" % (key, value) )
    print( "\n" )


# In[ ]:





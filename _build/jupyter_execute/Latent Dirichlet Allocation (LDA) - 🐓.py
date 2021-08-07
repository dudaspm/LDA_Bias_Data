#!/usr/bin/env python
# coding: utf-8

# # Topic Modeling - 🐓

# ![Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-h/images/cover.jpg)
# 
# > Alice's Adventures in Wonderland {cite:p}`Carroll` via https://www.gutenberg.org/files/11/11-h/11-h.htm

# To start our discussion, we should introduce what Topic Modeling is and how it can be applied. 

# :::{note}
# "Topic modeling is a princpled approach for discovering topics from a large corpus of text documents {cite:p}`liu2020sentiment` (pg.159)."
# :::
# 
# 

# Already, we have few things to unpack. What are topics? How are the defined? Do we define or does the computer? What is a large corpus? How many documents do we need?
# 
# 
# Let's start with a *large corpus of text documents*. Typically, we would have two documents 📄, five documents 📄, ten million documents 📄, can be thought of as our corpus. Yes, even 1 document 📄 can be used for topic modeling. So, defining, *large corpus of text documents*, can be subjective. 
# 
# As specified by Liu {cite:p}`liu2020sentiment` we can start this conversation using one of the two basic types of topic modeling. This being *probablistic Latent Dirichlet Allocation* or *Latent Dirichlet Allocation*. For our conversation, we will be using *Latent Dirichlet Allocation*. 
# 
# 
# 
# 

# ## Latent Dirichlet Allocation
# 
# ### Pronunciation
# 
# #### Latent
# <audio controls>
#   <source src="https://github.com/dudaspm/LDA_Bias_Data/blob/main/audio/Latent.mp3?raw=true"
#           type="audio/mp3">
# Your browser does not support the audio element.
# </audio>
# 
# #### Dirichlet
# <audio controls>
#   <source src="https://github.com/dudaspm/LDA_Bias_Data/blob/main/audio/Dirichlet.mp3?raw=true"
#           type="audio/mp3">
# Your browser does not support the audio element.
# </audio>
# 
# #### Allocation
# <audio controls>
#   <source src="https://github.com/dudaspm/LDA_Bias_Data/blob/main/audio/Allocation.mp3?raw=true"
#           type="audio/mp3">
# Your browser does not support the audio element.
# </audio>
# 
# Our pronoucation stems from a talk by David Blei who is a professor of Statistics and Computer Science at Columbia University during David's talk "Probabilistic Topic Models and User Behavior {cite:p}`Blei_2017`." The citation provides a link to original YouTube video (which is a *great* resource), but specifically, helpful for the pronouciation. 
# 

# ## What is Latent Dirichlet Allocation or LDA?
# 
# LDA is an unsupervised learning model. 

# :::{note}
# 
# Topic Modeling with Documents  📄           
#             
# * supervised - Our documents 📄 are pre-labeled with the given topic(s). We can then train 🏋️ and test 🧪 (and also, you can include validate). **Usually** this is split:
#     * training 🏋️ 80% 
#     * testing 🧪 20%. 
#             
#    
# * unsupervised - Data is not labeled. So, we have no idea what the topics are beforehand. That being said, we can (and will) define the *number of topics*. 
# 
# :::
# 

# So, coming back to our original questions:
# * What are topics? 
#     * The topics will X number of sets of terms (we define this X) which will (could) have a common theme. 
# * How are they defined? 
#     * This is what we will get to in this notebook.     
# * Do we define or does the computer? 
#     * LDA is unsupervised, so we define the number of topics. The computer provides the topics themselves. 
# * What is a large corpus? and How many documents do we need? 
#     * A bit subjective here. There is a *great* discussion about this by Tang et al.  {cite:p}`tang2014understanding` regarding this. If you have chance, read all the points, but to sum it up
#         * The number of documents does matter, but at some point, increasing the number does not warrent better results. Even sampling a 1000 papers from 1000000 papers could result in the same, if not, better results than using 1000000 documents. 
#         * The size of the documents also plays a role, so documents should not be short. Larger documents can be sampled and again, receive the same desired output. 
# 
# 

# ## 

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/files/11/11-h/11-h.htm"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()
print (type(text))


# In[2]:


import pandas as pd
import re
import numpy as np
import random 

from sklearn.feature_extraction.text import CountVectorizer
textArray = text.lower().split(" ")
print(len(textArray))
documents = []

print (random.choices(["sadf","asdf","Aewrwe"], k = 2))
for i in range(27):
    documents.append(" ".join(textArray[i*1000:(i+1)*1000]))

print(documents[10][0:100])
cv = CountVectorizer()
# tokenize and build vocab
df = cv.fit_transform(documents)



# In[68]:


from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components = 5, random_state = 42)
lda.fit(df)


# In[69]:


for index, topic in enumerate(lda.components_):
    print(f'Top 15 words for Topic #{index}')
    print([cv.get_feature_names()[i] for i in topic.argsort()[-15:]])
    print('\n')


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Latent Dirichlet Allocation (LDA)

# ![The Wonderful Wizard of Oz](https://www.gutenberg.org/files/55/55-h/images/cover.jpg)
# 
# > The Wonderful Wizard of Oz {cite:p}`Baum` via https://www.gutenberg.org/ebooks/55

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

# ### A Picture == 1000 Words
# 
# One of the best representations of what LDA is and how to utilize it, can be found in Blei's work *Probabilistic topic models* {cite:p}`blei2012probabilistic` Please note, that images and figure text come directly from the work. All credit should go to Blei {cite:p}`blei2012probabilistic`
# 
# ![The intuitions behind latent Dirichlet allocation](http://deliveryimages.acm.org/10.1145/2140000/2133826/figs/f1.jpg)
# "Figure 1. The intuitions behind latent Dirichlet allocation. We assume that some number of "topics," which are distributions over words, exist for the whole collection (far left). Each document is assumed to be generated as follows. First choose a distribution over the topics (the histogram at right); then, for each word, choose a topic assignment (the colored coins) and choose the word from the corresponding topic. The topics and topic assignments in this figure are illustrative—they are not fit from real data. {cite:p}`blei2012probabilistic` (Page 3)"
# 
# ![Real inference with LDA](https://deliveryimages.acm.org/10.1145/2140000/2133826/figs/f2.jpg)
# "Figure 2. Real inference with LDA. We fit a 100-topic LDA model to 17,000 articles from the journal Science. At left are the inferred topic proportions for the example article in Figure 1. At right are the top 15 most frequent words from the most frequent topics found in this article. {cite:p}`blei2012probabilistic` (Page 4)"

# ## Let's Try an Example

# For our example, we will be using a subset of books from L. Frank Baum that are part of the public-domain (again, thank you https://www.gutenberg.org).
# 
# * The Wonderful Wizard of Oz
#     * https://www.gutenberg.org/files/55/55-h/55-h.htm
# * The Marvellous Land of Oz
#     * https://www.gutenberg.org/files/54/54-h/54-h.htm
# * Ozma of Oz
#     * https://www.gutenberg.org/files/33361/33361-h/33361-h.htm
# * Dorothy and the Wizard in Oz 
#     * https://www.gutenberg.org/files/22566/22566-h/22566-h.htm
# * The Road to Oz
#     * https://www.gutenberg.org/files/26624/26624-h/26624-h.htm # 

# The books are all in the public domain and the HTML can be found at https://www.gutenberg.org/.
# We will go through one example of how to get the text from the book using Python. Please note, this will not be the most optimal way to do this but we hope we can make the process clear for you to try with other books or manuscripts. 
# 
# ### Get the HTML for the Book
# 
# We are going to use two libaries for this, one is a standard for python called. 
# 
# ```python
# import urllib
# ```
# the other is a favorite of ours, called beautiful soup {cite:p}`BeautifulSoup`. 
# 
# ```python
# from bs4 import BeautifulSoup
# ```
# 
# urllib will get the document and BeautifulSoup makes it easy to parse. 

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/files/55/55-h/55-h.htm" 
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")


# Here we are remove any CSS (style) or JavaScript (script)

# In[2]:


for script in soup(["script", "style"]):
    script.extract()


# Finally, get the text and add it to our document list. 

# In[3]:


text = soup.get_text()
documents = []
documents.append(text)


# We will repeat this process for the other four books. 

# In[4]:


url = "https://www.gutenberg.org/files/54/54-h/54-h.htm" 
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
documents.append(text)

url = "https://www.gutenberg.org/files/33361/33361-h/33361-h.htm" 
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
documents.append(text)

url = "https://www.gutenberg.org/files/22566/22566-h/22566-h.htm" 
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
documents.append(text)

url = "https://www.gutenberg.org/files/26624/26624-h/26624-h.htm" 
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text()
documents.append(text)


# ### Create Tokens and Vocabulary
# 
# Now that we have our books, we need to tokensize the stories by word and then create a vocabular out of these tokens. sklearn is fantastic library that we will be using through-out the notebook {cite:p}`sklearn_api`.

# In[5]:


get_ipython().run_cell_magic('capture', '', '!pip install sklearn')


# In[6]:


from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
df = cv.fit_transform(documents)
vocab = cv.get_feature_names()


# Let's take a look at the tokens and the number of occurance for the tokens. 

# In[7]:


print (df[0])


# The second number listed, is the token number and we use the vocab list to see what the actual word. An example would be to look at the first line. 
# 
# ```python
# (0, 8074) 3198
# ```
# The 8074 token was used 3198 times. The 8074 token is:

# In[8]:


print (vocab[8074])


# Not that surprising the word "the" is used that many times. 

# :::{note}
# 
# Because there are many commonly used terms. We would want to remove these words from our dataset. These words are called *stopwords* and should be removed. We do showcase this later.  
# 
# :::

# From here, we are actually at the point where we can run LDA.
# 
# There are much more than two inputs available for LDA, but we will focus on two. 
# > Here are the other inputs: https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html
# 
# The two we will focus on are:
# 
# * n_components - the number of topics, again, we need to specify this
# * doc_topic_prior - this relates the Dirichlet distribution (the next notebook goes into full detail about Dirichlet and how it relates to LDA. 
# 

# In[9]:


from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components = 4, doc_topic_prior=1)
lda.fit(df)


# To print out the top-5 words per topic, we used a solution from StackOverflow {cite:p}`python_LDA`

# In[10]:


topic_words = {}
n_top_words = 10
for topic, comp in enumerate(lda.components_):
    # for the n-dimensional array "arr":
    # argsort() returns a ranked n-dimensional array of arr, call it "ranked_array"
    # which contains the indices that would sort arr in a descending fashion
    # for the ith element in ranked_array, ranked_array[i] represents the index of the
    # element in arr that should be at the ith index in ranked_array
    # ex. arr = [3,7,1,0,3,6]
    # np.argsort(arr) -> [3, 2, 0, 4, 5, 1]
    # word_idx contains the indices in "topic" of the top num_top_words most relevant
    # to a given topic ... it is sorted ascending to begin with and then reversed (desc. now)    
    word_idx = np.argsort(comp)[::-1][:n_top_words]

    # store the words most relevant to the topic
    topic_words[topic] = [vocab[i] for i in word_idx]
    
for topic, words in topic_words.items():
    print('Topic: %d' % topic)
    print('  %s' % ', '.join(words))


# Looking at this, we do not get a clear picture of the topics. This time, let's remove those stopwords and see how important 🧼cleaning the data can be🧼! 

# In[195]:


from sklearn.feature_extraction.text import CountVectorizer

# we can add this to the tokenization step
cv = CountVectorizer(stop_words='english')
df = cv.fit_transform(documents)
vocab = cv.get_feature_names()


# In[196]:


from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components = 4, doc_topic_prior=1)
lda.fit(df)


# In[197]:


topic_words = {}
n_top_words = 10
for topic, comp in enumerate(lda.components_):
    # for the n-dimensional array "arr":
    # argsort() returns a ranked n-dimensional array of arr, call it "ranked_array"
    # which contains the indices that would sort arr in a descending fashion
    # for the ith element in ranked_array, ranked_array[i] represents the index of the
    # element in arr that should be at the ith index in ranked_array
    # ex. arr = [3,7,1,0,3,6]
    # np.argsort(arr) -> [3, 2, 0, 4, 5, 1]
    # word_idx contains the indices in "topic" of the top num_top_words most relevant
    # to a given topic ... it is sorted ascending to begin with and then reversed (desc. now)    
    word_idx = np.argsort(comp)[::-1][:n_top_words]

    # store the words most relevant to the topic
    topic_words[topic] = [vocab[i] for i in word_idx]
    
for topic, words in topic_words.items():
    print('Topic: %d' % topic)
    print('  %s' % ', '.join(words))


# Much better!

# ## Moving On
# 
# In the next section, we spend a good amount of time talking about the Dirichlet distribution and how it relates to LDA. 

# In[ ]:





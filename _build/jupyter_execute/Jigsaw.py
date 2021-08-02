#!/usr/bin/env python
# coding: utf-8

# # Section 2: Implementation of LDA

# To further understand the importance of topic modeling, we will be looking into a public dataset, i.e. the Jigsaw Unintended Bias dataset. 
# 
# 
# This dataset consists of ~2m public comments from the Civil Comment platform so that researchers could understand and improve civility in online conversations. These comments are then annotated by human raters for various toxic conversational attributes. Additional labels related to sociodemographic identifiers were mentioned to help a machine understand bias better, based on context analysis. But we will see the utility of this dataset and the presence of potential bias in these conversations related to people with physical, mental and learning disabilites. 

# We have filtered all the comments that have been provided a value for the parameters of 'Intellectual or Learning Disability'. 'Psychiatric or Mental Illness'. 'Physical Disability' & 'Other Disability'. We now have 18665 statements in this corpus. 
# The dataset therefore contains statements pertained to these parameters. We can assume that these statements might most likely take about people with disability, but with the help of topic modeling, we can confirm this. 

# We will import the necessary libraries here

# In[1]:


import pandas as pd
import re
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


import sklearn



import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import nltk
lemmatizer = WordNetLemmatizer()

from sklearn.decomposition import LatentDirichletAllocation


# ##### We will be reading the data into a dataframe for easy analysis.

# In[4]:


df = pd.read_csv(r'PWD.csv')


# This is how the data looks like:

# In[5]:


df.head()


# Below are just a few of the comments in this group. You can view more comments by changing the parameter in the 'head' function.
# ##### Warning: Some comments may have explicit language

# In[13]:


pd.set_option('display.max_colwidth', None)
df.comment_text.head(3)


# ##### Lets try removing unnecessary words and cleaning the statements for analysis of topics.

# In[11]:


nltk.download('stopwords')


# In[12]:


my_stopwords = nltk.corpus.stopwords.words('english')
word_rooter = nltk.stem.snowball.PorterStemmer(ignore_stopwords=False).stem
my_punctuation = '!"$%&\'()*+,-./:;<=>?[\\]^_`{|}~•@'

# cleaning master function
def clean_tweet(tweet, bigrams=False):
    tweet = tweet.lower() # lower case
    tweet = re.sub('['+my_punctuation + ']+', ' ', tweet) # strip punctuation
    tweet = re.sub('\s+', ' ', tweet) #remove double spacing
    tweet = re.sub('([0-9]+)', '', tweet) # remove numbers
    tweet_token_list = [word for word in tweet.split(' ')
                            if word not in my_stopwords] # remove stopwords

    tweet_token_list = [word_rooter(word) if '#' not in word else word
                        for word in tweet_token_list] # apply word rooter
    if bigrams:
        tweet_token_list = tweet_token_list+[tweet_token_list[i]+'_'+tweet_token_list[i+1]
                                            for i in range(len(tweet_token_list)-1)]
    tweet = ' '.join(tweet_token_list)
    return tweet


t = []
df['clean_tweet'] = df.comment_text.apply(clean_tweet)


# ##### We will be converting the statements to a vector format for the machine to understand. 

# In[14]:


from sklearn.feature_extraction.text import CountVectorizer

# the vectorizer object will be used to transform text to vector form
vectorizer = CountVectorizer(max_df=0.99, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')

# apply transformation
tf = vectorizer.fit_transform(df['clean_tweet']).toarray()

# tf_feature_names tells us what word each column in the matric represents
tf_feature_names = vectorizer.get_feature_names()


# ##### For the current analysis, lets define the machine to extract 10 unique topics from the dataset (You can play around with the number of topics.).

# In[15]:


number_of_topics = 10

model = LatentDirichletAllocation(n_components=number_of_topics, random_state=0)


# ##### Here, the machine performs the topic modelling analysis. (This might take a little while)

# In[16]:


model.fit(tf)


# In[17]:


#Function to display the topics generated.
def display_topics(model, feature_names, no_top_words):
    topic_dict = {}
    for topic_idx, topic in enumerate(model.components_):
        topic_dict["Topic %d words" % (topic_idx)]= ['{}'.format(feature_names[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
        topic_dict["Topic %d weights" % (topic_idx)]= ['{:.1f}'.format(topic[i])
                        for i in topic.argsort()[:-no_top_words - 1:-1]]
    return pd.DataFrame(topic_dict)


# ##### The below topics show the most significant word in each topic. With further analysis, we can understand the behaviour of the dataset and type of conversations that occur in them. 
# Try changing the no_top_words variable to show more or less words in each topic.

# In[40]:


no_top_words = 15
display_topics(model, tf_feature_names, no_top_words)


# We can go through the topics achieved to understand the most common conversations that occur in this dataset. We will be looking into this content in detail in the following section. 

# # Now to the analysis!
# ## Click \<insert Page name>

# In[ ]:





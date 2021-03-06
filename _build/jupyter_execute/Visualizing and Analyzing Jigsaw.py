#!/usr/bin/env python
# coding: utf-8

# # Visualizing and Analyzing Jigsaw

# In[1]:


import pandas as pd
import re
import numpy as np


# In the previous section, we explored how to generate topics from a textual dataset using LDA. But how can this be used as an application? 
# 
# Therefore, in this section, we will look into the possible ways to read the topics as well as understand how it can be used.

# We will now import the preloaded data of the LDA result that was achieved in the previous section. 

# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/dudaspm/LDA_Bias_Data/main/topics.csv")


# In[3]:


df.head()


# We will visualize these results to understand what major themes are present in them.  

# In[4]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/story/941631/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/story/941631/?utm_source=embed&utm_campaign=story/941631' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# ### An Overview of the analysis 
# From the above visualization, an anomaly that we come across is that the dataset we are examining is supposed to be related to people with physical, mental, and learning disabilities. But unfortunately, based on the topics that were extracted, we notice just a small subset of words that are related to this topic. 
# Topic 2 has words that address themes related to what we were expecting the dataset to have. But the major theme that was noticed in the Top 5 topics are main terms that are political. 
# (The Top 10 topics show themes related to Religion as well, which is quite interesting.)
# LDA hence helped in understanding what the conversations the dataset consisted. 

# From the word collection, we also notice that there were certain words such as \'kill' that can be categorized as \'Toxic'\. To analyze this more, we can classify each word because it can be categorized wi by an NLP classifier. 

# To demonstrate an example of a toxic analysis framework, the below code shows the working of the Unitary library in python. {cite}`Detoxify`
# 
# This library provides a toxicity score (from a scale of 0 to 1) for the sentence that is passed through it.

# In[5]:


headers = {"Authorization": f"Bearer api_ZtUEFtMRVhSLdyTNrRAmpxXgMAxZJpKLQb"}


# To get access to this software, you will need to get an API KEY at https://huggingface.co/unitary/toxic-bert
# Here is an example of what this would look like.
# ```python
# headers = {"Authorization": f"Bearer api_XXXXXXXXXXXXXXXXXXXXXXXXXXX"}
# ```

# In[6]:


import requests

API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# In[7]:


query({"inputs": "addict"})


# You can input words or sentences in \<insert word here>, in the code, to look at the results that are generated through this.
# 
# This example can provide an idea as to how ML can be used for toxicity analysis.

# In[8]:


query({"inputs": "<insert word here>"})


# In[9]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/story/941681/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/story/941681/?utm_source=embed&utm_campaign=story/941681' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# #### The Bias
# The visualization shows how contextually toxic words are derived as important words within various topics related to this dataset. These toxic words can lead to any Natural Language Processing kernel learning this dataset to provide skewed analysis for the population in consideration, i.e., people with mental, physical, and learning disabilities. This can lead to very discriminatory classifications. 

# ##### An Example
# To illustrate the impact better, we will be taking the most associated words to the word 'mental' from the results. Below is a network graph that shows the commonly associated words. It is seen that words such as 'Kill' and 'Gun' appear with the closest association. This can lead to the machine contextualizing the word 'mental' to be associated with such words. 

# In[10]:


get_ipython().run_cell_magic('html', '', "<iframe src='https://flo.uri.sh/visualisation/6867000/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/6867000/?utm_source=embed&utm_campaign=visualisation/6867000' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# It is hence essential to be aware of the dataset that is being used to analyze a specific population. With LDA, we were able to understand that this dataset cannot be used as a good representation of the disabled community. To bring about a movement of unbiased AI, we need to perform such preliminary analysis and more not to cause unintended discrimination. 

# ## The Dashboard
# 
# Below is the complete data visualization dashboard of the topic analysis. Feel feel to experiment and compare various labels to your liking. 

# In[11]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/visualisation/6856937/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/6856937/?utm_source=embed&utm_campaign=visualisation/6856937' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# ## Thank you!
# 
# We thank you for your time! 

#!/usr/bin/env python
# coding: utf-8

# # Section 3: Application of LDA - A Biased Percpective

# In[1]:


import pandas as pd
import re
import numpy as np


# In[ ]:





# In the previous section, we explored how to generate topics from a textual dataset using LDA. But how can this be used as an application? <br> Therefore, in this section, we will look into the possible ways to read the topics as well as understand how it can be used.

# In[ ]:





# We will now import the preloaded data of the LDA result that was achieved in the previous section. 

# In[2]:


df = pd.read_csv("topics.csv")


# In[32]:


df


# In[ ]:





# We shall try visualizing these results to understand what they talk about and what major themes are present in them. With the help of Jupyter Books, we can now embedd not just python code but HTML based projects as well. 

# In[35]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/story/941631/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/story/941631/?utm_source=embed&utm_campaign=story/941631' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# ### An Overview of the analysis 
# From the above visualization, an anomaly that we come across is that the database we are examining is supposed to be related to people with physical, mental and learning disability. But unfortunately based on the topics that were extracted, we notice just a small subset of words that are related to this topic. 
# Topic 2 have words that addresses themes related to what we were expecting the dataset to have. But the major theme that was noticed in the Top 5 topics are mainly terms that are political. 
# (The Top 10 topics show themes related to Religion as well, which is quite interesting.)
# LDA hence helped in understanding what the conversations the dataset consisted. 

# From the word collection, we also notice that there were certain words such as \'kill' that can be categorized as \'Toxic'\. To analyse this more, we cn classify each word based on the fact that it can be categorized as toxic by an NLP classifier. 

# In[ ]:





# ##### To demonstrate an example of a toxic analysis framework, the below code shows the working of the Unitary library in python. <br> 
# This library provides a toxicity score (from a scale of 0 to 1) for the sentece that is passed through it.

# In[13]:


{
    "tags": [
        "hide-cell"
    ]
}

import requests

API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
headers = {"Authorization": f"Bearer api_ZtUEFtMRVhSLdyTNrRAmpxXgMAxZJpKLQb"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


# In[16]:


query({"inputs": "addict"})


# In[ ]:





# You can input words or sentences in \<insert word here>, in the code, to look at the results that are generated through this. <br> This example can provide an idea as to how ML can be used for toxicity analysis.

# In[9]:


query({"inputs": "<insert word here>"})


# In[36]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/story/941681/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/story/941681/?utm_source=embed&utm_campaign=story/941681' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# #### The Bias
# The visualization shows how contextually toxic words are derived as important words within various topics related to this dataset. This can lead to any Natural Language Processing kernel to learning this dataset to provide skewed analysis for the population in consideration, i.e. people with mental, physical and learning disability. This can lead to very discriminatory classifications. 

# ##### An Example
# To illustrate the impact better, we will be taking the most associated words to the word 'mental' from the results. Below is a network graph that shows the commonly associated words. It is seen that words such as 'Kill' and 'Gun' appear with the closest association. This can lead to the machine contextualizing the word 'mental' to be associated with such words. 

# In[17]:


get_ipython().run_cell_magic('html', '', "<iframe src='https://flo.uri.sh/visualisation/6867000/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/6867000/?utm_source=embed&utm_campaign=visualisation/6867000' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# It is hence important to be aware of the dataset that is being used to analyse a specific population. With LDA, we were able to understand that this dataset cannot be used as a good representation of the disabled community. To bring about a movement of unbiased AI, we need to perform such preliminary analysis and more, to not cause unintended descrimination. 

# In[ ]:





# ##### The dashboard
# 
# Below is the complete data visaulization dashboard of the topic analysis. Feel feel to experiment and compare various labels to your liking. 

# In[18]:


get_ipython().run_cell_magic('html', '', "\n<iframe src='https://flo.uri.sh/visualisation/6856937/embed' title='Interactive or visual content' class='flourish-embed-iframe' frameborder='0' scrolling='no' style='width:100%;height:600px;' sandbox='allow-same-origin allow-forms allow-scripts allow-downloads allow-popups allow-popups-to-escape-sandbox allow-top-navigation-by-user-activation'></iframe><div style='width:100%!;margin-top:4px!important;text-align:right!important;'><a class='flourish-credit' href='https://public.flourish.studio/visualisation/6856937/?utm_source=embed&utm_campaign=visualisation/6856937' target='_top' style='text-decoration:none!important'><img alt='Made with Flourish' src='https://public.flourish.studio/resources/made_with_flourish.svg' style='width:105px!important;height:16px!important;border:none!important;margin:0!important;'> </a></div>")


# In[ ]:





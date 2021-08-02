#!/usr/bin/env python
# coding: utf-8

# # Using Pandas to Work with Data

# Why are we using Pandas? 
# 
# * Pandas us to quickly get our comma seperated value (csv) file. 
# 
# * Fill in missing values or NAs 
# 
# * Allow us the ability to preview the date (.head())
# 
# * Filter our data
# 
# 
# 

# In[1]:


import pandas as pd


# In[2]:


url="https://gist.githubusercontent.com/dudaspm/e518430a731ac11f52de9217311c674d/raw/4c2f2bd6639582a420ef321493188deebc4a575e/StateCollege2000-2020.csv"
data = []
data=pd.read_csv(url)
data = data.fillna(0) # replace all NAs with 0s


# In[3]:


data.head()


# ### Acknowledgement 
# 
# <cite>Cite as: Menne, Matthew J., Imke Durre, Bryant Korzeniewski, Shelley McNeal, Kristy Thomas, Xungang Yin, Steven Anthony, Ron Ray, Russell S. Vose, Byron E.Gleason, and Tamara G. Houston (2012): Global Historical Climatology Network - Daily (GHCN-Daily), Version 3. CITY:US420020. NOAA National Climatic Data Center. doi:10.7289/V5D21VHZ 02/22/2021. 
# 
# Publications citing this dataset should also cite the following article: Matthew J. Menne, Imke Durre, Russell S. Vose, Byron E. Gleason, and Tamara G. Houston, 2012: An Overview of the Global Historical Climatology Network-Daily Database. J. Atmos. Oceanic Technol., 29, 897-910. doi:10.1175/JTECH-D-11-00103.1. 
# 
# Use liability: NOAA and NCEI cannot provide any warranty as to the accuracy, reliability, or completeness of furnished data. Users assume responsibility to determine the usability of these data. The user is responsible for the results of any application of this data for other than its intended purpose.</cite>
# 
# Links:
# https://data.noaa.gov/onestop/
# 
# https://www.ncdc.noaa.gov/cdo-web/search

# ## Filtering

# Both Pandas and D3.js have a type of filtering that are very similar. I will discuss the Pandas version

# #### Filter by year

# In[4]:


data[data.YEAR==2020].head()


# In[5]:


data[(data.YEAR==2020) & (data.MONTH==11)].head()


# #### Filter by WT_HAIL or WT_HighWinds

# In[6]:


data[(data.WT_HAIL==1) | (data.WT_HIGHWINDS==1)].head()


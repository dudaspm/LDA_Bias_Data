#!/usr/bin/env python
# coding: utf-8

# # Working with R in JupyterLabs

# In[1]:


get_ipython().run_cell_magic('capture', '', '!pip install rpy2')


# In[2]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# In[3]:


get_ipython().run_cell_magic('R', '', 'library(installr)\ninstall.packages.zip("https://cran.r-project.org/bin/windows/contrib/4.2/ggplot2_3.3.3.zip")')


# In[15]:


get_ipython().run_cell_magic('R', '', 'library("ggplot2")\ndata(mpg, package="ggplot2") # alternate source: "http://goo.gl/uEeRGu")\ntheme_set(theme_bw())  # pre-set the bw theme.\n\ng <- ggplot(mpg, aes(cty, hwy))\n\n# Scatterplot\ng + geom_point() + \n  geom_smooth(method="lm", se=F) +\n  labs(subtitle="mpg: city vs highway mileage", \n       y="hwy", \n       x="cty", \n       title="Scatterplot with overlapping points", \n       caption="Source: a subset of the fuel economy data that the EPA makes available on http://fueleconomy.gov")')


# In[ ]:





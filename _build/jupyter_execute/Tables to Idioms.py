#!/usr/bin/env python
# coding: utf-8

# # Tables to Idioms
# 
# ### Acknowledgement 
# 
# Slides created by and for:
# <cite>Munzner, T. (2014). Visualization analysis and design. CRC press.</cite> {cite}`munzner2014visualization`
# 
# Used by permission of the author. 
# 
# Image from:
# <cite>Wickham, H. (2010). A layered grammar of graphics. Journal of Computational and Graphical Statistics, 19(1), 3-28.</cite> {cite}`wickham2010layered`
# 
# ```{bibliography}
# ```
# 
# 

# ### First the Data

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd

url="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv"
data = []
data=pd.read_csv(url)
data = data.dropna() # removed NAs with 0s

### Remove the United States entries

data = data[data.location != "United States"]

data.total_vaccinations = data.total_vaccinations/100000
data.total_distributed = data.total_distributed/100000
data.people_vaccinated = data.people_vaccinated/100000


# In[2]:


data.head()


# ### Acknowledgement 
# 
# <cite>Max Roser, Hannah Ritchie, Esteban Ortiz-Ospina and Joe Hasell (2020) - "Coronavirus Pandemic (COVID-19)". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/coronavirus' [Online Resource]</cite>
#     
# Original Link: https://github.com/owid/covid-19-data (Accessed 3/11/2021)
# Source Link: https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations 
# 
# 
# <cite>Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. IEEE Annals of the History of Computing, 9(03), 90-95.</cite>

# ### Today's and Yesterday's date and data

# In[3]:


from datetime import datetime, timedelta

todaysDate = datetime.today()
yesterdaysDate = todaysDate  - timedelta(days=1)
yesterdaysDate = yesterdaysDate.strftime('%Y-%m-%d')
twoDays = todaysDate - timedelta(days=2)
twoDays = twoDays.strftime('%Y-%m-%d')

data[data.date==yesterdaysDate].head()


# ![Scatterplot Description](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/scatterplot.PNG)

# <cite>Scatter Plot — Matplotlib 3.3.4 Documentation. https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html. Accessed 14 Mar. 2021.</cite>

# In[4]:


px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(600*px, 400*px))

ax.scatter(data.total_distributed, data.total_vaccinations)

# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Total Distributed (x100000)' )
ax.set_ylabel( 'Total Vaccinations (x100000)' )
plt.title( 'Distributed vs. Vaccinated per State' )
ax.grid()

# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


# ![Bar Chart Idiom](barchart.PNG)

# <cite>Grouped Bar Chart with Labels — Matplotlib 3.3.4 Documentation. https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html. Accessed 14 Mar. 2021.
# </cite>

# In[5]:


# creating the bar plot
yData = data[data.date==yesterdaysDate]
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(1000*px, 300*px))
ax.bar(yData.location, yData.total_vaccinations, color ='maroon', width = 0.4)

# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Locations' )
ax.set_ylabel( 'Total Vaccinations (x100000)' )
plt.title( 'Vaccinations Yesterday per Location' )
# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


# In[6]:


# creating the bar plot
top10 = ["California","Texas","Florida","New York State","Illinois","Pennsylvania","Ohio","Georgia","North Carolina","Michigan"]
yData = data[data.date==yesterdaysDate]

top10Yest = yData[yData.location.isin(top10)]
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(1000*px, 300*px))
ax.bar(top10Yest.location, top10Yest.total_vaccinations, color ='maroon', width = 0.4)

# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Locations' )
ax.set_ylabel( 'Total Vaccinations (x100000)' )
plt.title( 'Vaccinations Yesterday per Location' )
# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


# In[7]:


# creating the bar plot
top10 = ["California","Texas","Florida","New York State","Illinois","Pennsylvania","Ohio","Georgia","North Carolina","Michigan"]
yData = data[data.date==yesterdaysDate]

sortedData = yData.sort_values(by=['total_vaccinations'])
top10Yest = sortedData[sortedData.location.isin(top10)]
px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(1000*px, 300*px))
ax.bar(top10Yest.location, top10Yest.total_vaccinations, color ='maroon', width = 0.4)

# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Locations' )
ax.set_ylabel( 'Total Vaccinations (x100000)' )
plt.title( 'Vaccinations Yesterday per Location' )
# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


# ### Paired Bar Chart

# In[8]:


import numpy as np
# creating the bar plot
top10 = ["California","Texas","Florida","New York State","Illinois","Pennsylvania","Ohio","Georgia","North Carolina","Michigan"]
yData = data[data.date==yesterdaysDate]
sortedData = yData.sort_values(by=['total_vaccinations'])
top10Yest = sortedData[sortedData.location.isin(top10)]

twoData = data[data.date==twoDays]
sortedData = twoData.sort_values(by=['total_vaccinations'])
top102days = sortedData[sortedData.location.isin(top10)]

x = np.arange(len(sortedData[sortedData.location.isin(top10)].location))  # the label locations
width = 0.35  # the width of the bars

px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(1000*px, 300*px))
ax.bar(x - width/2, top102days.total_vaccinations, color ='steelblue', width = 0.4, label="Yesterday")
ax.bar(x + width/2, top10Yest.total_vaccinations, color ='maroon', width = 0.4, label="Two Days")
# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Locations' )
ax.set_ylabel( 'Total Vaccinations (x100000)' )
ax.set_xticks(x)
ax.set_xticklabels(sortedData[sortedData.location.isin(top10)].location)

ax.legend()

plt.title( 'Vaccinations Yesterday per Location' )
# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


# In[9]:


import numpy as np
# creating the bar plot
top10 = ["California","Texas","Florida","New York State","Illinois","Pennsylvania","Ohio","Georgia","North Carolina","Michigan"]
yData = data[data.date==yesterdaysDate]
sortedData = yData.sort_values(by=['total_vaccinations'])
top10Yest = sortedData[sortedData.location.isin(top10)]

twoData = data[data.date==twoDays]
sortedData = twoData.sort_values(by=['total_vaccinations'])
top102days = sortedData[sortedData.location.isin(top10)]

x = np.arange(len(sortedData[sortedData.location.isin(top10)].location))  # the label locations
width = 0.35  # the width of the bars

px = 1/plt.rcParams['figure.dpi']  # pixel in inches
fig, ax = plt.subplots(1,figsize=(1000*px, 300*px))
rects1 = ax.bar(x - width/2, top102days.total_vaccinations, color ='steelblue', width = 0.4, label="Two Days")
rects2 = ax.bar(x + width/2, top10Yest.total_vaccinations, color ='maroon', width = 0.4, label="Yesterday")
# Add labels, a title and grid lines to the plot
ax.set_xlabel( 'Locations' )
ax.set_ylabel( 'Total Vaccinations' )
ax.set_xticks(x)
ax.set_xticklabels(sortedData[sortedData.location.isin(top10)].location)

ax.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.1f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)


plt.title( 'Vaccinations Yesterday per Location' )
# Show the figure (here in Jupyter)
plt.show( fig )
plt.close( fig )


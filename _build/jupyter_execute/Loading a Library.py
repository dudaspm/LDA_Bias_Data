#!/usr/bin/env python
# coding: utf-8

# # Loading a Library

# Module or Library?

# Modules are python's way of organizing functions, variables and constructors, similar to libraries in other languages.  In this section, we will look at:
# * Using existing python modules
# * Building our own modules
# * Finding the things that are within modules

# ## Built in Modules

# Python uses modules to make additional functionality available.  Modules can be thought of as libraries with many functions, data types, and characteristics that can be used once loaded. 

# We load modules using the import statement:
# * Highly recommend import using a name (import module as name)
# * Use the name to keep multiply defined functions separate
# * You can import only individual functions from a module
# * You can also rename functions.

# In[1]:


# Import all functions using a name
import numpy as np
# We then use the name to refer to functions from this module
print( np.sin( 1./2. * np.pi ) )

# We can also import just some of the functions, as well as change their names
from math import cos as mathCos
print( mathCos( np.pi ) )


# Some common python modules are:
# * numpy
# * matplotlib
# * math
# * scipy
# * pandas
# 
# Modules based on their topic can be found: https://wiki.python.org/moin/UsefulModules

# Some modules are already included on the system.  You may have to add or update some yourself. Python uses pip for module addition, which includes dependencies. Typically users will put modules in their own space using --user, rather than install them globally. For example, to add cython and to update matplolib you would run in a cell:
# ```javascript
# !pip install cython --user
# 
# !pip install matplotlib --user --upgrade
# ```

# ## Homade Modules

# You can also build your own modules. To do this, place what you want in a python file (<fileName>.py) in your working directory.  Note that you need an empty file named __init__.py in this directory as well. You can then load your module just like the built-in modules.  For example, if a file called adamsTrigs.py contained:
# ```python
# import math as mt
# def printTrigVals(angle):
#     print( angle,mt.sin(angle),mt.cos(angle),mt.tan(angle) )
# ```
# then I can load the module and use this function locally by either importing everything in the file, or just the function we are interested in.

# In[2]:


import adamsTrigs as aT
aT.printTrigVals( np.pi / 3. )

from adamsTrigs import printTrigVals as trigVals
trigVals( np.pi / 5)


# ## Helpful hints for modules

# ### Dir

# Python has a built-in command called dir to show the directory (contents) of a module. This command provides lots of info, including the function names.

# In[3]:


import adamsTrigs as aT
dir( aT )


# We can also use dir to see what is currently available to use:

# In[4]:


dir()


# ### Main

# We can also define code that will only run if the file is being run directly.  This will not run if the file is being loaded by another. 

# In[5]:


if __name__ == "__main__":
    # Make a figure of the local data
    # Print out some local variables to provide examples for later use
    print( "This is being run from here" )


# This is often used in files to read in data, where individual data sets are read into discrete files, which are then read into the main function as modules.  You can make figures showing individual data sets to test if you are reading correctly in the read file.  Rather than make these each time you include that data read file as a module, you can put the plotting in an if statement like this.

# # Check yourself

# Call the math version of tan() mathTan and print out tangent of pi/2.  (Hint, pi can come from math or numpy).

# In[6]:


# Try it here


# Does numpy include functions called log10 and banana?

# In[7]:


# Try it here


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python - 🐧

# In this section, I wanted to introduce a few basic concepts and give an outline of this section. 

# ## Comments in Python

# In Python, we can create comments in the code itself. Considering we can use markdown language (as you see here 😁), we won't use this too much in this notebook. Though, here is an example. 
# 
# Basically, you use the... umm... hashtag? Number sign? Pound sign? 
# 
# This thing -> #

# In[4]:


# I am a comment in Python
# Here is 2 + 2
2 + 2
# As you can see, these are not "computed" using Python. 
# We are just comments for the person looking at this.
# Or... you!


# ## Print Function

# We will being using...
# 
# ```python
# print()
# ```
# 
# ...several times in this notebook. 
# 
# *print()* is a function to print out strings, variables, numbers, functions, etc. 
# 
# Let's use the classic example.

# In[7]:


print( "hello, world!" )


# OR

# In[8]:


print("hello, world!")


# *print()* can do some fun things as well. As in, giving it more than one thing to print with commas between them. This will print both things with spaces.

# In[6]:


print( "hello,", "world!" )


# ## Help Function

# The...
# 
# ```python
# help()
# ```
# 
# ... function is exactly what it is. It is a function to 🌟 help 🌟 you understand the basic usage of another function. 

# In[9]:


help(print)


# ## Resources

# Highly suggest looking for answers using [StackOverflow](https://stackoverflow.com/help/searching)

# ## Common Errors

# One of the most common errors in Python is the dreaded 
# 
# ```python
# 2 + 2
#  3 + 3
# 
#   File "<ipython-input-1-0dcc020fd5cb>", line 2
#     3 + 3
#     ^
# IndentationError: unexpected indent
# ```
# 
# Why does this occur? Well, because Python uses spacing or tabs to distinguish where things like loops, functions, and if/else statements start and end. So, if you add an extra space or tab at the beginning of the statement, you will see this message. If you do, check your spacing. 

# ```{note}
# Python can get weird with this issue. As you can, technically, start code wherever as long as you are consistent. The next cell shows an example of this... oddity.
# 
# ```

# In[5]:


2+2
3+3


# still works! 

#!/usr/bin/env python
# coding: utf-8

# # If-Else Conditions

# We can condition our data using if-else statements and switch cases.  If-else statements allow us to do different things if a certain criterion is met or not. We can count the odds and evens in our someNumbers list.

# ## if

# The *if* statement starts with if and then lists a condition that may or may not is met. If the condition is true, we do what is listed. If it is not, we move on. 
# 
# Our example here is straightforward; if answer is greater than 30, print something.

# In[1]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")


# OK, same concept. 

# In[2]:


answer = 42

if answer > 50:
    print( "This number is greater than 50")


# ```{note}
# Note the structure of a Python if/else statement where some languages use { } to denote the start and end of the if/else statement. Python uses spaces. 
# 
# if (condition): <-colon
# 
#  <- space or tab
#  
# Anything that is also spaced or tab is *part* of the if statement. 
# 
# ```

# ### Where the if Starts and Ends

# As mentioned in our note, the if/else statement uses spacing to indicate where it starts and ends. To highlight this, let's look at an example. 

# In[3]:


print("Into the If/Else!")

if (10 < 2):
    print("In the If/Else!")
    
    print("Still in the If/Else!")
    
    
    
    
    print("How do I get out of here!?")

print("Out of the If/Else!")


# ## else

# In these examples, only the numbers that are greater than 30 and 50 will get any response.  We can add a response for values that do not meet the conditional statement found within the if using an *else* statement. 

# In[4]:


answer = 42

if answer > 30:
    print( answer, "> 30")
else:
    print( answer, "< 30")
    
if answer > 50:
    print( answer, "> 50")
else:
    print( answer, "< 50")


# ## elif (else if)

# If-else statements can also be stacked together to allow for additional sorting using multiple conditions.  The way this is done in python is by using 
# ```python
# elif
# ```
# 
# This will chain conditions, but once one condition is true. It will stop ✋
# 
# Let's take a look at an example.

# In[5]:


favoriteColor = "Yellow"

if (favoriteColor == "Red"):
    print ("My favorite color is red.")
elif (favoriteColor == "Orange"):
    print ("My favorite color is orange.")
elif (favoriteColor == "Yellow"):
    print ("My favorite color is yellow.")
elif (favoriteColor == "Green"):
    print ("My favorite color is green.")
elif (favoriteColor == "Blue"):
    print ("My favorite color is blue.")
elif (favoriteColor == "Indigo"):
    print ("My favorite color is indigo.")
elif (favoriteColor == "Violet"):
    print ("My favorite color is violet.")
else:
    print ("I don't have a favorite color.")


# ### Switch Cases

# Switch Cases are specialized if-else statements - the criteria must be met precisely. Let's work on an example that changes between month numbers and month names. We first set up a dictionary that will be used for the evaluation.  We will use numbers as the keys and use the abbreviations as the values. 

# In[6]:


monthSwap = {1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}


# In[7]:


print( "monthSwap = ", monthSwap)

# Print out the 5th month
print( "\n#-# Key = 5")
print( monthSwap.get(5,"oooooops!") )

# Print out the 19th month
print( "\n#-# Key = 19")
print( monthSwap.get(19,"oooooops!") )


# In[ ]:





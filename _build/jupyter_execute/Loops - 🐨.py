#!/usr/bin/env python
# coding: utf-8

# # Loops - 🐨

# One of the programming features is that we have many options to do the same tasking multiple times.  The three methods we will be looking at are:
# * Functions (later notebook)
# * For loops
# * While Loops
# 

# ## For Loops

# Loops allow us to do the same thing to each item in a list or array. One of the most basic types of loops is a *for loop* - this allows us to iterate over any sequence.
# 
# We set up a for loop using 2 things:
# * loop variable - the value of the sequence currently being used
# * sequence - the data we iterate over
# 
# The sequence can be any list.  We set up *for loop* using the *for* and *in* keywords, a colon, and all of the code within the *for loop* indented.

# In[1]:


exampleList = ['a', 'niner', 6, 6.1, 'V@@@', 1001/2, 42]

print( exampleList )


# Now, before we talked about accessing elements in a list or array by their index. Meaning, if we wanted to print this out, we would need to...

# In[2]:


print( exampleList[0] )
print( exampleList[1] )
print( exampleList[2] )
print( exampleList[3] )
print( exampleList[4] )
print( exampleList[5] )
print( exampleList[6] )


# In[3]:


### Looping Over Values


# Very time consuming and frustrating 😤. 
# 
# Loops make this sooooooo much easier. There are three parts to a *for loop*. 
# 
# ```python
# 
# for variable_name_we_make_up in our_list_name:
#     do_something_with_each_value( variable_name_we_make_up )
#     
# ```
# 
# As stated, variable_name_we_make_up is something we makeup and is used to represent the value as we loop through our, well,... loop. 
# 
# ```python
# groceryList = ["apple", "banana", "eggs"]
# ``` 
# 
# Remember me? 

# In[4]:


groceryList = ["apple", "banana", "eggs"]

for itemInOurList in groceryList:
    print (itemInOurList)


# Like mentioned, we name the variable. Here is the same idea again.

# In[5]:


groceryList = ["apple", "banana", "eggs"]

for steve in groceryList:
    print (steve)


# Going back to our original list. See how much easier it is to print these values? 

# In[6]:


for item in exampleList:
    print (item)


# ### Looping Over Indices

# Sometimes, it's helpful to iterate using indices.  For example, linear algebra heavy calculations will almost always use indices to make working with vectors and matrices easier.
# 
# We can use the 
# ```python 
# len()
# ```
# and
# ```python 
# range()
# ```
# 
# functions to show the length and create indices.  We can then iterate using the index rather than the values. Let's show off these functions. 

# In[7]:


groceryList = ["apple", "banana", "eggs"]
print ( len(groceryList) )


# In[8]:


print ( range(3) )


# ```{note}
# *range()* can be a bit misleading. The range is always one less than what you might expect. Meaning, *range(0,3)* goes from 0 to 1 to 2 to... that's it. So when using *range()* think about it as *range(starting number, ending number - 1)*
# ```

# In[9]:


for index in range(len(groceryList)):
    print("index:",index,"value:",groceryList[index])


# You may have noticed that the second line is indented.  Like we saw before with If/Else statements. This indent is how we indicate what is in the loop.  Our loop can have many lines (all indented).  The first line that isn't indented indicates we are out of the loop.  This indent is the python syntax for in and out of the loop; other coding languages use other things such as braces {}.  Note that blank lines don't matter, just indentation.

# In[10]:


print( "Starting the loop" )
for val in groceryList:
    print( "\t", "item:", val )
    
    print( "\t", "Inside the loop" )
print( "Outside the loop" )


# ## While loops

# For loops are used when you have something you are iterating over - you know the length.  You can use a while loop if you don't know the number of times something will run. The while loop code requires a conditional statement; the loop will continue to run as long as this is true and will not run again as soon as it is false.

# #### Conceptual Example
# You can think about taking a test in two different ways. 
# 
# > Scenario: You are looking through your junk drawer for your sunglasses  
# 
# For loop:
# ```python
# for item in junk_drawer:
#     if (item == "sunglasses"):
#         "put them on" 😎
#     else:
#         "keep looking"
# ```
# 
# While loop:
# ```python 
# while item != "sunglasses":
#     "keep looking"
#     item = "some item in the junk drawer"
# "put them on" 😎
# ``` 
# 
# Can you see where each has their unique take on looping? Of course, you don't; you are wearing sunglasses indoors. Take them off first, then check out their uniqueness.

# The condition being set by the while statement will cause this to run as long as the statement is true.

# In[11]:


counting = 0

while (counting < 10):
    print ( "before:", counting )
    counting = counting + 1
    print ("\t","after:",counting)


# One thing to note is that the while loop won't ever be entered if the condition is false when the statement begins as false.

# In[12]:


startAtTen = 10

while (startAtTen < 10):
    print ( "before:", startAtTen )
    counting = counting + 1
    print ("\t","after:",startAtTen )


# ##### 😈 A VERY MEAN Example 😈

# Let's see where we can use this type of loop, in this 😈 VERY MEAN Example 😈. We are creating a set of 30 random numbers from 1 to 50. The *while* will run until it hits its first even number and print this out. Can you spot its MEAN intention?

# In[13]:


import random
randomList = [random.randrange(1, 50, 1) for i in range(30)]
print ( randomList[0:5] )

index = 0
print ("start loop")
while ( randomList[index] % 2 ):
    index = index + 1
print ( "the first even number is:", randomList[index])


# So why is this very mean?! Look at our warning.

# ```{warning}
# While loops will keep iterating as long as the statement stays true.  Infinite loops are caused by a condition that always stays true.  Use the stop button ( 🔲 but filled in ) to stop this erroneous code. Here is an example of this type of code. 
# ```

# ```python
# counting = 0
# 
# while (counting < 0):
#     print ( "This the loop that never ends. Yes, it goes on and on, my friend!" ) 
#     print ( "Some people started looping it not knowing what it was, " )
#     print ( "and they'll continue looping it forever just because..." ) 
#     counting = counting + 1
# ```

# This is 😈 A VERY MEAN Example 😈 because it is possible to have a set without a single even number. The odds of picking an even or an odd is a coin flip (50%). Now do this 30 times. What are the odds of flipping a coin 30 times without a single "Tails?" 
# 
# $\frac{1}{2}$ = 1 coin
# 
# $\frac{1}{2} * \frac{1}{2}$ = 2 coins
# 
# $\frac{1}{2} * \frac{1}{2} * \frac{1}{2}$ = 3 coins
# 
# $(\frac{1}{2})^n$ = n coin
# 
# $(\frac{1}{2})^{30}$ = 30 coin = $(\frac{1}{1073741824})$  OR one in 1 billion, 73 million, 741 thousand, 824. 
# 
# Meaning, a person out of 1073741824 will have an infinite loop! 
# 
# MUAHAHAHA!!!

# ## Your Turn

# Try to fill in code to fulfill the request!  Here is a variable used in the excercises

# In[14]:


aListOfNumbers = [6, 3, 4, 5, 7, 8, 9 ]


# Write a function that returns the length of aListOfNumbers as well as the maximum value. Hint: max() is a built-in function

# In[15]:


# Try it here:


# Use a for loop to add up all of the numbers in aListOfNumbers.

# In[16]:


# Try it here:


# Use a while loop to find the first number in aListOfNumbers that is both greater than 5 and a multiple of 4.

# In[17]:


# Try it here:


# Count the number of values in aListOfNumbers that are:
# * even
# * odd and divisible by three
# * odd and not divisible by three
# 
# using if, elif and else.

# In[18]:


# Try it here:


# Create a dictionary with keys 1-8 corresponding to the words one, two, three, etc. Loop through aListofNumbers to print out the word corresponding to the digit and provide a default value of 'Not Found' if the key is not contained within the dictionary.  You should get: six three four five seven eight Not Found

# In[19]:


# Try it here:


# In[ ]:





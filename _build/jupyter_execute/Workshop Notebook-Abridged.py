#!/usr/bin/env python
# coding: utf-8

# # Workshop Notebook Abridged

# ## Notebook Introduction - 🐸 - frog

# In[1]:


2 + 2


# ### Export to Binder or Google Colab 

# As you can see you can also export these notebooks to Binder or Google Colab. 
# 
# <img alt="Binder or Google Colab options" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/topscreen3.png" style="width:240px;margin-left:auto;margin-right:auto;display:block;">
# 
# This will take you to their respective websites but you can work with them there, if you would like!

# ### References

# I know it tradition to have the refences at the end of books, but when you are standing on the shoulders of giants. You thank them first. 

# ```{bibliography}
# ```

# ### Thank you!
# 
# Also, a huge *thank you* to Adam Lavely (https://github.com/adamlavely) for developing some of the intial notebooks! 

# ***

# ## Introduction to JupyterLab - 🐘 - elephant

# ### Where am I? (JupyterLab Notebook)

# Jupyter is a powerful suite of tools that allows us to do many things.
# 
# Jupyter is capable of running **Ju**lia, **Pyt**hon and **R**, as well as some other things. 
# 

# ### Cells

# Each box is called a cell. 

# #### Two types of Cells

# ##### Text 

# Text Cells allow you to add text (via Markdown), which includes tables, images, links, bullet lists, numbered lists, LaTeX, blockquote, among other things. 

# ##### Code

# Cells can be run using the Run button &#9658; or selecting one of the run options under the Run menu. 
# 
# Try this out! You can change what is in the cell and rerun the same cell, which is useful for debugging.

# In[2]:


2 + 2 


# ### Your turn!

# In a new cell, figure out what **5315 + 5618** is. 

# In[3]:


## remove and type out 5315 + 5618
## then hit the play button


# ### Jupyter ✨ MAGIC ✨

# When using other languages in Jupyter/JupyterLab, we need to designate the cell we are using with this langauge or function. To "activate" these language, we need to use ✨ MAGIC ✨. Here are a couple of examples.

# #### HTML

# In[4]:


get_ipython().run_cell_magic('html', '', '<ol>\n  <li>apple</li>\n  <li>banana</li>\n  <li>cookies</li>\n</ol>')


# #### SVG

# In[5]:


get_ipython().run_cell_magic('svg', '', '<svg height="100" width="100">\n  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="steelblue" />\n</svg>')


# #### R Language

# In Google Colab, you do *not* need to install anything, but if you are going to do this on your local machine (your computer). 
# 
# ![Anaconda Prompt - installing r-essentials](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/command.PNG)
# 
# You will need to install a few things first. To do this, open up the *Anaconda Prompt (anaconda3)* and run the following two commands:
# 
# ```jupyter
# conda install -c r r-essentials
# ```
# and
# ```jupyter
# conda install -c r rpy2
# ```
# 
# then continue from here.

# In[6]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# In[7]:


get_ipython().run_cell_magic('R', '', 'data <- c(1,2,3)\nprint(data)')


# #### SQL

# In[8]:


get_ipython().run_cell_magic('capture', '', '!pip install ipython-sql')


# In[9]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[10]:


get_ipython().run_line_magic('sql', 'sqlite:///exampleDatabase.db')


# More information can be found here: [Jupyter ✨ MAGIC ✨](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

# ***

# ## Introduction to Python - 🐧 - penguin

# In this section, I wanted to introduce a few basic concepts and give an outline of this section. 

# ### Comments in Python

# In[11]:


# I am a comment in Python
# Here is 2 + 2
2 + 2
# As you can see, these are not "computed" using Python. 
# We are just comments for the person looking at this.
# Or... you!


# ### Print Function

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

# In[12]:


print( "hello, world!" )


# *print()* can do some fun things as well. As in, giving it more than one thing to print with commas between them. This will print both things with spaces.

# In[13]:


print( "hello,", "world!" )


# ### Help Function

# The...
# 
# ```python
# help()
# ```
# 
# ... function is exactly what it is. It is a function to 🌟 help 🌟 you understand the basic usage of another function. 

# In[14]:


help(print)


# ### Resources

# Highly suggest looking for answers using [StackOverflow](https://stackoverflow.com/help/searching)

# ### Common Errors

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

# ### Your turn!
# 
# Print out the help information for a function called type().

# In[15]:


# Add a comment here 

# Remove this and print the help for type()


# ***

# ## Learning about Variables - 🐳 - whale

# In[16]:


5 + 3 + 16


# But let's look at an example where we need to get the circumference of a circle using multiple radii. The equation for the circumference of a circle is: 
# 
# $C = 2 \pi r$

# Let's say the radius is 5

# In[17]:


2 * 3.14159265359 * 5


# In[18]:


pi = 3.14159265359


# Now, every time we reference the variable called **pi** it will refer to the number **3.14159265359**
# 
# Let's try those radii again (10, 11, 4)

# In[19]:


2 * pi * 10


# In[20]:


2 * pi * 11


# In[21]:


2 * pi * 4


# ### Type of Variables

# #### Integers or int

# As mentioned, integers are whole numbers. Let's create an example. How about we use our numberOfKittens. We will then set this value to 0. As in, we have 0 kittens.

# In[22]:


numberOfKittens = 0


# One thing we might want to do is to have Python tell us what **type** this variable is. Well, Python has a function for this called
# 
# ```python
# type()
# ```

# In[23]:


type( numberOfKittens )


# So this checks out, we made an int, and it is showing us we have an int.
# 
# Now, once we have a variable, it is not static. We can change the value as much as we need to. Running the next cell will continually add 10 to our original variable. 
# 
# Try running this a few times.

# In[24]:


numberOfKittens = numberOfKittens + 10
print( numberOfKittens )


# #### Floating points or floats

# Floats are similar to integers, but with more precision.
# Float comes from a Floating point or a number with a decimal point. 
# 
# This example starts at 0, but note that this is .0 
# Adding the decimal tells Python that we should have a float value instead of an integer. 

# In[25]:


aFloatVariable = .0


# Let's again, check the variable type. 

# In[26]:


type( aFloatVariable )


# Looks good. 
# 
# And again, we will add 10 to this. There is something specific interesting here; see if you spot it.

# In[27]:


aFloatVariable = aFloatVariable + 10

print( aFloatVariable )


# If you guessed "mixing a float and an integer," you got it. Let's see an example. 

# ##### type-cast

# type-cast is temporary. If you do not use a type-cast, the variable will revert to its original variable type. 

# Let's switch our numberOfKittens to a float using 
# ```python
# float()
# ```
# 
# and turn our aFloatVariable to an integer using
# 
# ```python
# int()
# ```

# In[28]:


float(numberOfKittens)


# In[29]:


int(aFloatVariable)


# #### String or str

# In[30]:


helloStatement = "Hello, everyone!"


# As you can see, can capture text and other alphanumeric and special characters. There are several unique functions for strings but first, let's double-check and see what type we from our helloStatement.

# In[31]:


type( helloStatement )


# Not too surprising, we see this is type str or string. 

# ##### String Indexing/String Slicing

# In[32]:


helloStatement[1] 


# ohh.. wait a minute. We were expecting the letter *H*, but we got *e*. What happened?

# For indexes, we always start at the number 0. So, 0 is the first thing, 1 is the second thing, and so on.

# Let's try this again. 

# In[33]:


helloStatement[0]


# There we go! 

# Visually, this is how the string looks to Python. 
# 
# ![Hello, everyone! text](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/helloEveryone.png)

# ###### Indexing Multiple Letters

# In[34]:


print( helloStatement[0:5] )


# The way you should think of this is: 
# 
# ```python
# helloStatement[0 : 5 - 1]
# helloStatement[(starting number) to (ending number - 1)]
# ```
# 
# There is also a shortcut way of writing this, without the 0. 

# In[35]:


print( helloStatement[:5] )


# In[36]:


print( helloStatement[5:] )


# ##### String functions

# ###### Formatting

# In[37]:


print( helloStatement.capitalize() )
print( helloStatement.lower() )


# ###### Split

# In[38]:


print( helloStatement.split(" ") )


# *.split()* will eventually become your best friend. *.split()* is a **great** function to use when using uniquelly spaced data. 
# As in comma separated values or CSV. 

# ##### Concatenating Strings
# 
# When you want to put two strings together, we say you *concatenate* the strings. There are multiple ways of doing this but presented are what I believe to be the three most common ways. 

# ###### + Method

# This is the most straightforward method of the three, but there can be some issues. You simply add a plus sign *+* between your strings. Let's take a look at this. 

# In[39]:


print ( "hello, " + "everyone!")


# This works fine, but when you add a number to this idea. We run into issues. 

# In this case we need to *type-cast* the integer as a string using
# ```python
# str()
# ```

# In[40]:


print ( "hello, " + "every" + str(1) + "!")


# ###### % Method

# This is my favorite method out of the three. Let's see how this works with the same example. 
# 
# In this case, we use a %s (s = string) for each string we want to embed in our overall string. 

# In[41]:


print ( "%s, %s" % ("hello", "everyone") )


# There are three parts to this. 
# 
# *The format*
# ```python
# "%s, %s"
# ```
# 
# *The break*
# ```python
# %
# ```
# 
# *The fill*
# ```python
# ("hello", "everyone")
# ```
# 
# We have two %s, meaning we need to feed it with two strings. 

# OK, but what about numbers?

# In[42]:


print ( "%s, %s%s%s" % ("hello","every",1,"!") )


# Still works! This reason is why I like this method. You pick the formating and feed in the strings. 

# The same issue as before, we need to type-cast. 

# #### Booleans

# Booleans are used to do comparisions (true/false), (1/0), (yes/no)

# In[43]:


someCondition = True
type( someCondition )


# ##### Boolean Logic

# We will talk about boolean logic more in the next section (Comparisons)

# In[44]:


(someCondition == False)


# In[45]:


if (False): 
    print( "yes for False!" )
if (True): 
    print( "yes for True!" )


# A more "traditional" way to do booleans is to use 0 and 1. In Python, any number other than 0 is True. Including negative numbers and decimals. 

# In[46]:


if (0): 
    print( "yes for 0!" )
if (1): 
    print( "yes for 1!" )
if (2): 
    print( "yes for 2!" )
if (-3): 
    print( "yes for -3!" )
if (.4): 
    print( "yes for .4!" )


# ### Lists

# Lists (or also known as Arrays) are exactly that. A list of data. 
# 
# There are two options for creating a *List*. 
# 
# 1. Define the list initially

# In[47]:


groceryList = ["apple", "banana", "eggs"]
print( groceryList )


# 2. Create a list and add to it using
# 
# ```python 
# .append()
# ```

# In[48]:


groceryList = []
groceryList.append("apple")
groceryList.append("banana")
groceryList.append("eggs")
print( groceryList )


# ```{note}
# For indexes, we always start at the number 0. So, 0 is the first thing, 1 is the second thing, and so on.
# ```

# In[49]:


print( groceryList[2] )
print( groceryList[0] )
print( groceryList[1] )


# So what happens if we use an *index* outside of our list?

# ```python 
# print( groceryList[3] )
# 
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-44-0a77fb05d512> in <module>
#     print( groceryList[3] )
# 
# IndexError: list index out of range
# ```

# ```{note}
# Typically, going through an array, one index at a time is not how we want to use lists. 
# We will talk about going through lists using a *loop* in an upcoming notebook. 
# ```

# #### Dictionary

# Dictionaries are used to index based on a specific key. As in:
# 
# ```python
# dictionary["street adddress" (key)] = "123 Apple St." (value)
# ```

# In[50]:


personalInformation = {}
personalInformation["streetAddress"] = "123 Apple St."
personalInformation["firstName"] = "Patrick"
personalInformation["lastName"] = "Dudas"
print( personalInformation )


# Note the order.

# Again, to do this more efficiently, we will be using loops (we will talk about later).

# ### Your turn!
# 
# 1. Create a list
# 2. append() three items
#     1. an integer
#     2. a float
#     3. a string
# 3. print this list

# In[51]:


## list create
## append() integer
## append() float
## append() string
## print() list


# ***

# ## Comparison Operators - 🐭 - mouse

# We need to be able to compare different variables.  We will be working on:
# * Are these things the same?
# * Are these things not the same?
# * How do these things compare?
# 

# ### Are these things the same?

# #### Numeric Comparisons
# We have already initiated variables by setting something equal to something else - let's do that here by setting kitten 🐈 equal to 10 and then setting dog 🐕 equal to kitten 🐈. Finally, 🐝 bee will be equal to 11. 
# 
# So...
# 
# 🐈 = 10
# 
# 🐕 = 🐈
# 
# 🐝 = 11

# In[52]:


kitten = 10
dog = kitten
bee = 11 

print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )


# The first comparison operator is '==', which tests to see if two variables are equal. 

# In[53]:


print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )

print( "Is kitten equal to dog?")
print( kitten == dog )

print( "Is kitten equal to bee?")
print( kitten == bee )


# This tells us that kitten is equal to dog, because it returns *True* and kitten is not equal to bee, as that returns *False*.

# #### Character Comparisons
# We can also do comparisons with other variable types.  Here's an example with strings instead of integers.
# 
# Let's think about some foods, how about:
# 
# - food1 = 🍎
# - food2 = 🍪
# - food3 = 🍎

# In[54]:


food1 = 'apple'
food2 = 'cookie'
food3 = 'apple' 
print( "food1=", food1,"; food2 =", food2,"; food3 = ", food3 )

print( "Is food1 equal to food2?")
print( food1 == food2 )

print( "Is food1 equal to food3?")
print( food1 == food3 )

print( "Is apple equal to Apple?")
print( "apple" == "Apple" )


# ### Are these things different?

# #### This is Logical... NOT!
# We can also test to see if two values are not equal using the '!=' operator.

# In[55]:


print( "food1 =", food1,"; food2 =", food2,"; food3 =", food3 )

print( "Is food1 not equal to food2?")
print( food1 != food2 )

print( "Is food1 not equal to food3?")
print( food1 != food3 )


# This gives us the opposite of what we had before.  
# 
# So, what did we learn?
# 
# 🍎 == 🍎 = *True*
# 
# 🍎 != 🍪 = *True*

# ### How do these things compare?

# #### Math Comparisons 101
# We can also compare the magnitude of values using '<', '<=', '>'and '>=', which will return 'True' if the condition is being met.

# In[56]:


print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )


# In[57]:


print( "Is kitten less than dog?")
print( kitten < dog )

print( "Is kitten less than or equal to dog?")
print( kitten <= dog )

print( "Is kitten greater than or equal to dog?")
print( kitten >= dog )

print( "Is kitten greater than dog?")
print( kitten > dog )


# varible = varible is **not** the same thing as variable == variable
# 
# varible = varible will **always** return true

# ### Multiple Comparisons

# We can make multiple comparisons at once by stringing the statements
# * and
# * not
# * or
# 
# together. 
# 
# The individual testable (true/false) components need to be broken apart. For example,
# * If the *V* CATA bus is coming around the corner, then I need to run towards the bus stop.
# 
# requires several things for it to be true and to require running.  We can break these things out with:
# * If there is a vehicle coming around the corner **AND** that vehicle is a CATA bus **AND** that CATA bus is a V 
#     * then I need to run towards the bus stop
# 
# We will only run towards the bus stop if all of the statements are true.

# #### AND

# the **and** operator will return True if all of the conditions are met

# Let's create another scenario for this around clothes. For this, let's assume:
# 
# face = 😎 
# 
# shirt = 👕
# 
# pants = 👖 
# 
# 
# 
# 
# 

# In[58]:


face = "sunglasses"
shirt = "tshirt"
pants = "jeans"

print ( "Am I wearing sunglasses and jeans?" )
print (face == "sunglasses")
print (pants == "jeans") 
print( (face == "sunglasses") and (pants == "jeans") )

print ( "Am I wearing sweater and jeans?" )
print (shirt == "sweater")
print (pants == "jeans") 
print( (shirt == "sweater") and (pants == "jeans") )


# We can also string as many comparisons together as we want.

# In[59]:


print( (1 < 2) and (1 < 3) and (1 < 4) and (1 < 5) and (1 < 6) and (1 < 7) and (1 < 8) )


# #### OR

# the **or** operator will return True if at least *1* of the conditions is met

# In[60]:


print( "face =", face, "; shirt =", shirt, "; pants = ", pants )

print ( "Am I wearing sunglasses or jeans?" )
print (face == "sunglasses")
print (pants == "jeans") 
print( (face == "sunglasses") or (pants == "jeans") )

print ( "Am I wearing sweater or jeans?" )
print (shirt == "sweater")
print (pants == "jeans") 
print( (shirt == "sweater") or (pants == "jeans") )


# #### Not

# the **not** will reverse or switch the  meaning of the and/or operators

# In[61]:


print( "face =", face, "; shirt =", shirt, "; pants = ", pants )

print ( "Am I wearing sunglasses and not jeans?" )
print (face == "sunglasses")
print (not (pants == "jeans"))
print( (face == "sunglasses") and not (pants == "jeans") )

print ( "Am I wearing jeans and not a sweater?" )
print (not (shirt == "sweater"))
print (pants == "jeans") 
print( not (shirt == "sweater") and (pants == "jeans") )


# ### Your turn!

# Try to fill in code to fulfill the request!  Here are some variables used in the exercise

# In[62]:


dogA_color = 'brown'
dogA_mass = 42
dogA_sex = 'male'
dogA_age = 5
dogA_name = 'chip'

dogB_color = 'white'
dogB_mass = 19
dogB_sex = 'female'
dogB_age = 2
dogB_name = 'lady'


# Is dogA the same color as dogB? (False)

# In[63]:


# print out result


# ***

# ## If-Else Conditions - 🐴 - horse

# We can condition our data using if-else statements and switch cases.  If-else statements allow us to do different things if a certain criterion is met or not. We can count the odds and evens in our someNumbers list.

# ### if

# The *if* statement starts with if and then lists a condition that may or may not is met. If the condition is true, we do what is listed. If it is not, we move on. 

# In[64]:


answer = 42

if answer > 30:
    print( "This number is greater than 30")


# OK, same concept. 

# In[65]:


answer = 42

if answer > 50:
    print( "This number is greater than 50")


# Note the structure of a Python if/else statement where some languages use { } to denote the start and end of the if/else statement. Python uses spaces. 
# 
# if (condition): <-colon
# 
#  <- space or tab
#  
# Anything that is also spaced or tab is *part* of the if statement. 

# #### Where the if Starts and Ends

# In[66]:


print("Into the If/Else!")

if (10 < 2):
    print("In the If/Else!")
    
    print("Still in the If/Else!")
    
    
    
    
    print("How do I get out of here!?")

print("Out of the If/Else!")


# ### else

# In these examples, only the numbers that are greater than 30 and 50 will get any response.  We can add a response for values that do not meet the conditional statement found within the if using an *else* statement. 

# In[67]:


answer = 42

if answer > 30:
    print( answer, "> 30")
else:
    print( answer, "< 30")
    
if answer > 50:
    print( answer, "> 50")
else:
    print( answer, "< 50")


# ### elif (else if)

# If-else statements can also be stacked together to allow for additional sorting using multiple conditions.  The way this is done in python is by using 
# ```python
# elif
# ```
# 
# This will chain conditions, but once one condition is true. It will stop ✋
# 
# Let's take a look at an example.

# In[68]:


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


# ### Your turn!
# 
# Copy the above example ↑ and add your favorite color!

# In[69]:


## Copy code here


# ***

# ## Loops - 🐨 - koala

# One of the programming features is that we have many options to do the same tasking multiple times.  The three methods we will be looking at are:
# * Functions (later notebook)
# * For loops
# * While Loops
# 

# ### For Loops

# Loops allow us to do the same thing to each item in a list or array. One of the most basic types of loops is a *for loop* - this allows us to iterate over any sequence.
# 
# We set up a for loop using 2 things:
# * loop variable - the value of the sequence currently being used
# * sequence - the data we iterate over
# 
# The sequence can be any list.  We set up *for loop* using the *for* and *in* keywords, a colon, and all of the code within the *for loop* indented.

# In[70]:


exampleList = ['a', 'niner', 6, 6.1, 'V@@@', 1001/2, 42]

print( exampleList )


# Now, before we talked about accessing elements in a list or array by their index. Meaning, if we wanted to print this out, we would need to...

# In[71]:


print( exampleList[0] )
print( exampleList[1] )
print( exampleList[2] )
print( exampleList[3] )
print( exampleList[4] )
print( exampleList[5] )
print( exampleList[6] )


# #### Looping Over Values

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

# In[72]:


groceryList = ["apple", "banana", "eggs"]

for itemInOurList in groceryList:
    print (itemInOurList)


# Like mentioned, we name the variable. Here is the same idea again.

# In[73]:


groceryList = ["apple", "banana", "eggs"]

for steve in groceryList:
    print (steve)


# Going back to our original list. See how much easier it is to print these values? 

# In[74]:


for item in exampleList:
    print (item)


# #### Looping Over Indices

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

# In[75]:


groceryList = ["apple", "banana", "eggs"]
print ( len(groceryList) )


# In[76]:


print ( range(3) )


# *range()* can be a bit misleading. The range is always one less than what you might expect. Meaning, *range(0,3)* goes from 0 to 1 to 2 to... that's it. So when using *range()* think about it as 
# 
# ```python
# range(starting number, ending number - 1)
# ```

# In[77]:


for index in range(len(groceryList)):
    print("index:",index,"value:",groceryList[index])


# In[78]:


print( "Starting the loop" )
for val in groceryList:
    print( "\t", "item:", val )
    
    print( "\t", "Inside the loop" )
print( "Outside the loop" )


# ### While loops

# For loops are used when you have something you are iterating over - you know the length.  You can use a while loop if you don't know the number of times something will run. The while loop code requires a conditional statement; the loop will continue to run as long as this is true and will not run again as soon as it is false.

# ##### Conceptual Example
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

# In[79]:


counting = 0

while (counting < 10):
    print ( "before:", counting )
    counting = counting + 1
    print ("\t","after:",counting)


# One thing to note is that the while loop won't ever be entered if the condition is false when the statement begins as false.

# In[80]:


startAtTen = 10

while (startAtTen < 10):
    print ( "before:", startAtTen )
    counting = counting + 1
    print ("\t","after:",startAtTen )


# 
# While loops will keep iterating as long as the statement stays true.  Infinite loops are caused by a condition that always stays true.  Use the stop button ( 🔲 but filled in ) to stop this erroneous code. Here is an example of this type of code. 
# 

# ```python
# counting = 0
# 
# while (counting < 0):
#     print ( "This the loop that never ends. Yes, it goes on and on, my friend!" ) 
#     print ( "Some people started looping it not knowing what it was, " )
#     print ( "and they'll continue looping it forever just because..." ) 
#     counting = counting + 1
# ```

# ### Your turn!

# Try to fill in code to fulfill the request!  Here is a variable used in the excercises

# In[81]:


aListOfNumbers = [6, 3, 4, 5, 7, 8, 9 ]


# Use a for loop to add up all of the numbers in aListOfNumbers.

# In[82]:


# Try it here:


# ***

# ## Loading a Library - 🐠 - fish

# Modules are python's way of organizing functions, variables and constructors, similar to libraries in other languages.  In this section, we will look at:
# * Using existing python modules
# * Building our own modules
# * Finding the things that are within modules

# ### Built in Modules

# Python uses modules to make additional functionality available.  Modules can be thought of as libraries with many functions, data types, and characteristics that can be used once loaded. 

# In[83]:


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

# We can also use dir to see what is currently available to use:

# ### Your turn!

# Call the math version of tan() mathTan and print out tangent of pi/2.  (Hint, pi can come from math or numpy).

# In[84]:


# Try it here


# ***

# ## Creating a Function - 🐲 - dragon

# Functions allow us to do repeated tasks easily by writing the code only once.  Functions will have a name, inputs, and outputs and can be called anywhere the task is repeated.
# 
# There are functions that are built into python; for example, we have already been using the type() function, which tells us the type of variable we are using.  Note that print is also a function!

# In[85]:


aVal = 10.0
print( type( aVal ) )


# Functions have four typical parts:
# * Name - what you call your function
# * Input arguments - what you provide
# * Outputs - what the function gives back
# * Math/Magic - what the function does

# ### Creating Our Own Function

# In python, we use def to define a function with the function name and inputs followed by a colon.  The python function is then separated from the rest of the code by a tab. Some languages use braces rather than indentation.
# ````python
# def functionName( inputs ):
#     # Operate on the inputs
#     ouputs = inputs + 5
#     # Return what we want to back
#     return outputs;
#    ````

# Let's look at an example function, which changes degrees Fahrenheit to Celsius. 

# In[86]:


def changeFromFToC( farVal ):
    cVal = (farVal - 32.0) * 5.0 / 9.0
    return cVal 


# Here, our function name is *changeFromFToC*, the input is *farVal*, the temperature in Fahrenheit, the output is *cVal*, and the temperature in Celsius. We can print or store the output from the function.  Note that the function has to be defined before we use it - the cell with the function definition has to have run before we can call the function.

# In[87]:


print( "Change 14 deg F to Celsius" )
print( changeFromFToC( 14 ) )

print( "Change from 68 deg F to Celsius" )
niceTempC = changeFromFToC( 68 )
print( niceTempC )


# #### Function Gotcha! 😆 

# ```{note}
# The biggest gotcha on functions is with variable scope: 
# * Variables defined in a function are not accessible from the outside
# * Functions have access to more than just the variables passed in
# ```

# In[88]:


def addAnAnimal( animal ):
    print ("\t","in the function")
    print ("\t","I have access to dog:",dog)
    print ("\t","I have access to animal:",animal)
    newValue = animal + 1
    print ("\t","I have access to newValue:",newValue)
    return newValue
  
print ("outside the function")
dog = 10
print("dog:", dog)
print ("function output:",addAnAnimal( dog ))


# If we would add:
# 
# ```python
# print (newValue)
# ```
# 
# to the bottom, we would end up with this:

# ```python
# def addAnAnimal( animal ):
#     print ("\t","in the function")
#     print ("\t","I have access to dog:",dog)
#     print ("\t","I have access to animal:",animal)
#     newValue = animal + 1
#     print ("\t","I have access to newValue:",newValue)
#     return newValue
#   
# print ("outside the function")
# dog = 10
# print("dog:", dog)
# print ("function output:",addAnAnimal( dog ))
# print (newValue)
# ```
# 
# outside the function
# 
# dog: 10
# 
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in the function
#      
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have access to dog: 10
#      
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have access to animal: 10
#      
# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I have access to newValue: 11
#      
# function output: 11
# 
# ```python
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-32-07cce689eb00> in <module>
#      11 print("dog:", dog)
#      12 print ("function output:",addAnAnimal( dog ))
# ---> 13 print (newValue)
# 
# NameError: name 'newValue' is not defined
# ```
#     

# ### Your turn! 
# 
# What is the temperature today? Convert it to Celsius. 
# 
# For those who have the temperature in Celsius and want to convert it to Fahrenheit. Define a new function to do this.

# In[89]:


# Try it here


# ***

# ## The End

# Thank you again for attending the ICDS Python/JupyterLab Workshop! 

# In[ ]:





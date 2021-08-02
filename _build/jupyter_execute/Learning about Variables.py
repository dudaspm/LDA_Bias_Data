#!/usr/bin/env python
# coding: utf-8

# # Learning about Variables

# When we are developing our idea, we sometimes need to use values multiple times or change the value based on our code. This concept is where variables become very helpful. Let's look at an example.
# 
# In this example, we are adding a few numbers together. In this instance, if all we care about is getting the result (similar to a calculator). Then variables are not needed. 

# In[1]:


5 + 3 + 16


# But let's look at an example where we need to get the circumference of a circle using multiple radii. The equation for the circumference of a circle is: $C = 2 \pi r$

# Let's say the radius is 5

# In[2]:


2 * 3.14159265359 * 5


# OK, how about radius 10 and 11 and 4 and ... 
# Well, in this example, we might not want to rewrite 3.14159265359 over and over. So, in this case, we want to create a variable for this, and we will call it pi. 

# In[3]:


pi = 3.14159265359


# Now, every time we reference the variable called **pi** it will refer to the number **3.14159265359**
# 
# Let's try those radii again (10, 11, 4)

# In[4]:


2 * pi * 10


# In[5]:


2 * pi * 11


# In[6]:


2 * pi * 4


# By the way, if you happen to get an error:
# ```javascript
# NameError: name 'pi' is not defined
# ```
# Make sure you go to the cell that has
# ```python
# pi = 3.14159265359
# ```
# and run this cell *first* then try the other calculations. 

# ## Type of Variables

# There are multiple types of variables. The most common (and the ones we will talk about) are:
# 
# * Integers (whole numbers)
# * Float (Floating points or numbers with a decimal)
# * Text
# * Lists
# * Dictionaries
# 
# The nice thing about Python is that we do **not** need to specify (or declare) which type we are using. Python will figure this out for us! 
# 
# BUT FIRST, a quick detour...
# 
# We need to talk about Camel Casing.

# ### Camel Case

# <img src="https://upload.wikimedia.org/wikipedia/commons/c/c8/CamelCase_new.svg" alt="camel case" width="100" style="float:right"/>
# Variable names must be one continuous string of letters/numbers. So, let's say we wanted to create a variable called "number of kittens." Instead calling this variable <em>number of kittens</em>, I would call it <em>numberOfKittens</em>. Why the capitalization? Because it makes it easier to separate the words in the name. As in, <em>numberofkittens</em> vs. <em>numberOfKittens</em>. We have a fun name for this: camel case. 

# <cite>File:CamelCase new.svg. (2020, April 15). Wikimedia Commons, the free media repository. Retrieved 15:25, June 3, 2020 from https://commons.wikimedia.org/w/index.php?title=File:CamelCase_new.svg&oldid=411544943.</cite>

# ### Integers or int

# As mentioned, integers are whole numbers. Let's create an example. How about we use our numberOfKittens. We will then set this value to 0. As in, we have 0 kittens.

# In[7]:


numberOfKittens = 0


# One thing we might want to do is to have Python tell us what **type** this variable is. Well, Python has a function for this called
# 
# ```python
# type()
# ```

# In[8]:


type( numberOfKittens )


# So this checks out, we made an int, and it is showing us we have an int.
# 
# Now, once we have a variable, it is not static. We can change the value as much as we need to. Running the next cell will continually add 10 to our original variable. 
# 
# Try running this a few times.

# In[9]:


numberOfKittens = numberOfKittens + 10
numberOfKittens


# In[10]:


from IPython.display import Markdown as md
md(f"**or**<br />in more human-readable terms. <br />numberOfKittens (new value {numberOfKittens})  = numberOfKittens (originally {numberOfKittens-10}) + 10<br />numberOfKittens is now {numberOfKittens}<br />**or**")


# In[11]:


from IPython.display import HTML as html
listOfCats = []
for i in range(numberOfKittens): 
    listOfCats.append("🐈")
   
display(html(' '.join([str(elem) for elem in listOfCats])))


# ### Floating points or floats

# Floats are similar to integers, but with more precision.
# Float comes from a Floating point or a number with a decimal point. 
# 
# This example starts at 0, but note that this is .0 
# Adding the decimal tells Python that we should have a float value instead of an integer. 

# In[12]:


aFloatVariable = .0


# Let's again, check the variable type. 

# In[13]:


type( aFloatVariable )


# Looks good. 
# 
# And again, we will add 10 to this. There is something specific interesting here; see if you spot it.

# aFloatVariable = aFloatVariable + 10
# aFloatVariable

# If you guessed "mixing a float and an integer," you got it. Let's see an example. 

# #### Mixing integers and floats

# In Python (3, more specifically), the variable will always take the form of the most precision. So, by default, a float.

# In[14]:


letsSeeWhatHappens = numberOfKittens + aFloatVariable
letsSeeWhatHappens


# We can force variables to be a certain type. We call this 'type-cast' and can be used to:
# 
# * make an integer into a float
# * a float to an integer
# * an integer to a string (we have not discussed this yet)
# * a float to a string (we have not discussed this yet)
# * etc...

# #### type-cast

# ```{note}
# type-cast is temporary. If you do not use a type-cast, the variable will revert to its original variable type. 
# ```

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

# In[15]:


float(numberOfKittens)


# In[16]:


int(aFloatVariable)


# ```{admonition} Common Question
# :class: tip
# What happens when you convert a float like .5 to an integer? Does it round up or down?
# ```

# Well let's see what happens.

# In[17]:


printList = []
for i in range(10): printList.append("for value %s we will get %s" % ((i/10),int(i/10)))

display(md('<br />'.join([str(elem) for elem in printList])))


# So, in conclusion. It will always round down.

# ### String or str

# So, up to this point, we started our conversation working with numbers. Well, what about the other things that are not numbers... like text? Well, for text, we use something called a String or str. 
# 
# Strings allow us to capture a single character up to thousands of characters (actually, much more than this). Let's go through a traditional example of "Hello, World!" but with my slight spin to it. 

# In[18]:


helloStatement = "Hello, everyone!"


# As you can see, can capture text and other alphanumeric and special characters. There are several unique functions for strings but first, let's double-check and see what type we from our helloStatement.

# In[19]:


type( helloStatement )


# Not too surprising, we see this is type str or string. 

# ```{note}
# For those coming from another programming language. Sometimes other programming languages will have a specific designation for a single character string or, as it is called, a character. Python has a one-size-fits-all label for text, and that is a string. Here, let me prove it. 
# ```

# In[20]:


singleCharacter = "a"
type( singleCharacter )


# #### String Indexing/String Slicing

# One of the first ways to interact with our string is to take a look at individual characters by using their **index**.
# 
# The **index** is position (or multiple positions) for each character in the string. So, if we look at our string, we have Hello, everyone! If we wanted to see the first letter *H*, we could reference this using the index or the position where the letter is in the string. 

# In[21]:


helloStatement[1] 


# ohh.. wait a minute. We were expecting the letter *H*, but we got *e*. What happened?

# ```{note}
# For indexes, we always start at the number 0. So, 0 is the first thing, 1 is the second thing, and so on.
# ```

# Let's try this again. 

# In[22]:


helloStatement[0]


# There we go! 

# Visually, this is how the string looks to Python. 
# 
# ![Hello, everyone! text](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/helloEveryone.png)

# In[23]:


get_ipython().run_cell_magic('html', '--isolated', '<label for="vol">Index value:&nbsp;</label><span id="letterindex">0</span><br><input type="range" id="vol" name="vol" min="0" max="16" value="0" oninput="document.getElementById(\'letterImages\').src=\'https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/l\'+(this.value)+\'.PNG\'; document.getElementById(\'letterindex\').innerHTML=this.value;"><br><img id="letterImages" alt="Individual letters in Hello, everyone!" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/l0.PNG" style="width:50px">\n')


# ##### Indexing Multiple Letters

# In[24]:


print( helloStatement[0:5] )


# Wait a second! 
# 
# ![Hello, everyone! text](https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/helloEveryone.png)

# The way you should think of this is: 
# 
# ```python
# helloStatement[0 : 5 - 1]
# helloStatement[(starting number) to (ending number - 1)]
# ```
# 
# There is also a shortcut way of writing this, without the 0. 

# In[25]:


print( helloStatement[:5] )


# In[26]:


print( helloStatement[5:] )


# #### String functions

# ##### Find

# In[27]:


print( helloStatement.find("one") )
print( helloStatement.find("me") )
print( helloStatement.find("hello") )
print( helloStatement.find("Hello") )


# ```{note}
# When using *.find()*, if the function can NOT find the sequence of the letters given. It will return -1. 
# ```

# ##### Formatting

# In[28]:


print( helloStatement.capitalize() )
print( helloStatement.lower() )


# ##### Split

# In[29]:


print( helloStatement.split(" ") )


# ```{note}
# *.split()* will eventually become your best friend. *.split()* is a **great** function to use when using uniquelly spaced data. 
# As in comma separated values or CSV. 
# ```

# ##### Chaining Functions

# In[30]:


print( helloStatement )
print( helloStatement[0:5].capitalize() )
print( helloStatement.find("hello") )
print( helloStatement[:5].lower().find("hello") )


# #### Concatenating Strings
# 
# When you want to put two strings together, we say you *concatenate* the strings. There are multiple ways of doing this but presented are what I believe to be the three most common ways. 

# ##### + Method

# This is the most straightforward method of the three, but there can be some issues. You simply add a plus sign *+* between your strings. Let's take a look at this. 

# In[31]:


print ( "hello, " + "everyone!")


# This works fine, but when you add a number to this idea. We run into issues. 

# ```python
# print ( "hello, " + "every" + 1 + "!")
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-41-1f53f06cad5c> in <module>
# ----> 1 print ( "hello, " + "every" + 1 + "!")
# 
# TypeError: can only concatenate str (not "int") to str
# ```

# In this case we need to *type-cast* the integer as a string using
# ```python
# str()
# ```

# In[32]:


print ( "hello, " + "every" + str(1) + "!")


# ##### % Method

# This is my favorite method out of the three. Let's see how this works with the same example. 
# 
# In this case, we use a %s (s = string) for each string we want to embed in our overall string. 

# In[33]:


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

# In[34]:


get_ipython().run_cell_magic('html', '', '<figure>\n<video width="720" height="360" controls muted >\n  <source src="https://github.com/dudaspm/JupyterLab-Python/blob/main/images/percent_cat.mp4?raw=true" type=video/mp4>\n</video>\n  <figcaption>(No Audio) Video of how % concatenate works with substituting strings. </figcaption>\n</figure>')


# OK, but what about numbers?

# In[35]:


print ( "%s, %s%s%s" % ("hello","every",1,"!") )


# Still works! This reason is why I like this method. You pick the formating and feed in the strings. 

# ##### join() Method

# The .join() method uses a function called
# ```python
# .join()
# ```
# This is a create function to be aware of, as it will allow you the ability to join strings with a specific, static format. What do I mean by static formatting? Well, unlike the % method, that can be formatted exactly how I want it. The .join() method requires a specific pattern. Example time!

# In[36]:


print ( " ".join(["hello, ", "everyone!"]) )


# There are two parts to this. 
# 
# *The splitter*
# ```python
# " "
# ```
# 
# *The fill*
# ```python
# .join(["hello, ", "everyone!"])
# ```
# 
# Notice that the join has the brackets around it. Technically, you are feeding this an array or list (we have not talked about this yet). This function again, like *.split()*, will be a great asset to you in the future. 
# 
# Let's show this with our number again. 

# ```python
# print ( " ".join(["hello, ", "every", 1, "!"]) )
# 
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-54-e926f0c4c025> in <module>
# ----> 1 print ( " ".join(["hello, ", "every", 1, "!"]) )
# 
# TypeError: sequence item 2: expected str instance, int found
# ```

# The same issue as before, we need to type-cast. 

# In[37]:


print ( " ".join(["hello, ", "every", str(1), "!"]) )


# Notice the spaces? Again, we are saying with *the splitter* what each string is going to be seperated by, so in this case, everything will be split by spaces. 

# ### Booleans

# Booleans are used to do comparisions (true/false), (1/0), (yes/no)

# In[38]:


someCondition = True
type( someCondition )


# #### Boolean Logic

# We will talk about boolean logic more in the next section (Comparisons)

# In[39]:


(someCondition == False)


# In[40]:


if (False): 
    print( "yes for False!" )
if (True): 
    print( "yes for True!" )


# ```{note}
# A more "traditional" way to do booleans is to use 0 and 1. In Python, any number other than 0 is True. Including negative numbers and decimals. 
# ```

# In[41]:


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

# In[42]:


groceryList = ["apple", "banana", "eggs"]
print( groceryList )


# 2. Create a list and add to it using
# 
# ```python 
# .append()
# ```

# In[43]:


groceryList = []
groceryList.append("apple")
groceryList.append("banana")
groceryList.append("eggs")
print( groceryList )


# ```{note}
# For indexes, we always start at the number 0. So, 0 is the first thing, 1 is the second thing, and so on.
# ```

# In[44]:


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

# ### Dictionary

# Dictionaries are used to index based on a specific key. As in:
# 
# dictionary[\"street adddress\" (key)] = "123 Apple St." (value)

# In[45]:


personalInformation = {}
personalInformation["streetAddress"] = "123 Apple St."
personalInformation["firstName"] = "Patrick"
personalInformation["lastName"] = "Dudas"
print( personalInformation )


# Note the order.

# Again, to do this more efficiently, we will be using loops (we will talk about later).

#!/usr/bin/env python
# coding: utf-8

# # Creating a Function

# Functions allow us to do repeated tasks easily by writing the code only once.  Functions will have a name, inputs, and outputs and can be called anywhere the task is repeated.
# 
# There are functions that are built into python; for example, we have already been using the type() function, which tells us the type of variable we are using.  Note that print is also a function!

# In[1]:


aVal = 10.0
print( type( aVal ) )


# Functions have four typical parts:
# * Name - what you call your function
# * Input arguments - what you provide
# * Outputs - what the function gives back
# * Math/Magic - what the function does

# ## Creating Our Own Function

# In python, we use def to define a function with the function name and inputs followed by a colon.  The python function is then separated from the rest of the code by a tab. Some languages use braces rather than indentation.
# ````python
# def functionName( inputs ):
#     # Operate on the inputs
#     ouputs = inputs + 5
#     # Return what we want to back
#     return outputs;
#    ````

# Let's look at an example function, which changes degrees Fahrenheit to Celsius. 

# In[2]:


def changeFromFToC( farVal ):
    cVal = (farVal - 32.0) * 5.0 / 9.0
    return cVal 


# Here, our function name is *changeFromFToC*, the input is *farVal*, the temperature in Fahrenheit, the output is *cVal*, and the temperature in Celsius. We can print or store the output from the function.  Note that the function has to be defined before we use it - the cell with the function definition has to have run before we can call the function.

# In[3]:


print( "Change 14 deg F to Celsius" )
print( changeFromFToC( 14 ) )

print( "Change from 68 deg F to Celsius" )
niceTempC = changeFromFToC( 68 )
print( niceTempC )


# Your turn! What is the temperature today? Convert it to Celsius. 
# 
# For those who have the temperature in Celsius and want to convert it to Fahrenheit. Define a new function to do this.

# ### Multiple inputs and outputs

# Here is an example of multiple outputs. We can actually work the output in a couple of different ways.

# #### Multiple Output Function

# In[4]:


def changeFromFToCAndK( farVal ):
    # Change the temperature from Fahrenheit to Celsius and Kelvin
    cVal = (farVal - 32.0) * 5.0 / 9.0
    kVal= cVal + 273.15
    return cVal, kVal  


# #### Output: List

# In[5]:


def changeFromFToCAndK( farVal ):
    # Change the temperature from Fahrenheit to Celsius and Kelvin
    cVal = (farVal - 32.0) * 5.0 / 9.0
    kVal= cVal + 273.15
    return cVal, kVal    
    
print( "Change 14 deg F to Celsius and Kelvin" )
print( changeFromFToCAndK( 14 ) )

print( "Change 32 deg F to Celsius and Kelvin" )
freezing = changeFromFToCAndK( 32 ) 
print( freezing[0] )
print( freezing[1] )


# #### Output: Multiple Variables 

# In[6]:


print( "Change 212 deg F to Celsius and Kelvin" )
boilingC, boilingK = changeFromFToCAndK( 212 ) 
print( boilingC )
print( boilingK )


# #### Multiple Input Function

# In[7]:


def changeFromFToCOrK( farVal, tempType ):
    if (tempType == "C"):
        return (farVal - 32.0) * 5.0 / 9.0
    elif (tempType == "K"):
        return ((farVal - 32.0) * 5.0 / 9.0) + 273.15
    else:
        return "invalid temperature type"


# In[8]:


print ( changeFromFToCOrK(70,"C") )


# In[9]:


print ( changeFromFToCOrK(70,"K") )


# In[10]:


print ( changeFromFToCOrK(70,"W") )


# ### Functions calling other functions

# Functions can call other functions.  Here we add three using a function to add two and then adding one.

# In[11]:


def addTwo( inValAddTwo ):
    # Add two to the input
    return inValAddTwo + 2

def addThree( inValAddThree ):
    # Add three two the input
    return addTwo( inValAddThree ) + 1

# Add three to four
print( "Add three to four using addThree (which adds 1) but calls addTwo (which adds 2)" )
print( addThree( 4 ) )


# ### Recursive Functions

# Functions can also call themselves - these are called recursive functions.  See how we calculate the factorial by subtracting one and calling the function again. 

# In[12]:


def factorialRecursive( facIn ):
    print ("In factorialRecursive() and the current number is:", facIn)
    if facIn == 1:
        return facIn
    else:
        return facIn * factorialRecursive( facIn - 1)

print( "Use a recursive function to calculate the factorial of 5" )
print( factorialRecursive( 5 ) )


# ### Function Gotcha! 😆 

# ```{note}
# The biggest gotcha on functions is with variable scope: 
# * Variables defined in a function are not accessible from the outside
# * Functions have access to more than just the variables passed in
# ```

# In[13]:


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

# ## Your Turn

# Try to fill in code to fulfill the request!  Here is a variable used in the excercises.

# In[14]:


aListOfNumbers = [6, 3, 4, 5, 7, 8, 9 ]


# Write a function that returns the length of aListOfNumbers as well as the maximum value. Hint: max() is a built-in function

# In[15]:


## try here!


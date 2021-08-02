#!/usr/bin/env python
# coding: utf-8

# # A Python guessing game for jupyter

# Play the existing game with the first cell!  The only things here that we did not talk about in Seminar 1 are:
# * isdigit() - a function to see if a string can be transformed into an integer without error
# * randInt from the random module - a function to create a random integer 

# In[1]:


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# guessingGame
# A python number guessing game
#
# Adam Lavely
# adam.lavely.psu@gmail.com
#
# Created for ICS Python Training Series
# Spring 2019
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# This is a number guessing game.  Python
# uses a random number generator to get
# a target between minVal and maxVal
# and then the guesser must guess this
# number using greater/less than clues.
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Load the modules we need

# Use random to get the random number 
import random as rd 

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Functions required

def guessChecker( guessVal ):
    # Function to verify that the guess an integer
    if guessVal.isdigit() == True:
        return True
    else:
        print("Bad input, please use an integer")
        return False
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Background info
minVal=1
maxVal=100
goodGuesses=1
ANSWER=rd.randint( minVal, maxVal)
answerRight = 'Nope'


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Play the game
print( "Guess an integer such that", minVal, " <= X <= ", maxVal )

while answerRight == 'Nope':
    
    # Get the guess
    
    guess = input("\nEnter an integer: ")
    
    # Check to make sure the guess is an integer
    goodAns = guessChecker( guess )
    
    # Yes an integer
    if goodAns == True:
        guessInt = int( guess ) 
        
        # Check to see if guess is above the answer 
        if guessInt > ANSWER:
            print("Answer is too high, please guess again")
            maxVal = guessInt
            goodGuesses = goodGuesses+1
            print( "Your current inclusive range is ", minVal, " - ", maxVal )
        elif guessInt < ANSWER:
            print("Answer is too low, please guess again")
            minVal = guessInt
            goodGuesses = goodGuesses+1
            print( "Your current inclusive range is ", minVal, " - ", maxVal )
        else:
            print("\nHurray, you guessed ", ANSWER, " in ", goodGuesses, " guesses! " )
            answerRight = 'Yep'
    
    # Not an integer
    else:
        print( "Please try again")    


# Can you add a range checker to the code using a function? Take an initial guess of 100000001: this is an integer and so will pass the current check, but it is out of the existing range. Your updated code should limit your guesses to the current range. (Note the maxVal is set to 10 here to make debugging easier.)

# In[ ]:


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# guessingGame
# A python number guessing game
#
# Originally written: Adam Lavely 
# adam.lavely.psu@gmail.com
#
# Modified by: YOUR NAME
# YOUR EMAIL ADDRESS
#
# Created for ICS Python Training Series
# Spring 2019
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# This is a number guessing game.  Python
# uses a random number generator to get
# a target between minVal and maxVal
# and then the guesser must guess this
# number using greater/less than clues. 
#
# MODIFICATION: 
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Load the modules we need

# Use random to get the random number 
import random as rd 

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Functions required

def guessChecker( guessVal ):
    # Function to verify that the guess an integer
    if guessVal.isdigit() == True:
        return True
    else:
        print("Bad input, please use an integer")
        return False
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Background info
minVal=1
maxVal=10
goodGuesses=1
ANSWER=rd.randint( minVal, maxVal)
answerRight = 'Nope'


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# Play the game
print( "Guess an integer such that", minVal, " <= X <= ", maxVal )

while answerRight == 'Nope':
    
    # Get the guess
    
    guess = input("\nEnter an integer: ")
    
    # Check to make sure the guess is an integer
    goodAns = guessChecker( guess )
    
    # Yes an integer
    if goodAns == True:
        guessInt = int( guess ) 
        
        # Check to see if guess is above the answer 
        if guessInt > ANSWER:
            print("Answer is too high, please guess again")
            maxVal = guessInt
            goodGuesses = goodGuesses+1
            print( "Your current inclusive range is ", minVal, " - ", maxVal )
        elif guessInt < ANSWER:
            print("Answer is too low, please guess again")
            minVal = guessInt
            goodGuesses = goodGuesses+1
            print( "Your current inclusive range is ", minVal, " - ", maxVal )
        else:
            print("\nHurray, you guessed ", ANSWER, " in ", goodGuesses, " guesses! " )
            answerRight = 'Yep'
    
    # Not an integer
    else:
        print( "Please try again")  


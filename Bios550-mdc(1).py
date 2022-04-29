#!/usr/bin/env python
# coding: utf-8

# # Problem 1:  Username
# - Write a function named **get_user_name** that asks the user for their name with the phrase, *“Greetings, what is your name?”*
# - The function should store the user’s response in a variable name, print “Welcome to Bioinformatics, <name>!” and then return name. (Python input function)

# In[133]:


get_user_name = input("Greetings, what it your name?")
print("Welcome to Bioinformatics,", get_user_name,"!")


# # Problem 2: Area
# - Write a function named **calculate_circle_area** that takes **radius** as an argument.
# - This function should use that radius to calculate the area of a circle with that radius and return this value.
# - Hint: you will need to import either the math or numpy library to get the value of π!

# In[43]:


import math

def calculate_circle_area(radius):
    area = math.pi*radius**2
    return area

print('Area of Circle with a Radius of 5 =', calculate_circle_area(5))


# # Problem 3: Word Search
# - Write a function named **letter_word_search** that takes a string text and a char letter as arguments
# - This function should search text for all words that begin with letter and should return these values in a list
#     - Bonus: Check whether letter consists of a single character rather than a number or multi-character string!

# In[158]:


words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']


# In[159]:


def letter_word_search(name_list, letter):
    output_list = []
    for name in name_list:
        if name[0] == letter:
            output_list.append(name)
            
    return output_list


# In[160]:


letter_word_search(words, 'a')


# # Problem 4: Number Guessing Game
# - Write a function named **number_guessing_game** that selects a random number target between **0 and 36 (inclusive)**.
# - This function should then prompt the user for input guess with the statement, “I’m thinking of a number between 0 and 36. Can you guess what it is?” 
# - The user’s input guess should be compared to the target. If they guessed correctly, the program should print, “You guessed <guess>. My number was <target>. Congrats!” to terminal.
# - If they guessed incorrectly, the function should print, “You guessed <guess>. My number was <target>. Sorry, try again!”!

# In[15]:


import random

def guess_number(a, b):
    target = random.randint(a,b)
    guess = input("I'm thinking of a number between " + str(a) + " and " + str(b) + "." + " Can you guess what it is?" )
    if (str(target) == guess):
        print("You guessed " + str(guess) + ". My number was " + str(target) + ". Congrats!")
        return True
    else:
        print("You guessed " + str(guess)+ ". My number was " + str(target)+ ". Sorry, try again!")
        return False


# In[16]:


correct = guess_number(0,2)


# ****

# ### Problem 5: Approximating π
# - The value of pi can be calculated using a Monte Carlo simulation by **randomly** n points within a unit square (i.e. a square with side length = 1) and by determining whether those points would land within an inscribed unit circle (i.e. a circle with diameter = 1; see illustration).
# - Given the relationship between the area of a unit square (1) and the area of a unit circle (π/4 ), we know that: **π=4*  (number of points falling within circle)/n**
# - Write a function named **simulate_pi** that takes an integer n as an argument. This function should randomly select n points within a unit square (i.e. x and y coordinates between 0 and 1).
# - This function should then count the number of points that fall within the circle (i.e. the distance between the center of the circle (0.5, 0.5) and the randomly selected point ≤ 0.5).
# - The function should return an estimation of π using the equation given above.

# In[17]:


import random
import math
#length = 1; diameter = 1
#π=4* (number of points falling within circle)/n
#fxn: simulate_pi = random select 0,1
def simulate_pi(n):
    count = 0 
    for i in range(0,n):
        x = random.random()
        y = random.random()
        d = math.dist([x,y],[0.5,0.5])
        if(d <= 0.5):
            count = count + 1
    return 4*count/n


# In[18]:


simulate_pi(200000)


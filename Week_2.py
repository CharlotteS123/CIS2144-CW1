"""
Created on Thu Oct 14 11:46:34 2021

@author: 24445223
"""
"""
Problem 1
This is a program that find numbers, from the range 1000 to 2000 inclusive, that
are divisible by 11, but are not multiple of 3. 
"""
finalline = ""
for i in range(1000,2001): 
    if (i % 11 == 0) and (i % 3!= 0): # if statement for numbers / 11 but !/ 3
        finalline += str(i) + ", " # adds a comma and space to numbers for format
    else:         
        continue
print (finalline[:-2]) # final part of string doesn't include ", "

"""
Problem 2
This program allows a user to input a sentence, then displays how many upper
case and lower case letters there are.
"""
upper = 0
lower = 0
sentence = input("Please enter your sentence: ")
for i in range (len(sentence)): # if statement for the type of letter
    if sentence[i].isalpha() == False:
        continue
    elif sentence[i] == sentence[i].upper():
        upper += 1
    elif sentence[i] == sentence[i].lower():
        lower += 1
print("There are " + str(upper) + " upper case letters and " + str(lower) + \
      " lower case letters in your sentence")

print("") # final formatting

"""
Problem 3
This was to create a function that changes a integer into a string, and then 
this function was to be called to print an user inputted number.
"""
def int_to_string(a):
    """
    Converts the inputted number to a string then returns this.
    
    :param a: is a integer that is going to be converted
    :return: the string version of 'a'
    """
    return str(a)
inputted = input("Please enter a number: ")
print(int_to_string(inputted))

print ("") # final formatting

"""
Problem 4
This was to generate all possible sentences from three lists, where the sentence
contains three words, one from each list in the order they appear.
"""
a = (["I", "You"], ["Read", "Borrow"], ["Shakespeare's plays", "Shakespeare's poems"])
import itertools
for list in itertools.product(*a): 
  print (list);
  
# Problem 5
import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.array([1,2,3])
y = np.array([2,4,1])

plt.plot(x,y)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Problem 5")
plt.show()

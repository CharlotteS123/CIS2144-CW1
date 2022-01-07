"""
Created on Thu Oct  7 12:08:14 2021.

@author: 24445223
"""
"""
Problem 1
This calculates the answer to 52 + 78 and displays it in the console.
"""
num1 = 52
num2 = 78
answer = num1 + num2
print ("The value of", num1 , "+", num2 , "is", answer) # prints the answer to 52+78

print("") # for final layout only

"""
Problem 2
This prints the text 'Hello, World!' four times.
"""
for i in range(4): # for loop that prints next statement four times
    print ("Hello, World!") 

print("") # for final layout only

"""
Problem 3
This prints the song 'Twinkle, twinkle little star' on separate lines and 
in a specific format using \t -> inserts a tab.
"""
print("""Twinkle, twinkle little star, 
\tHow I wonder what you are! 
\t\tUp above the world so high,

\t\tLike a diamond in the sky.
Twinkle, twinkle, little star,
\tHow I wonder what you are""")

print("") # for final layout only

"""
Challenge 1
This prints only the present index letters of an entered string.
"""
inputvalue = input("Please enter a string: ") # takes user input
evenindex = "" 
for i in range (len(inputvalue)): 
    if i % 2 != 0: # if statement for if i isn't even
        continue 
    else: # if statement for if i is even
        evenindex += inputvalue[i] + ", " 
print (evenindex[:-2]) # prints the text in the string final, apart from last two comma and space

print("") # for final layout only

"""
Challenge 2
This prints a pattern of numbers out from a function.
"""
def pattern(iterations):
    """
    pattern prints each iteration of number that many times, e.g. 2 is printed twice.
    
    :param iterations: is the number of iterations the for loop goes through
    :return: the string final pattern, which contains the completed pattern
    """
    finalpattern = ""
    for i in range (iterations + 1): # + 1 because otherwise it would cut off one before
        for j in range (i): 
            stringi = str(i) 
            finalpattern += stringi + " "
        finalpattern += "\n"
    return finalpattern 
print (pattern(5)) 